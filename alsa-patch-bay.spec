# Conditional build:
# _with_fltk		enable fltk UI
# _without_gtkmm	disable gtkmm UI
#
# TODO:
# - PL translations - I have absolutely no idea for it :/
#   but for now it works as it should...
#
Summary:	A GUI patchbay for ALSA and JACK.
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
BuildRequires:	libtool
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	pkgconfig
%{!?_without_gtkmm:BuildRequires:	gtkmm-devel}
%{?_with_fltk:BuildRequires:	fltk-devel}
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA Patch Bay is a GUI patchbay for the ALSA seq sequencer api and
the JACK audio API. It can use FLTK 1.1 or GTKmm 2.0.0.

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
%{_datadir}/applications/*.desktop
%attr(755,root,root) %{_libdir}/%{name}/driver/*.so
%attr(755,root,root) %{_libdir}/%{name}/ui/*.so
%{_pixmapsdir}/*.png
