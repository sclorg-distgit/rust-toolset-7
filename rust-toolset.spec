%global scl_name_base rust-toolset
%global scl_name_version 7

%global scl %{scl_name_base}-%{scl_name_version}

%global scl_llvm llvm-toolset-7

%scl_package %scl

Summary:        Package that installs %scl
Name:           %scl_name
Version:        1.22.1
Release:        1%{?dist}
License:        ASL 2.0 or MIT

Requires:       %{scl_prefix}rust = 1.22.1
Requires:       %{scl_prefix}cargo = 0.23.0

BuildRequires:  scl-utils-build

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils
Requires: %{scl_llvm}-runtime

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%prep
%setup -c -T

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH="%{_bindir}\${PATH:+:\${PATH}}"
export LD_LIBRARY_PATH="%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}"
export MANPATH="%{_mandir}:\${MANPATH:-}"

source scl_source enable %{scl_llvm}
EOF

%files

%files runtime
%scl_files

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%changelog
* Wed Dec 13 2017 Josh Stone <jistone@redhat.com> - 1.22.1-1
- Update to rust-1.22.1 and cargo-0.23.0
- (rhbz 1521195) remove dockerfiles

* Wed Oct 04 2017 Josh Stone <jistone@redhat.com> - 1.20.0-4
- Update dockerfiles

* Tue Sep 19 2017 Josh Stone <jistone@redhat.com> - 1.20.0-3
- Update dockerfiles

* Mon Sep 11 2017 Josh Stone <jistone@redhat.com> - 1.20.0-2
- Update to cargo-0.21.1

* Wed Sep 06 2017 Josh Stone <jistone@redhat.com> - 1.20.0-1
- Update to rust-1.20.0 and cargo-0.21.0

* Wed Aug 09 2017 Tom Stellard <tstellar@redhat.com> - 1.19.0-3
- Add dockerfiles

* Wed Aug 09 2017 Tom Stellard <tstellar@redhat.com> - 1.19.0-2
- Add stub dockerfiles sub-package

* Mon Jul 24 2017 Josh Stone <jistone@redhat.com> - 1.19.0-1
- Update to rust-1.19.0 and cargo-0.20.0

* Thu Jun 15 2017 Josh Stone <jistone@redhat.com> - 1.18.0-2
- Update to cargo-0.19.0

* Thu Jun 15 2017 Josh Stone <jistone@redhat.com> - 1.18.0-1
- Update to rust-1.18.0

* Thu Jun 01 2017 Josh Stone <jistone@redhat.com> - 1.17.0-1
- Update to the new SCL name.
- Require exact rust and cargo versions.
