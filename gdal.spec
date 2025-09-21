# TODO:
# - be reasonable about devel dependencies - you do not need all of them to
#   use gdal (probably a gdal module or driver shall not imply devel dependency)
# - MongoCXX (mongo/client/dbclient.h, -lmongoclient -lboost_system -lboost_thread -lboost_regex)
# - rasterlite2
# - sfcgal >= 1.2.2
# - libjpeg12 (needs patching to use system one, --with-jpeg12 is not sufficient as of 1.9.2)
# - libkml (1.3.0 needed, not released yet)
# - csharp, java
# - additional, proprietary(?) formats support:
#   - FMEObjects (http://www.safe.com/support/support-resources/fme-downloads/)
#   - ESRI FileGDBAPI (http://resources.arcgis.com/content/geodatabases/10.0/file-gdb-api)
#   - ECW (http://www.erdas.com/products/ecw/ERDASECWJPEG2000SDK/Details.aspx)
#   - Kakadu/JPEG2000 (http://www.kakadusoftware.com/)
#   - MrSID (http://www.lizardtech.com/developer/)
#   - LuraTech JP2Lura 
#   - MSG/EUMETSAT (http://www.eumetsat.int/Home/Main/DataAccess/SupportSoftwareTools/index.htm)
#   - Ingres (--with-ingres=/path)
#   - Informix DB (--with-idb)
#   - DWGdirect (members only? http://www.opendwg.org/)
#   - ESRI SDE (http://www.esri.com/software/arcgis/arcsde/index.html)
#   - Teigha DWG/DGN (https://www.opendesign.com/products/drawings?)
#
# Conditional build:
%bcond_without	armadillo	# Armadillo support for faster TPS transform
%bcond_without	fyba		# SOSI geodata support using FYBA
%bcond_without	gta		# GTA format support
%bcond_without	kea		# KEA format support
%bcond_without	mysql		# MySQL DB support
%bcond_without	odbc		# ODBC DB support
%bcond_without	opencl		# OpenCL (GPU) support
%bcond_without	openjpeg	# OpenJPEG 2 (JPEG2000) support
%bcond_with	podofo		# PDF support via podofo instead of poppler
%bcond_without	poppler		# PDF support via poppler
%bcond_without	xerces		# Xerces support
%bcond_without	java		# Java and MDB support

%if %{with podofo}
%undefine	with_poppler
%endif

%{?use_default_jdk}

