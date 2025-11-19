#!/usr/bin/bash
set -euo pipefail

LOGFILE="/var/log/system-clean.log"

# Ensure logfile exists BEFORE redirect
if [ ! -f "$LOGFILE" ]; then
    touch "$LOGFILE"
    chmod 644 "$LOGFILE"
fi

# Redirect all output to logfile (stdout + stderr)
exec >> "$LOGFILE" 2>&1

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

log "=== System cleanup started ==="

# --------------------------------------------------------------------
# Clean journal logs
# --------------------------------------------------------------------
log "Cleaning journal logs older than 2 days..."
journalctl --vacuum-time=2d

# --------------------------------------------------------------------
# Clean system cache (safe subset)
# --------------------------------------------------------------------
log "Cleaning safe system cache directories..."
rm -rf /var/cache/fontconfig/* || true
rm -rf /var/cache/ldconfig/* || true
rm -rf /var/cache/man/* || true

# --------------------------------------------------------------------
# Clean per-user cache
# --------------------------------------------------------------------
log "Cleaning user caches..."
for userhome in /home/*; do
    if [ -d "$userhome/.cache" ]; then
        rm -rf "$userhome/.cache/"* || true
    fi
done

# --------------------------------------------------------------------
# Clean temporary directories
# --------------------------------------------------------------------
log "Cleaning /tmp and /var/tmp..."
rm -rf /tmp/* /var/tmp/* || true

# --------------------------------------------------------------------
# rpm-ostree specific cleanup
# --------------------------------------------------------------------
log "Running rpm-ostree maintenance cleanup..."
rpm-ostree cleanup -m || true

log "=== System cleanup finished ==="
