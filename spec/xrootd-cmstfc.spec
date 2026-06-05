
Name: xrootd-cmstfc
Version: 1.5.2
Release: 3%{?dist}
Summary: CMS TFC plugin for xrootd

Group: System Environment/Daemons
License: BSD
URL: https://github.com/bbockelm/xrootd-cmstfc
# Generated from:
# git-archive master | gzip -7 > ~/rpmbuild/SOURCES/xrootd-lcmaps.tar.gz
Source0: %{name}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: xrootd-libs-devel xerces-c-devel pcre-devel
BuildRequires: cmake
Requires: /usr/bin/xrootd pcre xerces-c

%package devel
Summary: Development headers and libraries for Xrootd CMSTFC plugin
Group: System Environment/Development

%description
%{summary}

%description devel
%{summary}

%prep
%autosetup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%{_libdir}/libXrdCmsTfc.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/XrdCmsTfc.hh

%changelog
* Fri Jun 05 2026 Luke Kreczko <kreczko@cern.ch> - 1.5.2-3
- cleanup spec for EL9
* Thu Nov 29 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 1.5.1-3
- Move module back into base RPM.

* Mon Nov 12 2012 Brian Bockelman - 1.5.1-1
- Fix SL6 compilation issues.

* Mon Oct 22 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 1.5-1
- Switch to cmake.
- Rebuild against Xrootd 3.3.

* Wed May 18 2011 Brian Bockelman <bbockelm@cse.unl.edu> 1.4.3-1
- Apply path matching only at the beginning of the path.

* Mon Mar 28 2011 Brian Bockelman <bbockelm@cse.unl.edu> 1.4.2-2
- Rebuild to reflect the updated RPM names.

* Wed Sep 29 2010 Brian Bockelman <bbockelm@cse.unl.edu> 1.4.2-1
- Reduce verbosity of the logging.
- Fix for TFC parsing to better respect rule order; request from Florida.

* Tue Aug 24 2010 Brian Bockelman <bbockelm@cse.unl.edu> 1.4.0-1
- Break xrootd-cmstfc off into its own standalone RPM.