Summary:	Geospatial Data Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji danych dotyczących powierzchni Ziemi
Name:		gdal
Version:	3.11.3
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	https://github.com/OSGeo/gdal/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	436c9e7e244613a1073738eeaec05600
URL:		http://www.gdal.org/
# 1.x or 2.x supported
BuildRequires:	CharLS-devel
%{?with_opencl:BuildRequires:	OpenCL-devel >= 1.0}
%{?with_armadillo:BuildRequires:	armadillo-devel}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cfitsio-devel
BuildRequires:	cryptopp-devel
BuildRequires:	curl-devel
BuildRequires:	doxygen >= 1.4.2
BuildRequires:	expat-devel >= 1.95.0
%{?with_fyba:BuildRequires:	fyba-devel}
BuildRequires:	freexl-devel >= 1.0
BuildRequires:	gcc >= 6:4.1
BuildRequires:	geos-devel >= 3.1.0
BuildRequires:	giflib-devel >= 4.0
BuildRequires:	hdf-devel >= 4.2.5
BuildRequires:	hdf5-devel
BuildRequires:	jasper-devel
%{?with_java:%buildrequires_jdk}
%{?with_java:BuildRequires:	jpackage-utils}
BuildRequires:	json-c-devel >= 0.11
%{?with_kea:BuildRequires:	kealib-devel}
BuildRequires:	libavif-devel
BuildRequires:	libcsf-devel >= 2.0-0.041111.6
BuildRequires:	libdap-devel >= 3.10
BuildRequires:	libgeotiff-devel >= 1.2.1
%{?with_gta:BuildRequires:	libgta-devel}
BuildRequires:	libjpeg-devel >= 6b
#BuildRequires:	libkml-devel >= 1.3.0
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4.0
BuildRequires:	libtirpc-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 2
#%{?with_mysql:BuildRequires:	mysql-devel >= 4}
%{?with_mysql:BuildRequires:	/usr/bin/mysql_config}
BuildRequires:	netcdf-devel >= 4.1
BuildRequires:	ogdi-devel >= 3.1
%{?with_openjpeg:BuildRequires:	openjpeg2-devel >= 2.1.0}
# 8.1.7 for DB support, 10.0.1 for georaster
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig >= 1:0.21
%{?with_podofo:BuildRequires:	podofo-devel}
%{?with_poppler:BuildRequires:	poppler-devel >= 0.24}
# ensure it's compiled with PQescapeStringConn support
BuildRequires:	postgresql-backend-devel >= 8.1.4
BuildRequires:	postgresql-devel >= 8.1.4
BuildRequires:	proj-devel >= 4
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numpy-devel >= 1:1.0.0
BuildRequires:	python-setuptools
BuildRequires:	qhull-devel >= 2012
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	swig-python >= 1.3
BuildRequires:	texlive-dvips
BuildRequires:	texlive-latex
%{?with_odbc:BuildRequires:	unixODBC-devel >= 2.2.15}
%{?with_xerces:BuildRequires:	xerces-c-devel >= 3.1.0}
BuildRequires:	xz-devel
BuildRequires:	zlib-devel >= 1.1.4
# for ZSTD compression in TIFF
BuildRequires:	zstd-devel
%{?with_java:Requires:	 %{?use_jdk:%{use_jdk}-jre-base}%{!?use_jdk:jre}}
Requires:	freexl >= 1.0
Requires:	geos >= 3.1.0
Requires:	hdf >= 4.2.5
Requires:	libgeotiff >= 1.2.1
Requires:	libpng >= 2:1.2.8
Requires:	libtiff >= 4.0
%{?with_openjpeg:Requires:	openjpeg2 >= 2.1.0}
Requires:	qhull >= 2012
%{?with_xerces:Requires:	xerces-c >= 3.1.0}
Obsoletes:	gdal-static < 3.10.0
Obsoletes:	perl-gdal < 3.10.0
Obsoletes:	python-gdal < 3.10.0
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
Requires:	CharLS-devel
%{?with_opencl:Requires:	OpenCL-devel >= 1.0}
%{?with_armadillo:Requires:	armadillo-devel}
Requires:	cfitsio-devel
Requires:	cryptopp-devel
Requires:	curl-devel
%{?with_fyba:Requires:	fyba-devel}
Requires:	expat-devel >= 1.95.0
Requires:	freexl-devel >= 1.0
Requires:	geos-devel >= 3.1.0
Requires:	giflib-devel >= 4.0
Requires:	hdf-devel >= 4.2.5
Requires:	hdf5-devel
Requires:	jasper-devel
Requires:	json-c-devel >= 0.11
%{?with_kea:Requires:	kealib-devel}
Requires:	libcsf-devel
Requires:	libdap-devel >= 3.10
Requires:	libgeotiff-devel >= 1.2.1
%{?with_gta:Requires:	libgta-devel}
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel >= 2:1.2.8
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 4.0
Requires:	libuuid-devel
Requires:	libwebp-devel
Requires:	libxml2-devel >= 2
%{?with_mysql:Requires:	/usr/bin/mysql_config}
Requires:	netcdf-devel >= 4
Requires:	ogdi-devel >= 3.1
%{?with_openjpeg:Requires:	openjpeg2-devel >= 2.1.0}
Requires:	pcre-devel
%{?with_podofo:Requires:	podofo-devel}
%{?with_poppler:Requires:	poppler-devel >= 0.24}
Requires:	postgresql-devel
Requires:	proj-devel >= 4
Requires:	qhull-devel >= 2012
Requires:	sqlite3-devel >= 3.0.0
%{?with_odbc:Requires:	unixODBC-devel}
%{?with_xerces:Requires:	xerces-c-devel >= 3.1.0}
Requires:	xz-devel
Requires:	zlib-devel >= 1.1.4
Requires:	zstd-devel

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

