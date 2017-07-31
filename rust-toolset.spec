%global scl_name_base rust-toolset
%global scl_name_version 7

%global scl %{scl_name_base}-%{scl_name_version}

%global scl_llvm llvm-toolset-7

%scl_package %scl

Summary:        Package that installs %scl
Name:           %scl_name
Version:        1.17.0
Release:        1%{?dist}
License:        ASL 2.0 or MIT

Requires:       %{scl_prefix}rust = 1.17.0
Requires:       %{scl_prefix}cargo = 0.18.0

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
* Thu Jun 01 2017 Josh Stone <jistone@redhat.com> - 1.17.0-1
- Update to the new SCL name.
- Require exact rust and cargo versions.
