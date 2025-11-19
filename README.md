# kinoite-cleanup
Automatic cleanup package for Fedora Kinoite
📦 Kinoite Cleanup – Installering & Bruk

Dette prosjektet gir automatisk vedlikehold for Fedora Kinoite:

🧹 Flatpak-rensing (ukentlig)

🧹 rpm-ostree-maintenance (månedlig)

🧹 Systemfil-rensing (ukentlig)

📝 Logger til /var/log/system-clean.log

⚙️ Fullt rpm-ostree-kompatibelt (ingen overrides!)

🚀 Installasjon
1. Legg til repoet ditt

Repoet inneholder ferdig bygde RPM-filer.

sudo tee /etc/yum.repos.d/kinoite-cleanup.repo << 'EOF'
[kinoite-cleanup]
name=Kinoite Cleanup Repo
baseurl=https://raw.githubusercontent.com/Cosmopolitz/kinoite-cleanup/main/repo/
enabled=1
gpgcheck=0
EOF

2. Installer pakken
sudo rpm-ostree install cosmo-kinoite-cleanup
systemctl reboot

⚙️ Etter omstart

Systemet vil automatisk ha aktivert:

Timer	Frekvens	Oppgave
flatpak-clean.timer	ukentlig	Rydder Flatpak-cache
kinoite-clean.timer	månedlig	Kjører rpm-ostree cleanup
system-clean.timer	ukentlig	Journal, cache, tmp osv.

Sjekk status:

systemctl status flatpak-clean.timer
systemctl status kinoite-clean.timer
systemctl status system-clean.timer

📄 Logg

All system-rens logges til:

/var/log/system-clean.log

Vis logg:

sudo cat /var/log/system-clean.log

🔧 Manuell kjøring

Du kan når som helst kjøre alle renseskript manuelt:

sudo /usr/bin/kinoite-clean.sh
sudo /usr/bin/flatpak-clean.sh
sudo /usr/bin/system-clean.sh

🧨 Avinstallasjon
sudo rpm-ostree uninstall cosmo-kinoite-cleanup
systemctl reboot

Dette fjerner alle timers, tjenester og skripter.
