package gitsync

import (
	"log"
	"os"
	"path/filepath"
	"sync"
	"time"

	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/config"
	"github.com/go-git/go-git/v5/plumbing"
)

type SyncManager struct {
	repoURL   string
	localPath string
	branch    string
	repo      *git.Repository
	mu        sync.Mutex
}

func NewSyncManager(repoURL, localPath string) *SyncManager {
	return &SyncManager{
		repoURL:   repoURL,
		localPath: localPath,
		branch:    "master",
	}
}

func (s *SyncManager) SetBranch(branch string) {
	s.branch = branch
}

func (s *SyncManager) Clone() (bool, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if _, err := os.Stat(filepath.Join(s.localPath, ".git")); err == nil {
		log.Printf("Repository exists at %s, opening", s.localPath)
		repo, err := git.PlainOpen(s.localPath)
		if err != nil {
			return false, err
		}
		s.repo = repo
		changed, err := s.syncLocked()
		if err != nil {
			log.Printf("Existing repository sync failed, recloning: %v", err)
			return s.recloneLocked()
		}
		return changed, nil
	}

	return s.cloneFreshLocked()
}

func (s *SyncManager) Pull() (bool, error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	return s.syncLocked()
}

func (s *SyncManager) cloneFreshLocked() (bool, error) {
	if err := os.MkdirAll(filepath.Dir(s.localPath), 0o755); err != nil {
		return false, err
	}

	log.Printf("Cloning %s to %s", s.repoURL, s.localPath)
	start := time.Now()

	repo, err := git.PlainClone(s.localPath, false, &git.CloneOptions{
		URL:           s.repoURL,
		ReferenceName: plumbing.NewBranchReferenceName(s.branch),
		SingleBranch:  true,
		Tags:          git.NoTags,
		Progress:      os.Stdout,
	})
	if err != nil {
		return false, err
	}

	s.repo = repo
	log.Printf("Clone completed in %v", time.Since(start))
	return true, nil
}

func (s *SyncManager) recloneLocked() (bool, error) {
	s.repo = nil
	if err := os.RemoveAll(s.localPath); err != nil {
		return false, err
	}
	return s.cloneFreshLocked()
}

func (s *SyncManager) syncLocked() (bool, error) {
	if s.repo == nil {
		return false, nil
	}

	log.Printf("Fetching %s", s.repoURL)
	start := time.Now()

	err := s.repo.Fetch(&git.FetchOptions{
		RemoteName: "origin",
		RefSpecs: []config.RefSpec{
			config.RefSpec("+refs/heads/" + s.branch + ":refs/remotes/origin/" + s.branch),
		},
		Tags:     git.NoTags,
		Force:    true,
		Progress: os.Stdout,
	})
	if err != nil && err != git.NoErrAlreadyUpToDate {
		return false, err
	}

	remoteRef, err := s.repo.Reference(plumbing.NewRemoteReferenceName("origin", s.branch), true)
	if err != nil {
		return false, err
	}

	headRef, err := s.repo.Head()
	if err != nil {
		return false, err
	}

	if headRef.Hash() == remoteRef.Hash() {
		log.Printf("Already up to date (%v)", time.Since(start))
		return false, nil
	}

	w, err := s.repo.Worktree()
	if err != nil {
		return false, err
	}

	if err := w.Reset(&git.ResetOptions{
		Commit: remoteRef.Hash(),
		Mode:   git.HardReset,
	}); err != nil {
		return false, err
	}

	log.Printf("Sync completed in %v", time.Since(start))
	return true, nil
}

func (s *SyncManager) ContentPath() string {
	return filepath.Join(s.localPath, "hugo-site", "content")
}

func (s *SyncManager) LocalPath() string {
	return s.localPath
}
