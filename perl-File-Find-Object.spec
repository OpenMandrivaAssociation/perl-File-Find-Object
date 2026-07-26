%define upstream_name    File-Find-Object
Name:		perl-%{upstream_name}
Version:	0.3.9
Release:	2

Summary:	File::Find like object

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/shlomif/perl-file-find-object
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-%{version}.tar.gz

BuildRequires:	make
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



