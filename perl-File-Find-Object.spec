%define upstream_name    File-Find-Object
%define upstream_version v0.2.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.2.8
Release:	1

Summary:	File::Find like object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-Find-Object-v0.2.8.tar.gz

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

