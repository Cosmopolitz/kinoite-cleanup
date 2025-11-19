Name:           cosmo-kinoite-cleanup
Version:        1.4
Release:        1%{?dist}.cosmo
Summary:        Automated cleanup scripts for Fedora Kinoite
License:        MIT

BuildArch:      noarch

Source0:        kinoite-cleanup-cosmo-%{version}.tar.gz

%description
Custom cleanup scripts for Fedora Kinoite.
Includes:
- Flatpak cleanup
- rpm-ostree cleanup
- System cache cleanup
- Systemd timers for automatic maintenance

%prep
%setup -q -n cosmo-kinoite-cleanup-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/systemd/system

install -m 0755 payload/usr/bin/kinoite-clean.sh %{buildroot}/usr/bin/
install -m 0755 payload/usr/bin/flatpak-clean.sh %{buildroot}/usr/bin/
install -m 0755 payload/usr/bin/system-clean.sh %{buildroot}/usr/bin/

install -m 0644 payload/etc/systemd/system/kinoite-clean.service %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/kinoite-clean.timer %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/flatpak-clean.service %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/flatpak-clean.timer %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/system-clean.service %{buildroot}/etc/systemd/system/
install -m 0644 payload/etc/systemd/system/system-clean.timer %{buildroot}/etc/systemd/system/

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
* Wed Nov 19 2025 Cosmopolitz <cosmo@example.com> - 1.4-1
- Initial release of cosmo-kinoite-cleanup

