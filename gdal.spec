#
# TODO:
# separate -devel, python- etc.
# more formats (CFITSIO, OGDI, GRASS)
# link dynamically where possible
%include	/usr/lib/rpm/macros.python
Summary:	Geospatial Data Abstraction Library
Summary(pl):	Biblioteka abstrakcji danych dotycz±cych powierzchni Ziemi
Name:		gdal
Version:	1.1.7
Release:	0.1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/gdal/%{name}-%{version}.tar.gz
Patch0:		%{name}-jpeg.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-pgsql.patch
Patch3:		%{name}-DESTDIR.patch
URL:		http://www.remotesensing.org/gdal/
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
#BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	libungif-devel
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GDAL is a translator library for raster geospatial data formats that
is released under an Open Source license. As a library, it presents a
single abstract data model to the calling application for all
supported formats. The related OGR library (which lives within the
GDAL source tree) provides a similar capability for simple features
vector data.
	    
%description -l pl
GDAL to biblioteka konwertuj±ca miêdzy formatami rastrowych danych
dotycz±cych powierzchni Ziemi, udostêpniona na licencji Open Source.
Jako biblioteka udostêpnia aplikacjom jeden abstrakcyjny model danych
do wszystkich obs³ugiwanych formatów. Powi±zana z nia biblioteka OGR
(której ¼ród³a s± do³±czone do drzewa ¼róde³ GDAL) daje podobne
mo¿liwo¶ci dla danych wektorowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS html/*.{html,gif,css}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.a
%{_includedir}/*.h
%attr(755,root,root) %{py_sitedir}/_gdalmodule.so
%{py_sitedir}/*.py
%{_datadir}/gdal
