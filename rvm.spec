%define name rvm
%define version 1.16
%define release %mkrel 2

%define major 1

%define libname %mklibname %name %major
%define develname %mklibname %name -d

Summary: RVM library
Name: %name
Version: %version
Release: %release
Group: Development/Other
License: LGPL
Url: http://www.coda.cs.cmu.edu/doc/html/index.html
Source: ftp://ftp.wu-wien.ac.at/pub/systems/coda/src/%name-%{version}.tar.gz
BuildRequires:	liblwp-devel
BuildRequires:	chrpath
Buildroot: %_tmppath/%name-%{version}

%description
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed filesystem.

%package -n %libname
Summary: RVM tools
Group: Development/Other

%description -n %libname
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed filesystem.

%package -n %develname
Summary: RVM library development files
Group: Development/Other
Requires: %libname = %version-%release
Provides: rvm-devel = %version-%release
Obsoletes:  %mklibname %name -d 1

%description -n %develname
Headers and static libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%package tools
Summary: RVM tools
Group: Development/Other

%description tools
Userspace tools to initialize and manipulate RVM log and data segments.
The RVM library is used by the Coda distributed filesystem.

%prep
%setup -q

%build
autoreconf -fi
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
chrpath --delete %{buildroot}%{_libdir}/*.so.*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %libname
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %libname
%endif

%files -n %libname
%defattr(-,root,root)
%doc COPYING NEWS INSTALL
%{_libdir}/librvmlwp.so.*
%{_libdir}/librdslwp.so.*
%{_libdir}/libseglwp.so.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/librvmlwp.la
%{_libdir}/librvmlwp.a
%{_libdir}/librvmlwp.so
%{_libdir}/librdslwp.la
%{_libdir}/librdslwp.a
%{_libdir}/librdslwp.so
%{_libdir}/libseglwp.la
%{_libdir}/libseglwp.a
%{_libdir}/libseglwp.so
%{_includedir}/rvm
%{_libdir}/pkgconfig/rvmlwp.pc

%files tools
%defattr(-,root,root)
%{_sbindir}/rvmutl
%{_sbindir}/rdsinit

