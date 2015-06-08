# TODO:
# - be reasonable about devel dependencies - you do not need all of them to
#   use gdal (probably a gdal module or driver shall not imply devel
#   dependency)
# - libjpeg12 (needs patching to use system one, --with-jpeg12 is not sufficient as of 1.9.2)
# - libkml (1.3.0 needed, not released yet)
# - wait for newer pcidsk, switch to external again
# - csharp, java
# - additional, proprietary(?) formats support:
#   - FMEObjects (http://www.safe.com/support/support-resources/fme-downloads/)
#   - ESRI FileGDBAPI (http://resources.arcgis.com/content/geodatabases/10.0/file-gdb-api)
#   - ECW (http://www.erdas.com/products/ecw/ERDASECWJPEG2000SDK/Details.aspx)
#   - Kakadu/JPEG2000 (http://www.kakadusoftware.com/)
#   - MrSID (http://www.lizardtech.com/developer/)
#   - MSG/EUMETSAT (http://www.eumetsat.int/Home/Main/DataAccess/SupportSoftwareTools/index.htm)
#   - Ingres (--with-ingres=/path)
#   - Informix DB (--with-idb)
#   - DWGdirect (members only? http://www.opendwg.org/)
#   - ESRI SDE (http://www.esri.com/software/arcgis/arcsde/index.html)
#
# Conditional build:
%bcond_without	armadillo	# Armadillo support for faster TPS transform
%bcond_without	crnlib		# DDS support via crunch/crnlib
%bcond_without	epsilon		# EPSILON wavelet compression support
%bcond_without	fyba		# SOSI geodata support using FYBA
%bcond_with	grass		# GRASS support (note: dependency loop; use gdal-grass.spec instead)
%bcond_without	gta		# GTA format support
%bcond_without	mysql		# MySQL DB support
%bcond_with	oci		# ORACLE OCI DB and Georaster support
%bcond_without	odbc		# ODBC DB support
%bcond_without	opencl		# OpenCL (GPU) support
%bcond_without	openjpeg	# OpenJPEG 2 (JPEG2000) support
%bcond_with	podofo		# PDF support via podofo instead of poppler
%bcond_without	poppler		# PDF support via poppler
%bcond_without	rasdaman	# Rasdaman support
%bcond_without	spatialite	# SpatiaLite support
%bcond_without	xerces		# Xerces support
%bcond_without	java		# Java and MDB support
%bcond_without	php		# PHP binding
%bcond_without	ruby		# Ruby binding

