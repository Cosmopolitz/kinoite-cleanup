#!/usr/bin/bash
set -euo pipefail

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')  [kinoite-clean] $*" | tee -a /var/log/kinoite-clean.log
}

log "Starting rpm-ostree cleanup…"

rpm-ostree cleanup -m | tee -a /var/log/kinoite-clean.log

log "rpm-ostree cleanup completed."
