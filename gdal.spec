# TODO: csharp, java, mysql
#
# Conditional build:
%bcond_without	odbc	# disable odbc support
%bcond_without	xerces	# disable xerces support
%bcond_without	ruby	# disable ruby support
#
Summary:	Geospatial Data Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji danych dotyczących powierzchni Ziemi
Name:		gdal
Version:	1.7.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/gdal/%{name}-%{version}.tar.gz
# Source0-md5:	c4673970bd2285032de9ae9bbd82754a
Patch0:		%{name}-perl.patch
Patch1:		%{name}-ruby.patch
Patch2:		%{name}-asneeded.patch
Patch3:		%{name}-python_install.patch
Patch4:		%{name}-libdap.patch
URL:		http://www.gdal.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cfitsio-devel
BuildRequires:	doxygen
BuildRequires:	expat-devel >= 1.95.0
BuildRequires:	geos-devel >= 2.2
BuildRequires:	giflib-devel >= 4.0
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	hdf5-devel
BuildRequires:	jasper-devel
BuildRequires:	libcsf-devel
BuildRequires:	libdap-devel >= 3.10
BuildRequires:	libgeotiff-devel >= 1.2.1
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	libtool
BuildRequires:	netcdf-devel
BuildRequires:	ogdi-devel >= 3.1
BuildRequires:	pcidsk-devel
BuildRequires:	perl-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	proj-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-devel >= 1:1.0.0
BuildRequires:	rpm-pythonprov
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	swig-perl
BuildRequires:	swig-python >= 1.3
%{?with_ruby:BuildRequires:	swig-ruby}
%if "%{pld_release}" == "ti"
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-dvips
%else
BuildRequires:	texlive-dvips
BuildRequires:	texlive-latex
%endif
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_xerces:BuildRequires:	xerces-c-devel >= 2.2.0}
BuildRequires:	zlib-devel >= 1.1.4
Requires:	geos >= 2.2
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
Requires:	expat-devel >= 1.95.0
Requires:	geos-devel >= 2.2
Requires:	giflib-devel
Requires:	hdf-devel >= 4.0
Requires:	hdf5-devel
Requires:	jasper-devel
Requires:	libcsf-devel
Requires:	libdap-devel >= 3.10
Requires:	libgeotiff-devel >= 1.2.1
Requires:	libjpeg-devel
Requires:	libpng-devel >= 2:1.2.8
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 3.6.0
Requires:	netcdf-devel
Requires:	ogdi-devel >= 3.1
Requires:	pcidsk-devel
Requires:	postgresql-devel
Requires:	sqlite3-devel >= 3
%{?with_odbc:Requires:	unixODBC-devel}
%{?with_xerces:Requires:	xerces-c-devel >= 2.7.0}

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
%patch3 -p1
%patch4 -p1

# need to regenerate (old ones don't support perl 5.10)
%{__rm} swig/perl/{gdal_wrap.cpp,gdalconst_wrap.c,ogr_wrap.cpp,osr_wrap.cpp}
# includes updated for Ruby 1.9
%{__rm} swig/ruby/{gdal_wrap.cpp,gdalconst_wrap.c,ogr_wrap.cpp,osr_wrap.cpp}

%{__rm} -r man

%build
# $PYTHON_INCLUDES is set only with --with-ogpython, but we have --with-python,
# and $PYTHON_INCLUDES is needed to detect numpy properly
export PYTHON_INCLUDES=-I%{py_incdir}

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
# disable grass/libgrass here, it can be built from separate gdal-grass package
%configure \
	--datadir=%{_datadir}/gdal \
	--with-dods-root=/usr \
	--with-hide-internal-symbols \
	--with-pcidsk=/usr \
	--with-perl \
	--with-python \
	%{?with_ruby:--with-ruby} \
	--with-sqlite3 \
	%{?with_xerces:--with-xerces} \
	--with-xerces-inc=/usr/include/xercesc \
	--with-xerces-lib="-lxerces-c" \
	--without-grass \
	--without-libgrass
# --with-php needs Zend API update
# java broken, no configure option
# csharp builds, but has no configure option

# regenerate where needed
%{__make} -j1 -C swig/perl generate
%{?with_ruby:%{__make} -j1 -C swig/ruby generate}

%{__make} -j1

%{__make} -j1 docs

%{__make} -j1 man

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-man \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf _html
cp -a html _html
cp -a ogr/html _html/ogr

install -d $RPM_BUILD_ROOT%{_mandir}/man3
for f in BandProperty ColorAssociation CutlineTransformer DatasetProperty \
	EnhanceCBInfo GDALAspectAlgData GDALColorReliefDataset GDALColorReliefRasterBand \
	GDALGeneric3x3Dataset GDALGeneric3x3RasterBand GDALHillshadeAlgData \
	GDALSlopeAlgData NamedColor ; do
	mv $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1 $RPM_BUILD_ROOT%{_mandir}/man3/${f}.3
done

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

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

