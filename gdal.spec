#
# TODO:
# - consider using GRASS (or GDAL in GRASS? build trap possible)
#
Summary:	Geospatial Data Abstraction Library
Summary(pl):	Biblioteka abstrakcji danych dotycz±cych powierzchni Ziemi
Name:		gdal
Version:	1.2.3
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	6fe5b737e3ab323a34dea7578cc7fc9b
Patch0:		%{name}-pgsql.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www.remotesensing.org/gdal/
BuildRequires:	autoconf
BuildRequires:	cfitsio-devel
BuildRequires:	doxygen
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	jasper-devel
BuildRequires:	libgeotiff-devel >= 1.2.1
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	libungif-devel >= 4.0
BuildRequires:	netcdf-devel
BuildRequires:	ogdi-devel >= 3.1
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	unixODBC-devel
BuildRequires:	xerces-c-devel >= 2.2.0
BuildRequires:	zlib-devel >= 1.1.4
Requires:	libgeotiff >= 1.2.1
Requires:	libtiff >= 3.6.0
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
do wszystkich obs³ugiwanych formatów. Powi±zana z ni± biblioteka OGR
(której ¼ród³a s± do³±czone do drzewa ¼róde³ GDAL) daje podobne
mo¿liwo¶ci dla danych wektorowych.

%package devel
Summary:	GDAL library header files
Summary(pl):	Pliki nag³ówkowe biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cfitsio-devel
Requires:	hdf-devel >= 4.0
Requires:	jasper-devel
Requires:	libgeotiff-devel >= 1.2.1
Requires:	libjpeg-devel
Requires:	libpng-devel >= 1.0.6
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 3.6.0
Requires:	libungif-devel
Requires:	netcdf-devel
Requires:	ogdi-devel >= 3.1
Requires:	postgresql-devel
Requires:	unixODBC-devel
Requires:	xerces-c-devel >= 2.2.0

%description devel
GDAL library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki GDAL.

%package static
Summary:	GDAL static libraries
Summary(pl):	Statyczne biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GDAL static libraries.

%description static -l pl
Statyczne biblioteki GDAL.

%package -n python-gdal
Summary:	GDAL Python module
Summary(pl):	Modu³ Pythona GDAL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-gdal
GDAL Python module.

%description -n python-gdal -l pl
Modu³ Pythona GDAL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__perl} -pi -e "s@lib/python@%{_lib}/python@" aclocal.m4

%build
%{__autoconf}
%configure \
	--datadir=%{_datadir}/gdal \
	--with-pymoddir=%{py_sitedir} \
	--with-xerces \
	--with-xerces-inc=/usr/include/xercesc \
	--with-xerces-lib="-lxerces-c" \
	--without-grass \
	--without-geos

%{__make}

%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f ogr/html html/org

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so.*.*.*
%{_datadir}/gdal
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gdal-config.1*

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so
%{_libdir}/libgdal.la
%{_includedir}/*.h
%{_mandir}/man1/gdal-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files -n python-gdal
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_gdalmodule.so
%{py_sitedir}/*.py
