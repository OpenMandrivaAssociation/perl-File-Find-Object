%define upstream_name    File-Find-Object
%define upstream_version v0.2.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary: 	File::Find like object
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
File::Find::Object does same job of File::Find but trough an object and
using an iterator. It allow to perform multiple tree parsing in same
application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
