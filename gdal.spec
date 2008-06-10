# TODO: fix LDFLAGS passing (to use as-needed)
#
# Conditional build:
%bcond_without	odbc	# disable odbc support
%bcond_without	xerces	# disable xerces support
%bcond_without	ruby	# disable ruby support
#
Summary:	Geospatial Data Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji danych dotyczących powierzchni Ziemi
Name:		gdal
Version:	1.4.3
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	d2b0d428edab7895aa53c7d827094a09
Patch0:		%{name}-dods.patch
Patch1:		%{name}-perl.patch
Patch2:		%{name}-ruby.patch
URL:		http://www.gdal.org/
BuildRequires:	autoconf
BuildRequires:	cfitsio-devel
BuildRequires:	doxygen
BuildRequires:	geos-devel >= 2.0
BuildRequires:	giflib-devel >= 4.0
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	jasper-devel
BuildRequires:	libcsf-devel
BuildRequires:	libdap-devel >= 3.5
BuildRequires:	libgeotiff-devel >= 1.2.1
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	netcdf-devel
BuildRequires:	ogdi-devel >= 3.1
BuildRequires:	perl-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-devel >= 1:1.0.0
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	swig-python >= 1.3
%{?with_ruby:BuildRequires:	swig-ruby}
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xerces:BuildRequires:	xerces-c-devel >= 2.2.0}
BuildRequires:	zlib-devel >= 1.1.4
Requires:	geos >= 2.0
Requires:	libgeotiff >= 1.2.1
Requires:	libpng >= 2:1.2.8
Requires:	libtiff >= 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GDAL is a translator library for raster geospatial data formats that
is released under an Open Source license. As a library, it presents a
single abstract data model to the calling application for all
supported formats. The related OGR library (which lives within the
GDAL source tree) provides a similar capability for simple features
vector data.

%description -l pl.UTF-8
GDAL to biblioteka konwertująca między formatami rastrowych danych
dotyczących powierzchni Ziemi, udostępniona na licencji Open Source.
Jako biblioteka udostępnia aplikacjom jeden abstrakcyjny model danych
do wszystkich obsługiwanych formatów. Powiązana z nią biblioteka OGR
(której źródła są dołączone do drzewa źródeł GDAL) daje podobne
możliwości dla danych wektorowych.

%package devel
Summary:	GDAL library header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cfitsio-devel
Requires:	geos-devel >= 2.0
Requires:	giflib-devel
Requires:	hdf-devel >= 4.0
Requires:	jasper-devel
Requires:	libcsf-devel
Requires:	libdap-devel >= 3.5
Requires:	libgeotiff-devel >= 1.2.1
Requires:	libjpeg-devel
Requires:	libpng-devel >= 2:1.2.8
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 3.6.0
Requires:	netcdf-devel
Requires:	ogdi-devel >= 3.1
Requires:	postgresql-devel
Requires:	sqlite3-devel >= 3
%{?with_odbc:Requires:	unixODBC-devel}
%{?with_xerces:Requires:	xerces-c-devel >= 2.2.0}

%description devel
GDAL library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GDAL.

%package static
Summary:	GDAL static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GDAL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GDAL static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GDAL.

%package -n perl-gdal
Summary:	Perl bindings for GDAL
Summary(pl.UTF-8):	Wiązania Perla do pakietu GDAL
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-gdal
Perl bindings for GDAL - Geo::GDAL, Geo::OGR and Geo::OSR modules.

%description -n perl-gdal -l pl.UTF-8
Wiązania Perla do pakietu GDAL - moduły Geo::GDAL, Geo::OGR, Geo::OSR.

%package -n python-gdal
Summary:	GDAL Python module
Summary(pl.UTF-8):	Moduł Pythona GDAL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-gdal
GDAL Python module.

%description -n python-gdal -l pl.UTF-8
Moduł Pythona GDAL.