%if %{with podofo}
%undefine	with_poppler
%endif
%if 0%{!?php_name:1}
%define		php_name	php55
%endif
Summary:	Geospatial Data Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji danych dotyczących powierzchni Ziemi
Name:		gdal
Version:	1.11.2
Release:	5
License:	BSD-like
Group:		Libraries
Source0:	http://download.osgeo.org/gdal/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	90221810dd9ca656ee23d434d4266ef6
Patch0:		%{name}-perl.patch
Patch1:		%{name}-python_install.patch
Patch2:		%{name}-php.patch
Patch3:		%{name}-fpic.patch
Patch4:		%{name}-format-security.patch
Patch5:		%{name}-grass.patch
Patch6:		%{name}-sse.patch
Patch7:		%{name}-link.patch
Patch8:		%{name}-fyba.patch
Patch9:		%{name}-dds.patch
Patch11:	%{name}-armadillo.patch
Patch12:	%{name}-rasdaman.patch
Patch13:	%{name}-pluginsdir.patch
Patch14:	poppler-0.31.patch
URL:		http://www.gdal.org/
%{?with_php:BuildRequires:	%{php_name}-devel}
%{?with_opencl:BuildRequires:	OpenCL-devel >= 1.0}
%{?with_armadillo:BuildRequires:	armadillo-devel}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cfitsio-devel
%{?with_crnlib:BuildRequires:	crnlib-devel}
BuildRequires:	curl-devel
BuildRequires:	doxygen >= 1.4.2
%{?with_epsilon:BuildRequires:	epsilon-compressor-devel}
BuildRequires:	expat-devel >= 1.95.0
%{?with_fyba:BuildRequires:	fyba-devel}
BuildRequires:	freexl-devel >= 1.0
BuildRequires:	gcc >= 6:4.1
BuildRequires:	geos-devel >= 3.1.0
BuildRequires:	giflib-devel >= 4.0
%{?with_grass:BuildRequires:	grass-devel >= 6.4}
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	hdf5-devel
BuildRequires:	jasper-devel
%{?with_java:BuildRequires:	jdk}
%{?with_java:BuildRequires:	jpackage-utils}
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	libcsf-devel
BuildRequires:	libdap-devel >= 3.10
BuildRequires:	libgeotiff-devel >= 1.2.1
%{?with_gta:BuildRequires:	libgta-devel}
BuildRequires:	libjpeg-devel >= 6b
#BuildRequires:	libkml-devel >= 1.3.0
BuildRequires:	libpng-devel >= 2:1.2.8
%{?with_spatialite:BuildRequires:	libspatialite-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 2
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	netcdf-devel >= 4.1
BuildRequires:	ogdi-devel >= 3.1
%{?with_openjpeg:BuildRequires:	openjpeg2-devel >= 2.0.0-2}
# 8.1.7 for DB support, 10.0.1 for georaster
%{?with_oci:BuildRequires:	oracle-instantclient-devel >= 10.0.1}
#BuildRequires:	pcidsk-devel > 0.3
BuildRequires:	perl-devel
%{?with_podofo:BuildRequires:	podofo-devel}
%{?with_poppler:BuildRequires:	poppler-devel >= 0.24}
# ensure it's compiled with PQescapeStringConn support
BuildRequires:	postgresql-backend-devel >= 8.1.4
BuildRequires:	postgresql-devel >= 8.1.4
BuildRequires:	proj-devel >= 4
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-devel >= 1:1.0.0
BuildRequires:	python-setuptools
%{?with_rasdaman:BuildRequires:	rasdaman-devel}
BuildRequires:	rpm-pythonprov
%{?with_ruby:BuildRequires:	rpm-rubyprov}
BuildRequires:	rpmbuild(macros) >= 1.344
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	swig-perl
BuildRequires:	swig-php >= 2.0.12-2
BuildRequires:	swig-python >= 1.3
%{?with_ruby:BuildRequires:	swig-ruby}
BuildRequires:	texlive-dvips
BuildRequires:	texlive-latex
%{?with_odbc:BuildRequires:	unixODBC-devel >= 2.2.15}
%{?with_xerces:BuildRequires:	xerces-c-devel >= 2.7.0}
BuildRequires:	xz-devel
BuildRequires:	zlib-devel >= 1.1.4
Requires:	freexl >= 1.0
Requires:	geos >= 3.1.0
Requires:	libgeotiff >= 1.2.1
Requires:	libpng >= 2:1.2.8
Requires:	libtiff >= 4.0
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
%{?with_opencl:Requires:	OpenCL-devel >= 1.0}
%{?with_armadillo:Requires:	armadillo-devel}
Requires:	cfitsio-devel
%{?with_crnlib:Requires:	crnlib-devel}
Requires:	curl-devel
%{?with_epsilon:Requires:	epsilon-compressor-devel}
%{?with_fyba:Requires:	fyba-devel}
Requires:	expat-devel >= 1.95.0
Requires:	freexl-devel >= 1.0
Requires:	geos-devel >= 3.1.0
Requires:	giflib-devel >= 4.0
Requires:	hdf-devel >= 4.0
Requires:	hdf5-devel
Requires:	jasper-devel
Requires:	json-c-devel >= 0.11
Requires:	libcsf-devel
Requires:	libdap-devel >= 3.10
Requires:	libgeotiff-devel >= 1.2.1
%{?with_gta:Requires:	libgta-devel}
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel >= 2:1.2.8
%{?with_spatialite:Requires:	libspatialite-devel}
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 4.0
Requires:	libuuid-devel
Requires:	libwebp-devel
Requires:	libxml2-devel >= 2
%{?with_mysql:Requires:	mysql-devel}
Requires:	netcdf-devel >= 4
Requires:	ogdi-devel >= 3.1
%{?with_openjpeg:Requires:	openjpeg2-devel >= 2.0.0-2}
#Requires:	pcidsk-devel > 0.3
%{?with_podofo:Requires:	podofo-devel}
%{?with_poppler:Requires:	poppler-devel >= 0.24}
Requires:	postgresql-devel
Requires:	proj-devel >= 4
%{?with_rasdaman:Requires:	rasdaman-devel}
Requires:	sqlite3-devel >= 3.0.0
%{?with_odbc:Requires:	unixODBC-devel}
%{?with_xerces:Requires:	xerces-c-devel >= 2.7.0}
Requires:	xz-devel
Requires:	zlib-devel >= 1.1.4

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

%package -n %{php_name}-gdal
Summary:	PHP bindings for GDAL library
Summary(pl.UTF-8):	Wiązania PHP do biblioteki GDAL
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}

