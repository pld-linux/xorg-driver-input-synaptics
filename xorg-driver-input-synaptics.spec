Summary:	X.org input driver for Synaptics and ALPS touchpads
Summary(pl.UTF-8):	Sterownik wejściowy X.org do touchpadów Synaptics oraz ALPS
Name:		xorg-driver-input-synaptics
Version:	1.10.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/archive/individual/driver/xf86-input-synaptics-%{version}.tar.xz
# Source0-md5:	017383c13a0d0f4cb320be477ab25513
Patch0:		restore-shm1.patch
Patch1:		restore-shm2.patch
Patch2:		more-fingers.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libevdev-devel >= 1.2
BuildRequires:	libtool >= 2:2
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXi-devel >= 1.2
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.1
BuildRequires:	xorg-proto-inputproto-devel >= 2.1.99.3
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.13
BuildRequires:	xorg-xserver-server-devel >= 1.18
BuildRequires:	xz
Requires:	xorg-lib-libXi >= 1.2
Requires:	xorg-lib-libXtst >= 1.0.99.1
Requires:	xorg-xserver-server >= 1.18
%{?requires_xorg_xserver_xinput}
Obsoletes:	X11-input-synaptics < 0.15
Obsoletes:	X11-synaptics < 0.15
Obsoletes:	XFree86-input-synaptics < 0.15
Obsoletes:	xorg-app-synaptics < 0.15
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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/synclient
%attr(755,root,root) %{_bindir}/syndaemon
%attr(755,root,root) %{_libdir}/xorg/modules/input/synaptics_drv.so
%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
%{_mandir}/man1/synclient.1*
%{_mandir}/man1/syndaemon.1*
%{_mandir}/man4/synaptics.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_pkgconfigdir}/xorg-synaptics.pc
