#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Games
%define		pnam	Console
Summary:	Games::Console - a 2D quake style in-game console
Summary(pl.UTF-8):	Games::Console - dwuwymiarowa konsola dla gier podobna do tej z quake'a
Name:		perl-Games-Console
Version:	0.04
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Games/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c494d242db47dca607d676173c7cd4ba
URL:		http://search.cpan.org/dist/Games-Console/
BuildRequires:	perl-Games-OpenGL-Font-2D >= 0.05
BuildRequires:	perl-SDL >= 1.20.3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides you with 2D console, which can accept user input
and display messages from the application. The console works very much
like in the popular ID games.

%description -l pl.UTF-8
Ten pakiet udostępnia dwuwymiarową konsolę przyjmującą wejście od
użytkownika i wyświetlającą komunikaty aplikacji. Konsola działa
bardzo podobnie do tej z popularnych gier ID.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
	CC="%{__cc}" \
#	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README BUGS TODO 
# use macros:
#%%{perl_vendorlib}/...
#%%{perl_vendorarch}/...
%{_mandir}/man3/*