%description -n %{php_name}-gdal
PHP bindings for GDAL library

%description -n %{php_name}-gdal -l pl.UTF-8
Wiązania PHP do biblioteki GDAL.

%package -n python-gdal
Summary:	GDAL Python module
Summary(pl.UTF-8):	Moduł Pythona GDAL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs

%description -n python-gdal
GDAL Python module.

%description -n python-gdal -l pl.UTF-8
Moduł Pythona GDAL.

%package -n ruby-gdal
Summary:	Ruby bindings for GDAL
Summary(pl.UTF-8):	Wiązania języka Ruby do pakietu GDAL
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

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
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

# need to regenerate (old ones don't support perl 5.10 or php 5.5)
%{__rm} swig/{perl,php}/{gdal_wrap.cpp,gdalconst_wrap.c,ogr_wrap.cpp,osr_wrap.cpp}

%{__sed} -i \
	-e 's/^CC=gcc/CC=%{__cc}/' \
	-e 's/^CXX=g++/CXX=%{__cxx}/' \
	-e 's/^CFLAGS=-fpic/CFLAGS=%{rpmcflags} -fPIC/' \
	-e 's/^LDFLAGS=-shared/LDFLAGS=%{rpmldflags} -shared/' \
	swig/php/GNUmakefile
# Build with fPIC to allow Ruby bindings
# Xcompiler should normally achieve that -- http://trac.osgeo.org/gdal/ticket/3978
# http://trac.osgeo.org/gdal/ticket/1994
sed -i 's|\$(CFLAGS)|$(CFLAGS) -fPIC|g' swig/ruby/RubyMakefile.mk
# Install Ruby bindings to distribution specific directory
sed -i 's|RUBY_EXTENSIONS_DIR :=.*|RUBY_EXTENSIONS_DIR := %{ruby_vendorarchdir}|' swig/ruby/RubyMakefile.mk

# Install Ruby bindings into the proper place
sed -i -e 's|^$(INSTALL_DIR):|$(DESTDIR)$(INSTALL_DIR):|' swig/ruby/RubyMakefile.mk
sed -i -e 's|^install: $(INSTALL_DIR)|install: $(DESTDIR)$(INSTALL_DIR)|' swig/ruby/RubyMakefile.mk

# our man path
sed -i -e 's#^mandir=.*##g' configure.in

%{__rm} -r man

%{__sed} -i -e 's,DODS_INC="-I.*,DODS_INC="$(pkg-config --cflags libdap)",' configure.in