%if %{with ruby}
%{__rm} $RPM_BUILD_ROOT%{ruby_sitearchdir}/gdal/*.la
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS PROVENANCE.TXT
%attr(755,root,root) %{_bindir}/epsg_tr.py
%attr(755,root,root) %{_bindir}/esri2wkt.py
%attr(755,root,root) %{_bindir}/gcps2vec.py
%attr(755,root,root) %{_bindir}/gcps2wld.py
%attr(755,root,root) %{_bindir}/gdal2tiles.py
%attr(755,root,root) %{_bindir}/gdal2xyz.py
%attr(755,root,root) %{_bindir}/gdal_contour
%attr(755,root,root) %{_bindir}/gdal_fillnodata.py
%attr(755,root,root) %{_bindir}/gdal_grid
%attr(755,root,root) %{_bindir}/gdal_merge.py
%attr(755,root,root) %{_bindir}/gdal_polygonize.py
%attr(755,root,root) %{_bindir}/gdal_proximity.py
%attr(755,root,root) %{_bindir}/gdal_rasterize
%attr(755,root,root) %{_bindir}/gdal_retile.py
%attr(755,root,root) %{_bindir}/gdal_sieve.py
%attr(755,root,root) %{_bindir}/gdal_translate
%attr(755,root,root) %{_bindir}/gdaladdo
%attr(755,root,root) %{_bindir}/gdalbuildvrt
%attr(755,root,root) %{_bindir}/gdalchksum.py
%attr(755,root,root) %{_bindir}/gdaldem
%attr(755,root,root) %{_bindir}/gdalenhance
%attr(755,root,root) %{_bindir}/gdalident.py
%attr(755,root,root) %{_bindir}/gdalimport.py
%attr(755,root,root) %{_bindir}/gdalinfo
%attr(755,root,root) %{_bindir}/gdalmanage
%attr(755,root,root) %{_bindir}/gdaltindex
%attr(755,root,root) %{_bindir}/gdaltransform
%attr(755,root,root) %{_bindir}/gdalwarp
%attr(755,root,root) %{_bindir}/mkgraticule.py
%attr(755,root,root) %{_bindir}/nearblack
%attr(755,root,root) %{_bindir}/ogr2ogr
%attr(755,root,root) %{_bindir}/ogrinfo
%attr(755,root,root) %{_bindir}/ogrtindex
%attr(755,root,root) %{_bindir}/pct2rgb.py
%attr(755,root,root) %{_bindir}/rgb2pct.py
%attr(755,root,root) %{_bindir}/testepsg
%attr(755,root,root) %{_libdir}/libgdal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdal.so.1
%{_datadir}/gdal
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal_contour.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_grid.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdal_rasterize.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/gdal_translate.1*
%{_mandir}/man1/gdal_utilities.1*
%{_mandir}/man1/gdaladdo.1*
%{_mandir}/man1/gdalbuildvrt.1*
%{_mandir}/man1/gdaldem.1*
%{_mandir}/man1/gdalinfo.1*
%{_mandir}/man1/gdaltindex.1*
%{_mandir}/man1/gdaltransform.1*
%{_mandir}/man1/gdalwarp.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr2ogr.1*
%{_mandir}/man1/ogr_utilities.1*
%{_mandir}/man1/ogrinfo.1*
%{_mandir}/man1/ogrtindex.1*
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*

%files devel
%defattr(644,root,root,755)
%doc _html/*
%attr(755,root,root) %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so
%{_libdir}/libgdal.la
%{_includedir}/cpl_*.h
%{_includedir}/cplkeywordparser.h
%{_includedir}/gdal*.h
%{_includedir}/gvgcpfit.h
%{_includedir}/memdataset.h
%{_includedir}/ogr_*.h
%{_includedir}/ogrsf_frmts.h
%{_includedir}/rawdataset.h
%{_includedir}/thinplatespline.h
%{_includedir}/vrtdataset.h
%{_mandir}/man1/gdal-config.1*
%{_mandir}/man3/BandProperty.3*
%{_mandir}/man3/ColorAssociation.3*
%{_mandir}/man3/CutlineTransformer.3*
%{_mandir}/man3/DatasetProperty.3*
%{_mandir}/man3/EnhanceCBInfo.3*
%{_mandir}/man3/GDAL*.3*
%{_mandir}/man3/NamedColor.3*

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
%{py_sitedir}/gdal.py[co]
%{py_sitedir}/gdalconst.py[co]
%{py_sitedir}/gdalnumeric.py[co]
%{py_sitedir}/ogr.py[co]
%{py_sitedir}/osr.py[co]
%{py_sitedir}/GDAL-*.egg-info
%dir %{py_sitedir}/osgeo
%attr(755,root,root) %{py_sitedir}/osgeo/_gdal.so
%attr(755,root,root) %{py_sitedir}/osgeo/_gdal_array.so
%attr(755,root,root) %{py_sitedir}/osgeo/_gdalconst.so
%attr(755,root,root) %{py_sitedir}/osgeo/_ogr.so
%attr(755,root,root) %{py_sitedir}/osgeo/_osr.so
%{py_sitedir}/osgeo/*.py[co]

%if %{with ruby}
%files -n ruby-gdal
%defattr(644,root,root,755)
%dir %{ruby_sitearchdir}/gdal
%attr(755,root,root) %{ruby_sitearchdir}/gdal/gdal.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/gdalconst.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/ogr.so
%attr(755,root,root) %{ruby_sitearchdir}/gdal/osr.so
%endif
