#
# TODO:
# - consider using GRASS (or GDAL in GRASS? build trap possible)
#
%include	/usr/lib/rpm/macros.python
Summary:	Geospatial Data Abstraction Library
Summary(pl):	Biblioteka abstrakcji danych dotycz±cych powierzchni Ziemi
Name:		gdal
Version:	1.1.8
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/gdal/%{name}-%{version}.tar.gz
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-pgsql.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-soname.patch
Patch4:		%{name}-xerces.patch
URL:		http://www.remotesensing.org/gdal/
BuildRequires:	autoconf
BuildRequires:	cfitsio-devel
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	jasper-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	libungif-devel >= 4.0
BuildRequires:	ogdi-devel >= 3.1
BuildRequires:	postgresql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	xerces-c-devel >= 2.2.0
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

%package devel
Summary:	GDAL library header files
Summary(pl):	Pliki nag³ówkowe biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
GDAL library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki GDAL.

%package static
Summary:	GDAL static libraries
Summary(pl):	Statyczne biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GDAL static libraries.

%description static -l pl
Statyczne biblioteki GDAL.

%package -n python-gdal
Summary:	GDAL Python module
Summary(pl):	Modu³ Pythona GDAL
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description -n python-gdal
GDAL Python module.

%description -n python-gdal -l pl
Modu³ Pythona GDAL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__autoconf}
%configure \
	--with-xerces \
	--with-xerces-inc=/usr/include/xercesc \
	--with-xerces-lib="-lxerces-c" \
	--without-grass

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS html/*.{html,gif,png,css}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgdal.*.so
%{_datadir}/gdal

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdal.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files -n python-gdal
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_gdalmodule.so
%{py_sitedir}/*.py
