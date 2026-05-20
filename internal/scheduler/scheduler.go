package scheduler

import (
	"log"

	"github.com/robfig/cron/v3"
)

type Scheduler struct {
	cron *cron.Cron
}

func New() *Scheduler {
	return &Scheduler{
		cron: cron.New(cron.WithSeconds()),
	}
}

// AddSyncJob adds a job with a cron expression.
// Examples: "0 0 * * * *" (hourly), "@every 1h", "@every 5m"
func (s *Scheduler) AddSyncJob(cronExpr string, syncFn func()) error {
	_, err := s.cron.AddFunc(cronExpr, syncFn)
	return err
}

func (s *Scheduler) Start() {
	log.Println("Starting scheduler")
	s.cron.Start()
}

func (s *Scheduler) Stop() {
	log.Println("Stopping scheduler")
	ctx := s.cron.Stop()
	<-ctx.Done()
}
