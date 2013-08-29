# NOTE: internal gsm610 lib is significantly modified
#
# Conditional build:
%bcond_without	apidocs		# without doc
%bcond_without	smb		# SMB support
#
Summary:	Multiformat media decoding library
Summary(pl.UTF-8):	Biblioteka dekodująca wiele formatów multimedialnych
Name:		gmerlin-avdecoder
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	37b19266b098d9d05bb05ebef138ffbd
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-ffmpeg-0.8.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-am.patch
Patch4:		%{name}-ffmpeg2.patch
URL:		http://gmerlin.sourceforge.net/avdec_frame.html
BuildRequires:	a52dec-libs-devel >= 0.7.4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8.5
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	faad2-devel >= 2.0
# avcodec build >= 3412992, avformat build >= 3415808, libpostproc >= 51.0.0, libswscale >= 0.5.0
BuildRequires:	ffmpeg-devel >= 0.7
BuildRequires:	flac-devel >= 1.2.0
BuildRequires:	gavl-devel >= 1.4.0
BuildRequires:	gettext-devel
BuildRequires:	gmerlin-devel >= 1.2.0
BuildRequires:	libcdio-devel >= 0.76
BuildRequires:	libdts-devel >= 0.0.2
# requires DVDREAD_VERSION >= 905; in case of 4.x series it's 4.2.0-1 (as in Th)
BuildRequires:	libdvdread-devel >= 0.9.5
BuildRequires:	libmad-devel >= 0.15.0
BuildRequires:	libmpcdec-devel >= 1.1
BuildRequires:	libmpeg2-devel >= 0.4.0
BuildRequires:	libogg-devel >= 1:1.1
BuildRequires:	libpng-devel >= 1.2.2
%{?with_smb:BuildRequires:	libsmbclient-devel >= 3.0.0}
BuildRequires:	libtheora-devel >= 1.0.0
BuildRequires:	libtiff-devel >= 3.5.0
BuildRequires:	libtool
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	mjpegtools-devel >= 1.9.0
BuildRequires:	openjpeg-devel >= 1.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	schroedinger-devel >= 1.0.5
BuildRequires:	speex-devel >= 1.0.4
BuildRequires:	xorg-lib-libX11-devel >= 1.0.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Requires:	a52dec-libs >= 0.7.4
Requires:	faad2-libs >= 2.0
Requires:	ffmpeg-libs >= 0.7
Requires:	flac >= 1.2.0
Requires:	gavl >= 1.4.0
Requires:	libcdio >= 0.76
Requires:	libdts >= 0.0.2
Requires:	libdvdread >= 0.9.5
Requires:	libmad >= 0.15.0
Requires:	libmpcdec >= 1.1
Requires:	libmpeg2 >= 0.4.0
Requires:	libogg >= 1:1.1
Requires:	libpng >= 1.2.2
%{?with_smb:Requires:	libsmbclient >= 3.0.0}
Requires:	libtheora >= 1.0.0
Requires:	libtiff >= 3.5.0
Requires:	libvorbis >= 1:1.0
Requires:	mjpegtools-libs >= 1.9.0
Requires:	openjpeg >= 1.3
Requires:	schroedinger >= 1.0.5
Requires:	speex >= 1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -ffast-math

%description
General purpose media decoding library. It is one of the most complete
general purpose media decoding libraries. The supported formats and
codecs span a wide range of applications from consumer level (mp3,
divx etc.) to high end production formats like 32 bit PCM and some
professional uncompressed video codecs.

%description -l pl.UTF-8
Ogólnego przeznaczenia biblioteka dekodująca multimedia. Jest to jedna
z najbardziej kompletnych bibliotek tego typu. Obsługiwane formaty
obejmują wiele zastosowań od poziomu konsumenckiego (mp3, divx itp.)
do formatów wysokiej jakości produkcji, jak 32-bitowy PCM i różne
profesjonalne kodeki obrazu bez kompresji.

%package devel
Summary:	Header files for gmerlin_avdec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gmerlin_avdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	a52dec-libs-devel >= 0.7.4
Requires:	faad2-devel >= 2.0
Requires:	ffmpeg-devel >= 0.7
Requires:	flac-devel >= 1.2.0
Requires:	gavl-devel >= 1.4.0
Requires:	libcdio-devel >= 0.76
Requires:	libdts-devel >= 0.0.2
Requires:	libdvdread-devel >= 0.9.5
Requires:	libmad-devel >= 0.15.0
Requires:	libmpcdec-devel >= 1.1
Requires:	libmpeg2-devel >= 0.4.0
Requires:	libogg-devel >= 1:1.1
Requires:	libpng-devel >= 1.2.2
%{?with_smb:Requires:	libsmbclient-devel >= 3.0.0}
Requires:	libtheora-devel >= 1.0.0
Requires:	libtiff-devel >= 3.5.0
Requires:	libvdpau-devel
Requires:	libvorbis-devel >= 1:1.0
Requires:	mjpegtools-devel >= 1.9.0
Requires:	openjpeg-devel >= 1.3
Requires:	schroedinger-devel >= 1.0.5
Requires:	speex-devel >= 1.0.4
Requires:	xorg-lib-libX11-devel >= 1.0.0
Requires:	xorg-lib-libXext-devel
Requires:	zlib-devel

%description devel
Header files for gmerlin_avdec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gmerlin_avdec.

%package static
Summary:	Static gmerlin_avdec library
Summary(pl.UTF-8):	Statyczna biblioteka gmerlin_avdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmerlin_avdec library.

%description static -l pl.UTF-8
Statyczna biblioteka gmerlin_avdec.

%package -n gmerlin-plugin-avdec
Summary:	avdec plugins for Gmerlin library
Summary(pl.UTF-8):	Wtyczki avdec dla biblioteki Gmerlin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmerlin >= 1.2.0

%description -n gmerlin-plugin-avdec
avdec plugins for Gmerlin library.

%description -n gmerlin-plugin-avdec -l pl.UTF-8
Wtyczki avdec dla biblioteki Gmerlin.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_smb:--disable-samba} \
	--enable-static \
	%{!?with_apidocs:--without-doxygen} \
	--with-cpuflags=none
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .la kept for now - .pc is missing proper {Libs,Requires}.private
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgmerlin_avdec.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmerlin/plugins/*.{la,a}
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}/apiref

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/bgavdemux
%attr(755,root,root) %{_bindir}/bgavdump
%attr(755,root,root) %{_libdir}/libgmerlin_avdec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmerlin_avdec.so.1

%files devel
%defattr(644,root,root,755)
%{?with_apidocs:%doc doc/apiref}
%attr(755,root,root) %{_libdir}/libgmerlin_avdec.so
%{_libdir}/libgmerlin_avdec.la
# NOTE: dir shared with gmerlin-devel
%dir %{_includedir}/gmerlin
%{_includedir}/gmerlin/avdec.h
%{_includedir}/gmerlin/bgav_version.h
%{_includedir}/gmerlin/bgavdefs.h
%{_pkgconfigdir}/gmerlin_avdec.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmerlin_avdec.a

%files -n gmerlin-plugin-avdec
%defattr(644,root,root,755)
# no reason for separate packages:
# all plugins make use of just libgmerlin_avcodec (external libs not linked directly)
%attr(755,root,root) %{_libdir}/gmerlin/plugins/i_avdec.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/i_dvb.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/i_dvd.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/i_vcd.so