%package -n python3-gdal
Summary:	GDAL Python module
Summary(pl.UTF-8):	Moduł Pythona GDAL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs

%description -n python3-gdal
GDAL Python module.

%description -n python3-gdal -l pl.UTF-8
Moduł Pythona GDAL.

%package -n bash-completion-gdal
Summary:	Bash completion for GDAL command line programs
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-gdal
Bash completion for GDAL command line programs.

%prep
%setup -q

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
	  -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' \
	  -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      swig/python/gdal-utils/scripts/gdal2tiles.py \
      swig/python/gdal-utils/scripts/gdal2xyz.py \
      swig/python/gdal-utils/scripts/gdal_calc.py \
      swig/python/gdal-utils/scripts/gdal_edit.py \
      swig/python/gdal-utils/scripts/gdal_fillnodata.py \
      swig/python/gdal-utils/scripts/gdal_merge.py \
      swig/python/gdal-utils/scripts/gdal_pansharpen.py \
      swig/python/gdal-utils/scripts/gdal_polygonize.py \
      swig/python/gdal-utils/scripts/gdal_proximity.py \
      swig/python/gdal-utils/scripts/gdal_retile.py \
      swig/python/gdal-utils/scripts/gdal_sieve.py \
      swig/python/gdal-utils/scripts/gdalcompare.py \
      swig/python/gdal-utils/scripts/gdalmove.py \
      swig/python/gdal-utils/scripts/ogrmerge.py \
      swig/python/gdal-utils/scripts/pct2rgb.py \
      swig/python/gdal-utils/scripts/rgb2pct.py

%build
mkdir -p build
cd build

%if %{with java}
%ifarch %{x8664}
jvm_arch=amd64
%endif
%ifarch %{ix86}
jvm_arch=i386
%endif
%ifarch x32
jvm_arch=x32
%endif
%ifarch aarch64
jvm_arch=aarch64
%endif
%ifarch %{arm}
jvm_arch=aarch32
%endif
for jvm_type in server client; do
	for dir in lib jre/lib/$jvm_arch; do
		if [ -f "%{java_home}/$dir/$jvm_type/libjvm.so" ]; then
			jvm_lib="%{java_home}/$dir/$jvm_type"
			break
		fi
	done
done
%endif

%cmake ../ \
	-DPython_EXECUTABLE=%{__python3} \
	-DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/gdal \
	-DGDAL_HIDE_INTERNAL_SYMBOLS:BOOL=ON \
	-DBUILD_PYTHON_BINDINGS:BOOL=ON \
	-DGDAL_USE_LIBLZMA:BOOL=ON \
	-DGDAL_USE_SQLITE3:BOOL=ON \
	-DGDAL_USE_WEBP:BOOL=ON \
	-DGDAL_USE_TIFF_INTERNAL=OFF \
%if %{with java}
	-DBUILD_JAVA_BINDINGS:BOOL=ON \
	-DJAVA_HOME=%{java_home} \
	-DJAVA_JVM_LIBRARY:FILEPATH="$jvm_lib" \
%endif
	%{cmake_on_off armadillo GDAL_USE_ARMADILLO} \
	%{cmake_on_off gta GDAL_USE_GTA} \
	%{cmake_on_off kea GDAL_USE_KEA} \
	%{cmake_on_off mysql GDAL_USE_MYSQL} \
	%{cmake_on_off opencl GDAL_USE_OPENCL} \
	%{cmake_on_off podofo GDAL_USE_PODOFO} \
	%{cmake_on_off poppler GDAL_USE_POPPLER} \
	%{cmake_on_off fyba GDAL_USE_FYBA} \
	%{cmake_on_off xerces GDAL_USE_XERCESC}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS.md PROVENANCE.TXT
