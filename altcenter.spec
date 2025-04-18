%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: altcenter
Version: 1.0
Release: alt0.7
Summary: Application for show information and configure system

License: GPL-3.0+
Group: Graphical desktop/Other
URL: http://www.altlinux.org/altcenter

Source0: %name-%version.tar

%if "%altbranch" == "p11"
BuildArch: noarch
%else
ExcludeArch: ppc64le armh
%endif

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip mainwindow my_utils my_utils_pyqt5

%description
This is the grapical plugin-based application for show information and
configure system.

Available plugins:
- about
- license
- documentation
- hardware
- settings
- useful

%prep
%setup

%install
%makeinstall_std

%files
%doc README.md TODO.md
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Fri Apr 18 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.7
- hardware: added the ability to hardware probe.
- about: showed URL specified for product and product logo specified in
  /etc/os-release
- Used logo from icon theme.

* Fri Feb 07 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.6
- about: added info about DE + redesigned plugin.
- settings: fix DE like Alt-GNOME:GNOME (ALT #52873).

* Tue Jan 28 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.5
- Open the desired plugin via command line parameter.
- Remove unused code.

* Fri Jan 24 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.4
- Used correct user settings program for current DE (ALT #52797).
- Unset minimal size for mobile device (ALT #52798).

* Thu Jan 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.3
- about: fixed using float for setPointSize.

* Thu Jan 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.2
- Made unify spec for sisyphus and p11.
- Put application to autostart.

* Wed Jan 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1
- Initail build for Sisyphus.
