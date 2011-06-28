#
# Conditional build:
%bcond_without	apidocs	# without doc
Summary:	Multiformat decoding library
Name:		gmerlin-avdecoder
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	c1ea663e9da631453eec4ac79138b6c5
Patch0:		%{name}-cflags.patch
URL:		http://gmerlin.sourceforge.net/avdec_frame.html
BuildRequires:	a52dec-libs-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	gavl-devel
#BuildRequires:	gmerlin-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdts-devel
#BuildRequires:	libdvdread-devel >= 0.9.5
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	openjpeg-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	samba-devel
#BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -ffast-math

%description
General purpose media decoding library. It is one of the most complete
general purpose media decoding libraries. The supported formats and
codecs span a wide range of applications from consumer level (mp3,
divx etc.) to high end production formats like 32 bit PCM and some
professional uncompressed video codecs.
Using gmerlin_avdecoder in your playback for transcoding application
means rock solid media format support with an ever growing list of
supported codecs and formats

%package devel
Summary:	Header files for %{name} library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and
development documentation for %{name}.

%package static
Summary:	Static %{name} library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	%{!?with_apidocs:--without-doxygen} \
	--with-cpuflags=none
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT{%{_libdir}/*.la,%{_prefix}/share/doc/%{name}}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgmerlin_avdec.so.?
%attr(755,root,root) %{_libdir}/libgmerlin_avdec.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{?with_apidocs:%doc doc/apiref}
%attr(755,root,root) %{_bindir}/bgavd*
%attr(755,root,root) %{_libdir}/libgmerlin_avdec.so
%{_includedir}/gmerlin
%{_pkgconfigdir}/gmerlin_avdec.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmerlin_avdec.a
