Summary:	X.org input driver for Synaptics and ALPS touchpads
Summary(pl.UTF-8):	Sterownik wejściowy X.org do touchpadów Synaptics oraz ALPS
Name:		xorg-driver-input-synaptics
Version:	1.5.99.902
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
# Source0-md5:	3e57a18839aad7e8633e19afdabd6b49
URL:		http://xorg.freedesktop.org/
BuildRequires:	mtdev-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libXi-devel >= 1.2
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.1
BuildRequires:	xorg-proto-inputproto-devel >= 2.1.99.3
BuildRequires:	xorg-util-util-macros >= 1.13
BuildRequires:	xorg-xserver-server-devel >= 1.11.99.901
Requires:	xorg-lib-libXi >= 1.2
Requires:	xorg-lib-libXtst >= 1.0.99.1
Requires:	xorg-xserver-server >= 1.11.99.901
%{?requires_xorg_xserver_xinput}
Obsoletes:	X11-input-synaptics
Obsoletes:	X11-synaptics
Obsoletes:	XFree86-input-synaptics
Obsoletes:	xorg-app-synaptics
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Synaptics touchpads.

%description -l pl.UTF-8
Sterownik wejściowy X.org do touchpadów Synaptics.

%package devel
Summary:	Header file for synaptics driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika synaptics
Group:		Development/Libraries

%description devel
Header file for synaptics driver.

%description devel -l pl.UTF-8
Plik nagłówkowy sterownika synaptics.

%prep
%setup -q -n xf86-input-synaptics-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/synclient
%attr(755,root,root) %{_bindir}/syndaemon
%attr(755,root,root) %{_libdir}/xorg/modules/input/synaptics_drv.so
%{_datadir}/X11/xorg.conf.d/50-synaptics.conf
%{_mandir}/man1/synclient.1*
%{_mandir}/man1/syndaemon.1*
%{_mandir}/man4/synaptics.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_pkgconfigdir}/xorg-synaptics.pc
