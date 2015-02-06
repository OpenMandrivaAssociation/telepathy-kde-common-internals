%define srcname ktp-common-internals
%define major 3
%define version_lib 0.5

Name:		telepathy-kde-common-internals
Version:	%{version_lib}.1
Release:	3
Summary:	KDE Telepathy Parts
Group:		System/Libraries
License:	LGPLv2
URL:		https://projects.kde.org/projects/extragear/network/telepathy/ktp-common-internals
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/kde-telepathy/%version/src/%srcname-%version.tar.bz2
BuildRequires:	pkgconfig(TelepathyQt4) >= 0.9.2.1
BuildRequires:	kdelibs4-devel

%description
This package provides the commons part used by telepathy kde.


#------------------------------------------------------------------------------
%package core
Summary:	Commons files used by telepathy kde
Group:		Graphical desktop/KDE 
BuildArch:	noarch
Obsoletes:	%{name}-translations < 0.5.0
Conflicts:	%{name} < 0.5.0
Obsoletes:	%{name} < 0.5.0
Conflicts:	telepathy-kde-contact-list < 0.4.0

%description core
Commons files used by telepathy kde.

%files  core -f ktp-common-internals.lang
%{_kde_iconsdir}/hicolor/*/*/*.png
%{_kde_appsdir}/ktelepathy/ktelepathy.notifyrc
%{_kde_iconsdir}/hicolor/scalable/apps/telepathy-kde.svgz

#------------------------------------------------------------------------------

%define libktpmodelsprivate %mklibname ktpmodelsprivate %{major}

%package -n %{libktpmodelsprivate}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libktpmodelsprivate}
Runtime library for %{name}.

%files -n %{libktpmodelsprivate}
%{_kde_libdir}/libktpmodelsprivate.so.%{major}
%{_kde_libdir}/libktpmodelsprivate.so.%{version_lib}*

#------------------------------------------------------------------------------

%define libktpcommoninternalsprivate %mklibname ktpcommoninternalsprivate %{major}

%package -n %{libktpcommoninternalsprivate}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libktpcommoninternalsprivate}
Runtime library for %{name}.

%files -n %{libktpcommoninternalsprivate}
%{_kde_libdir}/libktpcommoninternalsprivate.so.%{major}
%{_kde_libdir}/libktpcommoninternalsprivate.so.%{version_lib}*

#------------------------------------------------------------------------------

%define libktpwidgetsprivate %mklibname ktpwidgetsprivate %{major}

%package -n %{libktpwidgetsprivate}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libktpwidgetsprivate}
Runtime library for %{name}.

%files -n %{libktpwidgetsprivate}
%{_kde_libdir}/libktpwidgetsprivate.so.%{major}
%{_kde_libdir}/libktpwidgetsprivate.so.%{version_lib}*

#------------------------------------------------------------------------------

%define devel %mklibname %{name} -d

%package -n %{devel}
Summary:	Headers files for %{name}
Group:		Development/KDE and Qt 
Provides:	%name-devel = %version-%release
Provides:	lib%{name}-devel = %version-%release
Requires:	%{libktpmodelsprivate} = %version-%release
Requires:	%{libktpcommoninternalsprivate} = %version-%release
Requires:	%{libktpwidgetsprivate} = %version-%release
Provides:	%{srcname}-devel = %version-%release

%description -n %{devel}
Headers files for %{name}.

%files -n %{devel}
%{_kde_includedir}/KTp/
%{_kde_libdir}/libktpmodelsprivate.so
%{_kde_libdir}/libktpcommoninternalsprivate.so
%{_kde_libdir}/libktpwidgetsprivate.so
%{_kde_bindir}/ktp-debugger

#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
export LD=/usr/bin/ld.gold
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON
%make

%install
%makeinstall_std -C build
%find_lang ktp-common-internals 
