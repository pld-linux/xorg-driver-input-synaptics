Summary:	X.org input driver for Synaptics and ALPS touchpads
Summary(pl.UTF-8):	Sterownik wejściowy X.org do touchpadów Synaptics oraz ALPS
Name:		xorg-driver-input-synaptics
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
# Source0-md5:	fa002949c6b4cdd5a4f792e5dbb824f5
URL:		http://xorg.freedesktop.org/
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libpciaccess-devel
BuildRequires:	xorg-xserver-server-devel
%requires_xorg_xserver_xinput
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install fdi/11-x11-synaptics.fdi $RPM_BUILD_ROOT%{_datadir}/hal/fdi/policy/10osvendor

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/synclient
%attr(755,root,root) %{_bindir}/syndaemon
%attr(755,root,root) %{_libdir}/xorg/modules/input/synaptics_drv.so
%{_datadir}/hal/fdi/policy/10osvendor/11-x11-synaptics.fdi
%{_mandir}/man1/synclient.1*
%{_mandir}/man1/syndaemon.1*
%{_mandir}/man4/synaptics.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/synaptics*.h
%{_pkgconfigdir}/xorg-synaptics.pc