%build
%ifarch %{x8664}
jvm_arch=amd64
%endif
%ifarch %{ix86}
jvm_arch=i386
%endif
%ifarch x32
jvm_arch=x32
%endif

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	--includedir=%{_includedir}/gdal \
	--datadir=%{_datadir}/gdal \
	--with-dods-root=/usr \
	%{?with_armadillo:--with-armadillo} \
	%{?with_crnlib:--with-dds} \
	%{?with_epsilon:--with-epsilon} \
	%{?with_grass:--with-grass} \
	%{!?with_gta:--without-gta} \
	--with-hide-internal-symbols \
	%{?with_java:--with-java=%{java_home}} \
	--with-liblzma \
	%{?with_java:--with-mdb --with-jvm-lib-add-rpath --with-jvm-lib=%{java_home}/jre/lib/$jvm_arch/server} \
	%{?with_mysql:--with-mysql} \
	%{?with_oci:--with-oci --with-oci-include=/usr/include/oracle/client --with-oci-lib=%{_libdir}} \
	%{?with_opencl:--with-opencl} \
	--with-perl \
	%{?with_php:--with-php} \
	%{?with_podofo:--with-podofo} \
	%{?with_poppler:--with-poppler} \
	--with-python \
	%{?with_rasdaman:--with-rasdaman=%{_libdir}/rasdaman} \
	%{?with_ruby:--with-ruby} \
	%{?with_fyba:--with-sosi} \
	%{?with_spatialite:--with-spatialite} \
	--with-sqlite3 \
	--with-webp \
	%{?with_xerces:--with-xerces} \
	--with-xerces-inc=/usr/include/xercesc \
	--with-xerces-lib="-lxerces-c" \
	--without-libgrass
#	--with-pcidsk=/usr (needs > 0.3)
# csharp builds, but has no configure option nor install target

# regenerate where needed
%{__make} -j1 -C swig/perl generate
%if %{with ruby}
%{__make} -j1 -C swig/ruby generate
%endif

%{__make} -j1 \
	%{?with_grass:GRASS_INCLUDE="-I/usr/include/grass64"} \
	%{?with_fyba:SOSI_INC="-I/usr/include/fyba"}

%{__make} -j1 docs

%{__make} -j1 man

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-man \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf _html
cp -a html _html
cp -a ogr/html _html/ogr

%if %{with php}
# missing in make install
install -d $RPM_BUILD_ROOT%{php_extensiondir}
install -p swig/php/php_gdal.so $RPM_BUILD_ROOT%{php_extensiondir}/gdal.so
install -p swig/php/php_gdalconst.so $RPM_BUILD_ROOT%{php_extensiondir}/gdalconst.so
install -p swig/php/php_ogr.so $RPM_BUILD_ROOT%{php_extensiondir}/ogr.so
install -p swig/php/php_osr.so $RPM_BUILD_ROOT%{php_extensiondir}/osr.so
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
cat <<'EOF' >$RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/gdal.ini
; Enable gdal extension modules
extension=gdal.so
extension=gdalconst.so
extension=ogr.so
extension=osr.so
EOF
%endif

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/GDAL/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/GDAL/Const/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/OGR/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Geo/OSR/.packlist

