package gitsync

import (
	"log"
	"os"
	"path/filepath"
	"sync"
	"time"

	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
)

type SyncManager struct {
	repoURL   string
	localPath string
	branch    string
	repo      *git.Repository
	mu        sync.Mutex
	onSync    func()
}

func NewSyncManager(repoURL, localPath string, onSync func()) *SyncManager {
	return &SyncManager{
		repoURL:   repoURL,
		localPath: localPath,
		branch:    "master",
		onSync:    onSync,
	}
}

func (s *SyncManager) SetBranch(branch string) {
	s.branch = branch
}

func (s *SyncManager) Clone() error {
	s.mu.Lock()
	defer s.mu.Unlock()

	if _, err := os.Stat(filepath.Join(s.localPath, ".git")); err == nil {
		log.Printf("Repository exists at %s, opening", s.localPath)
		repo, err := git.PlainOpen(s.localPath)
		if err != nil {
			return err
		}
		s.repo = repo
		return s.pullLocked()
	}

	log.Printf("Cloning %s to %s", s.repoURL, s.localPath)
	start := time.Now()

	repo, err := git.PlainClone(s.localPath, false, &git.CloneOptions{
		URL:           s.repoURL,
		ReferenceName: plumbing.NewBranchReferenceName(s.branch),
		SingleBranch:  true,
		Depth:         1,
		Progress:      os.Stdout,
	})
	if err != nil {
		return err
	}

	s.repo = repo
	log.Printf("Clone completed in %v", time.Since(start))

	if s.onSync != nil {
		s.onSync()
	}

	return nil
}

func (s *SyncManager) Pull() error {
	s.mu.Lock()
	defer s.mu.Unlock()
	return s.pullLocked()
}

func (s *SyncManager) pullLocked() error {
	if s.repo == nil {
		return nil
	}

	log.Printf("Pulling from %s", s.repoURL)
	start := time.Now()

	w, err := s.repo.Worktree()
	if err != nil {
		return err
	}

	err = w.Pull(&git.PullOptions{
		RemoteName:    "origin",
		ReferenceName: plumbing.NewBranchReferenceName(s.branch),
		SingleBranch:  true,
		Progress:      os.Stdout,
	})

	if err == git.NoErrAlreadyUpToDate {
		log.Printf("Already up to date (%v)", time.Since(start))
		return nil
	}
	if err != nil {
		return err
	}

	log.Printf("Pull completed in %v", time.Since(start))

	if s.onSync != nil {
		s.onSync()
	}

	return nil
}

func (s *SyncManager) ContentPath() string {
	return filepath.Join(s.localPath, "hugo-site", "content")
}

func (s *SyncManager) LocalPath() string {
	return s.localPath
}
