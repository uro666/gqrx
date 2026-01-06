Name:		gqrx
Version:	2.17.7
Release:	1
Source0:	https://github.com/gqrx-sdr/gqrx/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Software defined radio receiver powered by GNU Radio and Qt
URL:		https://github.com/gqrx-sdr/gqrx
License:	GPL-3.0-only
Group:		Communications/Radio
BuildSystem:	cmake
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	cmake(gnuradio-osmosdr)
BuildRequires:	desktop-file-utils
BuildRequires:	ninja
BuildRequires:	gnuradio-pmt-devel
BuildRequires:	gnuradio-utils
BuildRequires:	hicolor-icon-theme
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(fftw3f) >= 3.2
BuildRequires:	pkgconfig(gnuradio-analog)
BuildRequires:	pkgconfig(gnuradio-audio)
BuildRequires:	pkgconfig(gnuradio-blocks)
BuildRequires:	pkgconfig(gnuradio-digital)
BuildRequires:	pkgconfig(gnuradio-fft)
BuildRequires:	pkgconfig(gnuradio-filter)
BuildRequires:	pkgconfig(gnuradio-runtime)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libunwind-llvm)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6SvgWidgets)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(spdlog)
BuildRequires:	pkgconfig(volk) >= 3.2

%description
Gqrx is an open source software defined radio (SDR) receiver
implemented using GNU Radio and the Qt GUI toolkit.

Currently it works on Linux with hardware supported by gr-osmosdr,
including Funcube Dongle, RTL-SDR, Airspy, HackRF, BladeRF,
RFSpace, USRP and SoapySDR.

Gqrx can operate as an AM/FM/SSB receiver with audio output or as
an FFT-only instrument.

%prep
%autosetup -p1

%build
%cmake	\
	-DFORCE_QT6=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
# man page
install -Dpm 644 resources/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/dk.%{name}.%{name}.appdata.xml

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/dk.gqrx.gqrx.desktop
%{_datadir}/icons/hicolor/scalable/apps/gqrx.svg
%{_datadir}/metainfo/dk.gqrx.gqrx.appdata.xml
%{_mandir}/man1/%{name}.1.*

