%define upstream_name    File-Find-Object
%define upstream_version v0.2.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	File::Find like object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildArch:	noarch

%description
File::Find::Object does same job of File::Find but trough an object and
using an iterator. It allow to perform multiple tree parsing in same
application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.2.3-3mdv2011.0
+ Revision: 654960
- rebuild for updated spec-helper

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.3-2mdv2011.0
+ Revision: 410620
- update to 0.2.3

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.2-2mdv2010.0
+ Revision: 407691
- force rebuild
- rebuild using %%perl_convert_version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1mdv2010.0
+ Revision: 389774
- update to new version 0.2.2

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2010.0
+ Revision: 387755
- update to new version 0.2.1

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 343946
- update to new version 0.2.0

* Wed Feb 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.9-1mdv2009.1
+ Revision: 339342
- update to new version 0.1.9

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.8-1mdv2009.1
+ Revision: 331584
- update to new version 0.1.8

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.7-1mdv2009.1
+ Revision: 330183
- update to new version 0.1.7

* Mon Jan 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.6-1mdv2009.1
+ Revision: 328528
- update to new version 0.1.6

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 324503
- update to new version 0.1.5

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.4-1mdv2009.1
+ Revision: 320430
- update to new version 0.1.4

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2009.1
+ Revision: 302817
- update to new version 0.1.3

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2009.1
+ Revision: 297540
- update to new version 0.1.2

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2009.1
+ Revision: 296796
- update to new version 0.1.1

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-3mdv2009.0
+ Revision: 256917
- rebuild

* Thu Mar 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.1
+ Revision: 180622
- update to new version 0.1.0

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.9-1mdv2008.1
+ Revision: 174715
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.0.8-1mdv2008.0
+ Revision: 59248
- 0.0.8


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.0.7-1mdv2007.0
+ Revision: 132939
- 0.0.7

* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.0.6-1mdv2007.1
+ Revision: 95138
- 0.0.6

* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 0.0.5-1mdv2007.1
+ Revision: 85427
- Buildrequires
- 0.0.5
- 0.0.4

* Sun Jul 16 2006 Olivier Thauvin <nanardon@mandriva.org> 0.0.3-1mdv2007.0
+ Revision: 41266
- 0.0.3
- import perl-File-Find-Object

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 0.0.2-1mdk
- 0.0.2

* Thu Jun 23 2005 Olivier Thauvin <nanardon@mandriva.org> 0.0.1-1mdk
- first mdk release

