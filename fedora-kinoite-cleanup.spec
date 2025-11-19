Name:           cosmo-kinoite-cleanup
Version:        1.4
Release:        1%{?dist}.cosmo
Summary:        Cleanup scripts for Fedora Kinoite
License:        MIT
BuildArch:      noarch

Source0:        kinoite-cleanup-cosmo-1.4.tar.gz

%description
Custom cleanup scripts for Fedora Kinoite.
This package installs:
- system-clean.sh
- kinoite-clean.sh
- flatpak-clean.sh
and timer units for automated cleanup.

%prep
%setup -q -n cosmo-kinoite-cleanup-1.4

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/systemd/system

install -m 0755 payload/usr/bin/*.sh %{buildroot}/usr/bin/
install -m 0644 payload/etc/systemd/system/*.service %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/*.timer %{buildroot}/etc/systemd/system/

%files
/usr/bin/kinoite-clean.sh
/usr/bin/flatpak-clean.sh
/usr/bin/system-clean.sh
/etc/systemd/system/kinoite-clean.service
/etc/systemd/system/kinoite-clean.timer
/etc/systemd/system/flatpak-clean.service
/etc/systemd/system/flatpak-clean.timer
/etc/systemd/system/system-clean.service
/etc/systemd/system/system-clean.timer

%changelog
* Thu Nov 20 2025 Cosmo <cosmopolitz@example.com> - 1.4-1
- Initial custom release
