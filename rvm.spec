%define name rvm
%define version 1.12
%define release %mkrel 1

%define major 1

%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Summary: RVM library
Name: %name
Version: %version
Release: %release
Source: %name-%{version}.tar.bz2
Url: http://www.coda.cs.cmu.edu/doc/html/index.html
License: LGPL
Buildroot: %_tmppath/%name-buildroot
BuildRequires:	liblwp-devel
Group: Development/Other

%description
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed filesystem.

%package -n %libname
Summary: RVM tools
Group: Development/Other
Provides: %libname = %version-%release

%description -n %libname
The RVM persistent recoverable memory library. The RVM library is used by
the Coda distributed filesystem.

%package -n %libnamedev
Summary: RVM library development files
Group: Development/Other
Requires: %libname = %version
Provides: librvm-devel = %version-%release

%description -n %libnamedev
Headers and static libraries for developing programs using the RVM library.
The RVM library is used by the Coda distributed filesystem.

%package tools
Summary: RVM tools
Group: Development/Other

%description tools
Userspace tools to initialize and manipulate RVM log and data segments.
The RVM library is used by the Coda distributed filesystem.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure

%make

%install
%makeinstall
chmod 755 $RPM_BUILD_ROOT%{_libdir}/librvm.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/librvmlwp.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libseg.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/librds.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/librdslwp.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %libname

%postun -p /sbin/ldconfig -n %libname

%files -n %libname
%defattr(-,root,root)
%doc COPYING NEWS INSTALL
%{_libdir}/librvm.so.*
%{_libdir}/librvmlwp.so.*
%{_libdir}/libseg.so.*
%{_libdir}/librds.so.*
%{_libdir}/librdslwp.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/librvm.la
%{_libdir}/librvm.a
%{_libdir}/librvm.so
%{_libdir}/librvmlwp.la
%{_libdir}/librvmlwp.a
%{_libdir}/librvmlwp.so
%{_libdir}/libseg.la
%{_libdir}/libseg.a
%{_libdir}/libseg.so
%{_libdir}/librds.la
%{_libdir}/librds.a
%{_libdir}/librds.so
%{_libdir}/librdslwp.la
%{_libdir}/librdslwp.a
%{_libdir}/librdslwp.so
%dir %{_includedir}/rvm
%{_includedir}/rvm/rvm.h
%{_includedir}/rvm/rvm_statistics.h
%{_includedir}/rvm/rvm_segment.h
%{_includedir}/rvm/rds.h

%files tools
%defattr(-,root,root)
%{_sbindir}/rvmutl
%{_sbindir}/rdsinit

