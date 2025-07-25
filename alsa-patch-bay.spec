#
# Conditional build:
%bcond_without	fltk	# without FLTK UI
%bcond_without	gtkmm	# without gtkmm UI
%bcond_without	ladcca	# with ladcca support
#
Summary:	Graphical patch bay for the ALSA sequencer and JACK
Summary(pl.UTF-8):	Graficzny interfejs dla sekwencera ALSY i JACK-a
Name:		alsa-patch-bay
Version:	1.0.0
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://pkl.net/~node/software/alsa-patch-bay/%{name}-%{version}.tar.gz
# Source0-md5:	3aa458f6bee8b83b2cf7330707d72430
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop_pl.patch
Patch2:		%{name}-missing_m4.patch
Patch3:		%{name}-pic.patch
Patch4:		%{name}-make-jN.patch
Patch5:		%{name}-ac.patch
URL:		http://pkl.net/~node/software/alsa-patch-bay/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_fltk:BuildRequires:	fltk-devel >= 1.1}
%{?with_gtkmm:BuildRequires:	gtkmm22-devel}
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
%{?with_ladcca:BuildRequires:	ladcca-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-ui = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA Patch Bay is a GUI patchbay for the ALSA sequencer and
the JACK audio subsystems. In easy way connects ports of MIDI and
audio devices like sequencer, external keyboard, soft synth and
many others.

%description -l pl.UTF-8
ALSA Patch Bay to graficzny interfejs dla podsystemów sequencera
ALSY oraz dźwiękowego JACK-a. W łatwy sposób łączy porty urządzeń
MIDI i audio jak sekwencer, zewnętrzne klawisze, synteza programowa
i wiele innych.

%package driver-alsa
Summary:	ALSA audio driver for ALSA Patch Bay
Summary(pl.UTF-8):	Sterownik dźwięku ALSA dla ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}

%description driver-alsa
ALSA audio driver for ALSA Patch Bay.

%description driver-alsa -l pl.UTF-8
Sterownik dźwięku ALSA dla ALSA Patch Bay.

%package driver-jack
Summary:	JACK audio driver for ALSA Patch Bay
Summary(pl.UTF-8):	Sterownik dźwięku JACK-a dla ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-driver-alsa = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Provides:	jack-patch-bay

%description driver-jack
JACK audio driver for ALSA Patch Bay.

%description driver-jack -l pl.UTF-8
Sterownik dźwięku JACK-a dla ALSA Patch Bay.

%package ui-fltk
Summary:	FLTK-based GUI for ALSA Patch Bay
Summary(pl.UTF-8):	Oparte na FLTK GUI do ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-ui = %{version}-%{release}

%description ui-fltk
FLTK-based graphical user interface for ALSA Patch Bay.

%description ui-fltk -l pl.UTF-8
Oparty na FLTK graficzny interfejs użytkownika do ALSA Patch Bay.

%package ui-gtkmm
Summary:	GTKmm-based GUI for ALSA Patch Bay
Summary(pl.UTF-8):	Oparte na GTKmm GUI do ALSA Patch Bay
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm22
Provides:	%{name}-ui = %{version}-%{release}

%description ui-gtkmm
GTKmm-based GUI for ALSA Patch Bay.

%description ui-gtkmm -l pl.UTF-8
Oparte na GTKmm GUI do ALSA Patch Bay.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_fltk:--disable-fltk --disable-fltk-test} \
	%{!?with_gtkmm:--disable-gtkmm} \
	%{!?with_ladcca:--disable-ladcca} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf alsa-patch-bay $RPM_BUILD_ROOT%{_bindir}/jack-patch-bay

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/ui/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/driver
%dir %{_libdir}/%{name}/ui
%{_pixmapsdir}/*.png

%files driver-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/alsa-patch-bay
%attr(755,root,root) %{_libdir}/%{name}/driver/alsa.so
%{_desktopdir}/alsa-patch-bay.desktop

%files driver-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack-patch-bay
%attr(755,root,root) %{_libdir}/%{name}/driver/jack.so
%{_desktopdir}/jack-patch-bay.desktop

%if %{with fltk}
%files ui-fltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ui/fltk.so
%endif

%if %{with gtkmm}
%files ui-gtkmm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/ui/gtkmm.so
%endif
