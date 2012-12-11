%define name rvm
%define version 1.16
%define release %mkrel 3

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
%makeinstall
chrpath --delete %{buildroot}%{_libdir}/*.so.*

%files -n %libname
%doc COPYING NEWS INSTALL
%{_libdir}/librvmlwp.so.*
%{_libdir}/librdslwp.so.*
%{_libdir}/libseglwp.so.*

%files -n %develname
%{_libdir}/librvmlwp.a
%{_libdir}/librvmlwp.so
%{_libdir}/librdslwp.a
%{_libdir}/librdslwp.so
%{_libdir}/libseglwp.a
%{_libdir}/libseglwp.so
%{_includedir}/rvm
%{_libdir}/pkgconfig/rvmlwp.pc

%files tools
%{_sbindir}/rvmutl
%{_sbindir}/rdsinit



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-3mdv2011.0
+ Revision: 614799
- the mass rebuild of 2010.1 packages

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.16-2mdv2010.0
+ Revision: 442812
- rebuild

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.1
+ Revision: 349435
- new version

  + Jérôme Soyer <saispo@mandriva.org>
    - New upstream release

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.12-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import rvm


* Tue Aug  8 2006 Antoine Ginies <aginies@mandriva.com> 1.12-1mdv2007.0
- release 1.12
- use mkrel

* Thu Feb 16 2006 Antoine Ginies <aginies@mandriva.com> 1.11-1mdk
- 1.11

* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.10-1mdk
- 1.10

* Wed Jan 14 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.8-1mdk
- 1.8
- use mklibname

* Sat Dec 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.7-1mdk
- 1.7
- Fix Requires/Provides

* Thu Mar 21 2002 Florin <florin@mandrakesoft.com> 1.6-4mdk
- rebuild
- add the url tag

* Sat Nov  3 2001 Stefan van der Eijk <stefan@eijk.nu> 1.6-3mdk
- BuildRequires: liblwp-devel

* Fri Aug 24 2001 Florin Grad <florin@mandrakesoft.com> 1.6-2mdk
- remove the require on rvm to rvm-tools

* Thu Aug 23 2001 Florin Grad <florin@mandrakesoft.com> 1.6-1mdk
- 1.6
- add the doc section

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2-2mdk
- clean spec
- macros

* Thu Nov 16 2000 Florin Grad <florin@mandrakesoft.com> 1.2-1mdk
- 1.2.1
* Thu Aug 31 2000 Florin Grad <florin@mandrakesoft.com> 1.1-2mdk
- adding the macros
* Fri Jul 7 2000 Florin Grad <florin@mandrakesoft.com> 1.1-1mdk
- First attempt.
