#
# Conditional build:
# _without_fltk		- without FLTK UI
# _without_gtkmm	- without gtkmm UI
#
Summary:	A GUI patchbay for ALSA and JACK
Summary(pl):	Graficzny interfejs do zbioru patchy d¼wiêkowych dla ALSY i JACKa
Name:		alsa-patch-bay
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
# Source0-md5:	f1addf00d950ba03f0e6eb7c90b83dd4
Patch0:		%{name}-Makefile.patch
URL:		http://pkl.net/~node/alsa-patch-bay.html
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_fltk:BuildRequires:	fltk-devel >= 1.1}
%{!?_without_gtkmm:BuildRequires:	gtkmm-devel >= 2.0.0}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladcca-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA Patch Bay is a GUI patchbay for the ALSA sequencer api and
the JACK audio API. It can use FLTK 1.1 or GTKmm 2.0.

%description -l pl
ALSA Patch Bay to graficzny interfejs do zbioru patchy d¼wiêkowych dla
API sequencera ALSY oraz API d¼wiêkowego JACK. Mo¿e u¿ywaæ FLTK 1.1
lub GTKmm 2.0.

%package driver-alsa
Summary:	ALSA audio driver for ALSA Patch Bay
Summary(pl):	Sterownik d¼wiêku ALSA dla ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name}-%{version}

%description driver-alsa
ALSA audio driver for ALSA Patch Bay.

%description driver-alsa -l pl
Sterownik d¼wiêku ALSA dla ALSA Patch Bay.

%package driver-jack
Summary:	JACK audio driver for ALSA Patch Bay
Summary(pl):	Sterownik d¼wiêku JACK dla ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name}-%{version}

%description driver-jack
JACK audio driver for ALSA Patch Bay.

%description driver-jack -l pl
Sterownik d¼wiêku JACK dla ALSA Patch Bay.

%package ui-fltk
Summary:	FLTK-based GUI for ALSA Patch Bay
Summary(pl):	Oparte na FLTK GUI do ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name}-%{version}

%description ui-fltk
FLTK-based graphical user interface for ALSA Patch Bay.

%description ui-fltk -l pl
Oparty na FLTK graficzny interfejs u¿ytkownika do ALSA Patch Bay.

%package ui-gtkmm
Summary:	GTKmm-based GUI for ALSA Patch Bay
Summary(pl):	Oparte na GTKmm GUI do ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name}-%{version}

%description ui-gtkmm
GTKmm-based GUI for ALSA Patch Bay.

%description ui-gtkmm -l pl
Oparte na GTKmm GUI do ALSA Patch Bay.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?_without_fltk:--disable-fltk --disable-fltk-test} \
	%{?_without_gtkmm:--disable-gtkmm}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/driver
%dir %{_libdir}/%{name}/ui
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files driver-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/driver/alsa.so

%files driver-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/driver/jack.so

%files ui-fltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ui/fltk.so

%files ui-gtkmm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ui/gtkmm.so