%attr(755,root,root) %{_bindir}/gdal
%attr(755,root,root) %{_bindir}/gdal2tiles
%attr(755,root,root) %{_bindir}/gdal2tiles.py
%attr(755,root,root) %{_bindir}/gdal2xyz
%attr(755,root,root) %{_bindir}/gdal2xyz.py
%attr(755,root,root) %{_bindir}/gdaladdo
%attr(755,root,root) %{_bindir}/gdalattachpct
%attr(755,root,root) %{_bindir}/gdalattachpct.py
%attr(755,root,root) %{_bindir}/gdalbuildvrt
%attr(755,root,root) %{_bindir}/gdal_calc
%attr(755,root,root) %{_bindir}/gdal_calc.py
%attr(755,root,root) %{_bindir}/gdalcompare
%attr(755,root,root) %{_bindir}/gdalcompare.py
%attr(755,root,root) %{_bindir}/gdal_contour
%attr(755,root,root) %{_bindir}/gdal_create
%attr(755,root,root) %{_bindir}/gdaldem
%attr(755,root,root) %{_bindir}/gdal_edit
%attr(755,root,root) %{_bindir}/gdal_edit.py
%attr(755,root,root) %{_bindir}/gdalenhance
%attr(755,root,root) %{_bindir}/gdal_fillnodata
%attr(755,root,root) %{_bindir}/gdal_fillnodata.py
%attr(755,root,root) %{_bindir}/gdal_footprint
%attr(755,root,root) %{_bindir}/gdal_grid
%attr(755,root,root) %{_bindir}/gdalinfo
%attr(755,root,root) %{_bindir}/gdallocationinfo
%attr(755,root,root) %{_bindir}/gdalmanage
%attr(755,root,root) %{_bindir}/gdalmdiminfo
%attr(755,root,root) %{_bindir}/gdalmdimtranslate
%attr(755,root,root) %{_bindir}/gdal_merge
%attr(755,root,root) %{_bindir}/gdal_merge.py
%attr(755,root,root) %{_bindir}/gdalmove
%attr(755,root,root) %{_bindir}/gdalmove.py
%attr(755,root,root) %{_bindir}/gdal_pansharpen
%attr(755,root,root) %{_bindir}/gdal_pansharpen.py
%attr(755,root,root) %{_bindir}/gdal_polygonize
%attr(755,root,root) %{_bindir}/gdal_polygonize.py
%attr(755,root,root) %{_bindir}/gdal_proximity
%attr(755,root,root) %{_bindir}/gdal_proximity.py
%attr(755,root,root) %{_bindir}/gdal_rasterize
%attr(755,root,root) %{_bindir}/gdal_retile
%attr(755,root,root) %{_bindir}/gdal_retile.py
%attr(755,root,root) %{_bindir}/gdal_sieve
%attr(755,root,root) %{_bindir}/gdal_sieve.py
%attr(755,root,root) %{_bindir}/gdalsrsinfo
%attr(755,root,root) %{_bindir}/gdaltindex
%attr(755,root,root) %{_bindir}/gdaltransform
%attr(755,root,root) %{_bindir}/gdal_translate
%attr(755,root,root) %{_bindir}/gdal_viewshed
%attr(755,root,root) %{_bindir}/gdalwarp
%attr(755,root,root) %{_bindir}/gnmanalyse
%attr(755,root,root) %{_bindir}/gnmmanage
%attr(755,root,root) %{_bindir}/nearblack
%attr(755,root,root) %{_bindir}/ogr2ogr
%attr(755,root,root) %{_bindir}/ogrinfo
%attr(755,root,root) %{_bindir}/ogr_layer_algebra
%attr(755,root,root) %{_bindir}/ogr_layer_algebra.py
%attr(755,root,root) %{_bindir}/ogrlineref
%attr(755,root,root) %{_bindir}/ogrmerge
%attr(755,root,root) %{_bindir}/ogrmerge.py
%attr(755,root,root) %{_bindir}/ogrtindex
%attr(755,root,root) %{_bindir}/pct2rgb
%attr(755,root,root) %{_bindir}/pct2rgb.py
%attr(755,root,root) %{_bindir}/rgb2pct
%attr(755,root,root) %{_bindir}/rgb2pct.py
%attr(755,root,root) %{_bindir}/sozip
%attr(755,root,root) %{_libdir}/libgdal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdal.so.37
%dir %{_libdir}/gdalplugins
%{_libdir}/gdalplugins/drivers.ini
%{_datadir}/gdal
%{_mandir}/man1/gdal2tiles.1*
%{_mandir}/man1/gdal.1*
%{_mandir}/man1/gdal-convert.1*
%{_mandir}/man1/gdal-info.1*
%{_mandir}/man1/gdal-mdim*.1*
%{_mandir}/man1/gdal-raster*.1*
%{_mandir}/man1/gdal-vector*.1*
%{_mandir}/man1/gdal-vsi*.1*
%{_mandir}/man1/gdal_calc.1*
%{_mandir}/man1/gdal_contour.1*
%{_mandir}/man1/gdal_create.1*
%{_mandir}/man1/gdal_edit.1*
%{_mandir}/man1/gdal_fillnodata.1*
%{_mandir}/man1/gdal_footprint.1*
%{_mandir}/man1/gdal_grid.1*
%{_mandir}/man1/gdal_merge.1*
%{_mandir}/man1/gdal_pansharpen.1*
%{_mandir}/man1/gdal_polygonize.1*
%{_mandir}/man1/gdal_proximity.1*
%{_mandir}/man1/gdal_rasterize.1*
%{_mandir}/man1/gdal_retile.1*
%{_mandir}/man1/gdal_sieve.1*
%{_mandir}/man1/gdal_translate.1*
%{_mandir}/man1/gdal_viewshed.1*
%{_mandir}/man1/gdaladdo.1*
%{_mandir}/man1/gdalbuildvrt.1*
%{_mandir}/man1/gdalcompare.1*
%{_mandir}/man1/gdaldem.1*
%{_mandir}/man1/gdalinfo.1*
%{_mandir}/man1/gdallocationinfo.1*
%{_mandir}/man1/gdalmanage.1*
%{_mandir}/man1/gdalmdiminfo.1*
%{_mandir}/man1/gdalmdimtranslate.1*
%{_mandir}/man1/gdalmove.1*
%{_mandir}/man1/gdalsrsinfo.1*
%{_mandir}/man1/gdaltindex.1*
%{_mandir}/man1/gdaltransform.1*
%{_mandir}/man1/gdalwarp.1*
%{_mandir}/man1/gnmanalyse.1*
%{_mandir}/man1/gnmmanage.1*
%{_mandir}/man1/nearblack.1*
%{_mandir}/man1/ogr2ogr.1*
%{_mandir}/man1/ogrinfo.1*
%{_mandir}/man1/ogr_layer_algebra.1*
%{_mandir}/man1/ogrlineref.1*
%{_mandir}/man1/ogrmerge.1*
%{_mandir}/man1/ogrtindex.1*
%{_mandir}/man1/pct2rgb.1*
%{_mandir}/man1/rgb2pct.1*
%{_mandir}/man1/sozip.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdal-config
%attr(755,root,root) %{_libdir}/libgdal.so
%{_pkgconfigdir}/gdal.pc
%{_includedir}/gdal
%{_mandir}/man1/gdal-config.1*
%{_libdir}/cmake/gdal

%files -n python3-gdal
%defattr(644,root,root,755)
%{py3_sitedir}/GDAL-*.egg-info
%dir %{py3_sitedir}/osgeo
%{py3_sitedir}/osgeo/__pycache__
%{py3_sitedir}/osgeo/*.py
%attr(755,root,root) %{py3_sitedir}/osgeo/_gdal.*.so
%attr(755,root,root) %{py3_sitedir}/osgeo/_gdal_array.*.so
%attr(755,root,root) %{py3_sitedir}/osgeo/_gdalconst.*.so
%attr(755,root,root) %{py3_sitedir}/osgeo/_gnm.*.so
%attr(755,root,root) %{py3_sitedir}/osgeo/_ogr.*.so
%attr(755,root,root) %{py3_sitedir}/osgeo/_osr.*.so
%{py3_sitedir}/osgeo_utils/

%files -n bash-completion-gdal
%defattr(644,root,root,755)
%{bash_compdir}/gdal*
%{bash_compdir}/ogr*
