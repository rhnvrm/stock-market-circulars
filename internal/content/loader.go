package content

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/rhnvrm/stock-market-circulars/internal/models"
	"gopkg.in/yaml.v3"
)

// Loader handles reading and parsing circular markdown files
type Loader struct {
	contentDir string
}

// NewLoader creates a new content loader
func NewLoader(contentDir string) *Loader {
	return &Loader{contentDir: contentDir}
}

// LoadSummary reads only the frontmatter to build index quickly
func (l *Loader) LoadSummary(path string) (*models.CircularSummary, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("failed to open file: %w", err)
	}
	defer f.Close()

	frontmatter, err := l.extractFrontmatter(f)
	if err != nil {
		return nil, fmt.Errorf("failed to extract frontmatter: %w", err)
	}

	var c models.Circular
	if err := yaml.Unmarshal(frontmatter, &c); err != nil {
		return nil, fmt.Errorf("failed to parse frontmatter: %w", err)
	}

	// Derive fields from path and filename
	c.FilePath = path
	c.Slug = l.extractSlug(path)
	if !c.Date.Time.IsZero() {
		c.Year = c.Date.Year()
	}

	return c.ToSummary(), nil
}

// LoadFull reads the entire file including content
func (l *Loader) LoadFull(path string) (*models.Circular, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		return nil, fmt.Errorf("failed to read file: %w", err)
	}

	// Split frontmatter and body
	parts := bytes.SplitN(content, []byte("---"), 3)
	if len(parts) < 3 {
		return nil, fmt.Errorf("invalid markdown format: missing frontmatter")
	}

	var c models.Circular
	if err := yaml.Unmarshal(parts[1], &c); err != nil {
		return nil, fmt.Errorf("failed to parse frontmatter: %w", err)
	}

	// Store raw markdown content
	c.RawContent = string(bytes.TrimSpace(parts[2]))
	c.FilePath = path
	c.Slug = l.extractSlug(path)
	if !c.Date.Time.IsZero() {
		c.Year = c.Date.Year()
	}

	return &c, nil
}

// extractFrontmatter reads only the frontmatter section
func (l *Loader) extractFrontmatter(f *os.File) ([]byte, error) {
	scanner := bufio.NewScanner(f)
	var frontmatter bytes.Buffer
	inFrontmatter := false
	lineCount := 0

	for scanner.Scan() {
		line := scanner.Text()

		if line == "---" {
			if !inFrontmatter {
				inFrontmatter = true
				continue
			} else {
				// End of frontmatter
				break
			}
		}

		if inFrontmatter {
			frontmatter.WriteString(line)
			frontmatter.WriteByte('\n')
			lineCount++

			// Safety limit to avoid reading entire file
			if lineCount > 200 {
				break
			}
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return frontmatter.Bytes(), nil
}

// extractSlug derives slug from filename
func (l *Loader) extractSlug(path string) string {
	base := filepath.Base(path)
	return strings.TrimSuffix(base, ".md")
}