# some doxygen trash
%{__rm} $RPM_BUILD_ROOT%{_bindir}/gdal{compare,move}.dox
%{__rm} $RPM_BUILD_ROOT%{_bindir}/gdal_{calc,edit,fillnodata,polygonize,proximity,sieve}.dox

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
%attr(755,root,root) %{_bindir}/gdal_auth.py
%attr(755,root,root) %{_bindir}/gdal_contour
%attr(755,root,root) %{_bindir}/gdal_calc.py
%attr(755,root,root) %{_bindir}/gdal_edit.py
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
%attr(755,root,root) %{_bindir}/gdalcompare.py
%attr(755,root,root) %{_bindir}/gdaldem
%attr(755,root,root) %{_bindir}/gdalenhance
%attr(755,root,root) %{_bindir}/gdalident.py
%attr(755,root,root) %{_bindir}/gdalimport.py
%attr(755,root,root) %{_bindir}/gdalinfo
%attr(755,root,root) %{_bindir}/gdallocationinfo
%attr(755,root,root) %{_bindir}/gdalmanage
%attr(755,root,root) %{_bindir}/gdalmove.py
%attr(755,root,root) %{_bindir}/gdalserver
%attr(755,root,root) %{_bindir}/gdalsrsinfo
%attr(755,root,root) %{_bindir}/gdaltindex
%attr(755,root,root) %{_bindir}/gdaltransform
%attr(755,root,root) %{_bindir}/gdalwarp
%attr(755,root,root) %{_bindir}/mkgraticule.py
%attr(755,root,root) %{_bindir}/nearblack
%attr(755,root,root) %{_bindir}/ogr2ogr
%attr(755,root,root) %{_bindir}/ogrinfo
%attr(755,root,root) %{_bindir}/ogrlineref
%attr(755,root,root) %{_bindir}/ogrtindex
%attr(755,root,root) %{_bindir}/pct2rgb.py
%attr(755,root,root) %{_bindir}/rgb2pct.py
%attr(755,root,root) %{_bindir}/testepsg
%attr(755,root,root) %{_libdir}/libgdal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdal.so.1
%dir %{_libdir}/gdalplugins
%{_datadir}/gdal
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal_calc.1*
%{_mandir}/man1/gdal_contour.1*
%{_mandir}/man1/gdal_edit.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_grid.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdal_polygonize.1*
%{_mandir}/man1/gdal_proximity.1*
%{_mandir}/man1/gdal_rasterize.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/gdal_translate.1*
%{_mandir}/man1/gdal_utilities.1*
%{_mandir}/man1/gdaladdo.1*
%{_mandir}/man1/gdalbuildvrt.1*
%{_mandir}/man1/gdalcompare.1*
%{_mandir}/man1/gdaldem.1*
%{_mandir}/man1/gdalinfo.1*
%{_mandir}/man1/gdallocationinfo.1*
%{_mandir}/man1/gdalmanage.1*
%{_mandir}/man1/gdalmove.1*
%{_mandir}/man1/gdalsrsinfo.1*
%{_mandir}/man1/gdaltindex.1*
%{_mandir}/man1/gdaltransform.1*
%{_mandir}/man1/gdalwarp.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr2ogr.1*
%{_mandir}/man1/ogr_utilities.1*
%{_mandir}/man1/ogrinfo.1*
%{_mandir}/man1/ogrlineref.1*
%{_mandir}/man1/ogrtindex.1*
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*

%files devel
%defattr(644,root,root,755)
%doc _html/*
%attr(755,root,root) %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so
%{_libdir}/libgdal.la
%{_pkgconfigdir}/gdal.pc
%{_includedir}/gdal
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
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/GDAL.so
%dir %{perl_vendorarch}/auto/Geo/GDAL/Const
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/Const/Const.so
%dir %{perl_vendorarch}/auto/Geo/OGR
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OGR/OGR.so
%dir %{perl_vendorarch}/auto/Geo/OSR
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OSR/OSR.so

%if %{with php}
%files -n %{php_name}-gdal
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/gdal.ini
%attr(755,root,root) %{php_extensiondir}/gdal.so
%attr(755,root,root) %{php_extensiondir}/gdalconst.so
%attr(755,root,root) %{php_extensiondir}/ogr.so
%attr(755,root,root) %{php_extensiondir}/osr.so
%endif

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
%dir %{ruby_vendorarchdir}/gdal
%attr(755,root,root) %{ruby_vendorarchdir}/gdal/gdal.so
%attr(755,root,root) %{ruby_vendorarchdir}/gdal/gdalconst.so
%attr(755,root,root) %{ruby_vendorarchdir}/gdal/ogr.so
%attr(755,root,root) %{ruby_vendorarchdir}/gdal/osr.so
%endif
