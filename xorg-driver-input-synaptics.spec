Summary:	XOrg/XFree86 input driver for Synaptics and ALPS touchpads
Summary(pl.UTF-8):	Sterownik wejściowy XOrg/XFree86 do touchpadów Synaptics oraz ALPS
Name:		xorg-driver-input-synaptics
Version:	0.15.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
# Source0-md5:	939f1c831c5cd3a6f027e982592dfc5b
Source1:	11-x11-synaptics.fdi
URL:		http://xorg.freedesktop.org/
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-xserver-server-devel
%requires_xorg_xserver_xinput
Obsoletes:	X11-input-synaptics
Obsoletes:	X11-synaptics
Obsoletes:	XFree86-input-synaptics
Obsoletes:	xorg-app-synaptics
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xorg/XFree86 input driver for Synaptics touchpad.

%description -l pl.UTF-8
Sterownik wejściowy Xorg/XFree86 do touchpada Synaptics.

%prep
%setup -q -n xf86-input-synaptics-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xorg/modules/input/*.so
%{_datadir}/hal/fdi/policy/10osvendor/*.fdi
%{_mandir}/man?/*
