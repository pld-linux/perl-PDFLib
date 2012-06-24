#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pnam	PDFLib
Summary:	PDFLib Perl module - simpler and more OO interface to pdflib
Summary(pl):	Modu� Perla PDFLib - prostszy i bardziej obiektowy interfejs do pdflib-a
Name:		perl-PDFLib
Version:	0.12
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/M/MS/MSERGEANT/%{pnam}-%{version}.tar.gz
BuildRequires:	pdflib-perl >= 4.0
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDFLib is a simpler, more OO interface to pdflib, available from
http://www.pdflib.com/. It makes creating PDFs from Perl fast, easy
and safe. Currently it supports text, images, graphics, and
getting/setting all parameters. It has builting support for several
paper sizes. It also takes care of starting/ending new pages, to try
and make sure that a valid PDF file is always created.

%description -l pl
PDFLib to prostszy, bardziej obiektowo zorientowany interfejs do
pdflib-a, dost�pnego na http://www.pdflib.com/. Modu� ten czyni
tworzenie PDF-�w z Perla szybkim, �atwnym i bezpiecznym. Aktualnie
obs�uguje tekst, obrazki, grafik� i odczytywanie/ustawianie wszystkich
parametr�w. Ma wbudowan� obs�ug� kilku rozmiar�w papieru. Modu� dba
o rozpoczynanie/ko�czenie stron, pr�buje te� zapewni�, aby zawsze
by� tworzony poprawny PDF.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/PDFLib.pm
%{_mandir}/man3/*
