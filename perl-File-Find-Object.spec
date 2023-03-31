%define upstream_name    File-Find-Object
%define upstream_version v0.3.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.3.2
Release:	3

Summary:	File::Find like object

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/File::Find::Object
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
# For "make test"
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
File::Find::Object does same job of File::Find but trough an object and
using an iterator. It allow to perform multiple tree parsing in same
application.

%prep
%autosetup -p1 -n %{upstream_name}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc %{_mandir}/*/*
%{perl_vendorlib}/*



