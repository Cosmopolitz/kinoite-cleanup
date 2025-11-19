# kinoite-cleanup
Automatic cleanup package for Fedora Kinoite
📦 Kinoite Cleanup – Installering & Bruk

Kinoite Cleanup

Automatisert systemvedlikehold for Fedora Kinoite. Leveres som rpm-ostree-vennlig RPM-pakke og oppdateres automatisk via GitHub Actions.

✨ Funksjoner

Rydder Flatpak-cache
Rydder /tmp, /var/tmp, bruker-cache
Rydder systemd-journaler (safe)
Kjører rpm-ostree cleanup -m
Logger alt til /var/log/system-clean.log
Inkluderer systemd-timers for automatisk vedlikehold

🚀 Installasjon
sudo rpm-ostree install cosmo-kinoite-cleanup
systemctl reboot

🕒 Automatiske jobber
Timer	Oppgave	Frekvens
flatpak-clean.timer	Rydder Flatpak	ukentlig
kinoite-clean.timer	rpm-ostree cleanup	månedlig
system-clean.timer	systemcache / journal	ukentlig

🔧 Manuell kjøring
sudo system-clean.sh
sudo flatpak-clean.sh
sudo kinoite-clean.sh

📄 Logg
sudo cat /var/log/system-clean.log

❌ Avinstallasjon
sudo rpm-ostree uninstall cosmo-kinoite-cleanup
systemctl reboot
