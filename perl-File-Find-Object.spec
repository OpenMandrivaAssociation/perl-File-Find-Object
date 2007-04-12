%define module File-Find-Object
%define name perl-%{module}
%define version 0.0.7
%define release %mkrel 1

Summary: 	File::Find like object
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/N/NA/NANARDON/File-Find-Object/%{module}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{module}
%if %mdkversion < 200600
BuildRequires: perl-devel
%endif
BuildRequires: perl(Class::Accessor)
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
BuildArch: noarch

%description
File::Find::Object does same job of File::Find but trough an object and
using an iterator. It allow to perform multiple tree parsing in same
application.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/*


