#!/usr/bin/bash
set -euo pipefail

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')  [flatpak-clean] $*" | tee -a /var/log/kinoite-clean.log
}

log "Running Flatpak cleanup..."

flatpak uninstall --unused -y 2>&1 | tee -a /var/log/kinoite-clean.log || true
flatpak repair -y 2>&1 | tee -a /var/log/kinoite-clean.log || true

log "Flatpak cleanup completed."
