%define module File-Find-Object
%define name perl-%{module}
%define version 0.2.0
%define release %mkrel 1

Summary: 	File::Find like object
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::XSAccessor)
BuildArch: noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/*


