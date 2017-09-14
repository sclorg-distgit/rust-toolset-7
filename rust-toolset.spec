%global scl_name_base rust-toolset
%global scl_name_version 7

%global scl %{scl_name_base}-%{scl_name_version}

%global scl_llvm llvm-toolset-7

%scl_package %scl

%global dockerfiledir %{_datadir}/%{scl_prefix}dockerfiles

Summary:        Package that installs %scl
Name:           %scl_name
Version:        1.19.0
Release:        3%{?dist}
License:        ASL 2.0 or MIT

# How to generate dockerfile tarball:
# rhpkg clone rust-toolset-7-docker
# cd rust-toolset-7-docker
# git archive --prefix=rust-toolset-7-docker/ -o rust-toolset-7-docker-`git rev-parse --short HEAD`.tar.gz HEAD
Source0: %{scl_prefix}docker-b47082d.tar.gz

Requires:       %{scl_prefix}rust = 1.19.0
Requires:       %{scl_prefix}cargo = 0.20.0

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

%package dockerfiles
Summary: Package shipping Dockerfiles for rust-toolset

%description dockerfiles
This package provides a set of example Dockerfiles that can be used
with rust-toolset.

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%prep
%setup -c -T -a 0

%install
%scl_install

install -d %{buildroot}%{dockerfiledir}
install -d -p -m 755 %{buildroot}%{dockerfiledir}/rhel7
install -d -p -m 755 %{buildroot}%{dockerfiledir}/rhel7/%{scl_prefix}docker
cp -a %{scl_prefix}docker %{buildroot}%{dockerfiledir}/rhel7

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

%files dockerfiles
%{dockerfiledir}

%changelog
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
