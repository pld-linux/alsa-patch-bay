#
# Conditional build:
# _with_fltk		enable fltk UI
# _without_gtkmm	disable gtkmm UI
#
Summary:	A GUI patchbay for ALSA and JACK
Summary(pl):	Graficzny interfejs do zbioru patchy d¼wiêkowych dla ALSY i JACKa
Name:		alsa-patch-bay
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://pkl.net/~node/alsa-patch-bay.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?_with_fltk:BuildRequires:	fltk-devel >= 1.1}
%{!?_without_gtkmm:BuildRequires:	gtkmm-devel >= 2.0.0}
BuildRequires:	jack-audio-connection-kit-devel
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

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%if %{?_with_fltk:0}%{!?_with_fltk:1}
	--disable-fltk \
	--disable-fltk-test \
%endif
%{?_without_gtkmm:--disable-gtkmm}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/driver
%attr(755,root,root) %{_libdir}/%{name}/driver/*.so
%dir %{_libdir}/%{name}/ui
%attr(755,root,root) %{_libdir}/%{name}/ui/*.so
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
