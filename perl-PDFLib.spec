#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	PDFLib
Summary:	PDFLib Perl module - simpler and more OO interface to pdflib
Summary(pl):	Modu³ Perla PDFLib - prostszy i bardziej obiektowy interfejs do pdflib-a
Name:		perl-PDFLib
Version:	0.12
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/M/MS/MSERGEANT/%{pnam}-%{version}.tar.gz
# Source0-md5:	49ba9d136cc83210d37e7f4763b064cc
BuildRequires:	pdflib-perl >= 4.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
pdflib-a, dostêpnego na http://www.pdflib.com/. Modu³ ten czyni
tworzenie PDF-ów z Perla szybkim, ³atwnym i bezpiecznym. Aktualnie
obs³uguje tekst, obrazki, grafikê i odczytywanie/ustawianie wszystkich
parametrów. Ma wbudowan± obs³ugê kilku rozmiarów papieru. Modu³ dba
o rozpoczynanie/koñczenie stron, próbuje te¿ zapewniæ, aby zawsze
by³ tworzony poprawny PDF.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PDFLib.pm
%{_mandir}/man3/*