%package -n ruby-gdal
Summary:	Ruby bindings for GDAL
Summary(pl.UTF-8):	Wiązania języka Ruby do pakietu GDAL
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description -n ruby-gdal
Ruby bindings for GDAL - gdal, gdalconst, ogr and osr modules.

%description -n ruby-gdal -l pl.UTF-8
Wiązania języka Ruby do pakietu GDAL - moduły gdal, gdalconst, ogr i
osr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# $PYTHON_INCLUDES is set only with --with-python, but we have --with-ngpython,
# and $PYTHON_INCLUDES is needed to detect numpy properly
export PYTHON_INCLUDES=-I%{py_incdir}

# disable grass/libgrass here, it can be built from separate gdal-grass package
%{__autoconf}
%configure \
	--datadir=%{_datadir}/gdal \
	--with-dods-root=/usr \
	--with-perl \
	--with-pymoddir=%{py_sitedir} \
	%{?with_ruby:--with-ruby} \
	--with-sqlite \
	%{?with_xerces:--with-xerces} \
	--with-xerces-inc=/usr/include/xercesc \
	--with-xerces-lib="-lxerces-c" \
	--without-grass \
	--without-libgrass \
	--with-ngpython
# ngpython seems to be compatibile with old python bindings
# --with-php needs Zend API update
%{__make}

%{__make} -C swig build \
	OPTIMIZE="%{rpmcflags}"

%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf _html
cp -a html _html
cp -a ogr/html _html/ogr

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/GDAL/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/GDAL/Const/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/OGR/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/OSR/.packlist

# some doxygen trash
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Geo/GDAL.dox
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Geo/GDAL/Const.dox
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Geo/OGR.dox
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Geo/OSR.dox

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS PROVENANCE.TXT
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdal.so.1
%{_datadir}/gdal
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gdal-config.1*

%files devel
%defattr(644,root,root,755)
%doc _html/*
%attr(755,root,root) %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so
%{_libdir}/libgdal.la
%{_includedir}/*.h
%{_mandir}/man1/gdal-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdal.a

%files -n perl-gdal
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Geo
%{perl_vendorarch}/Geo/GDAL.pm
%dir %{perl_vendorarch}/Geo/GDAL
%{perl_vendorarch}/Geo/GDAL/Const.pm
%{perl_vendorarch}/Geo/OGR.pm
%{perl_vendorarch}/Geo/OSR.pm
%dir %{perl_vendorarch}/auto/Geo
%dir %{perl_vendorarch}/auto/Geo/GDAL
%{perl_vendorarch}/auto/Geo/GDAL/GDAL.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/GDAL.so
%dir %{perl_vendorarch}/auto/Geo/GDAL/Const
%{perl_vendorarch}/auto/Geo/GDAL/Const/Const.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/Const/Const.so
%dir %{perl_vendorarch}/auto/Geo/OGR
%{perl_vendorarch}/auto/Geo/OGR/OGR.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OGR/OGR.so
%dir %{perl_vendorarch}/auto/Geo/OSR
%{perl_vendorarch}/auto/Geo/OSR/OSR.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OSR/OSR.so

%files -n python-gdal
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_gdal.so
%attr(755,root,root) %{py_sitedir}/_gdalconst.so
%attr(755,root,root) %{py_sitedir}/_gdal_array.so
%attr(755,root,root) %{py_sitedir}/_ogr.so
%attr(755,root,root) %{py_sitedir}/_osr.so
%{py_sitedir}/gdal.py[co]
%{py_sitedir}/gdalconst.py[co]
%{py_sitedir}/gdalnumeric.py[co]
%{py_sitedir}/gdal_array.py[co]
%{py_sitedir}/ogr.py[co]
%{py_sitedir}/osr.py[co]
%{py_sitedir}/Gdal_Wrapper-*.egg-info

%if %{with ruby}
%files -n ruby-gdal
%defattr(644,root,root,755)
%dir %{ruby_sitearchdir}/gdal
%attr(755,root,root) %{ruby_sitearchdir}/gdal/gdal.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/gdalconst.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/ogr.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/osr.so
%endif