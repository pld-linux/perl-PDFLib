#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pnam	PDFLib
Summary:	PDFLib Perl module - simpler and more OO interface to pdflib
Summary(pl.UTF-8):	Moduł Perla PDFLib - prostszy i bardziej obiektowy interfejs do pdflib-a
Name:		perl-PDFLib
Version:	0.14
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSERGEANT/%{pnam}-%{version}.tar.gz
# Source0-md5:	e22be28ee9a06c790484fdadf0558c82
Patch0:		%{name}-pdflib4.patch
URL:		http://search.cpan.org/dist/-PDFLib/
BuildRequires:	pdflib-perl >= 4.0.3-11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	pdflib-perl >= 4.0.3-11
#Suggests:	pdflib-perl >= 5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDFLib is a simpler, more OO interface to pdflib, available from
http://www.pdflib.com/. It makes creating PDFs from Perl fast, easy
and safe. Currently it supports text, images, graphics, and
getting/setting all parameters. It has builting support for several
paper sizes. It also takes care of starting/ending new pages, to try
and make sure that a valid PDF file is always created.

%description -l pl.UTF-8
PDFLib to prostszy, bardziej obiektowo zorientowany interfejs do
pdflib-a, dostępnego na http://www.pdflib.com/. Moduł ten czyni
tworzenie PDF-ów z Perla szybkim, łatwnym i bezpiecznym. Aktualnie
obsługuje tekst, obrazki, grafikę i odczytywanie/ustawianie wszystkich
parametrów. Ma wbudowaną obsługę kilku rozmiarów papieru. Moduł dba o
rozpoczynanie/kończenie stron, próbuje też zapewnić, aby zawsze był
tworzony poprawny PDF.

%prep
%setup -q -n %{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PDFLib.pm
%{_mandir}/man3/*
