Summary:	Animated plasma wallpaper
Name:		plasma-wallpaper-dreamdesktop
Version:	0.3.0
Release:	3
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.jarzebski.pl/projekty/dreamdesktop.html
Source0:	http://www.jarzebski.pl/dreamdesktop/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel

%description
DreamDesktop is an animated wallpaper for KDE 4 environment.

Animation can be any video output from FFMPEG. Beautiful animations
can be found at: http://www.dreamscene.org/

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%{_kde_libdir}/kde4/dreamdesktop.so
%{_kde_appsdir}/dreamdesktop
%{_kde_services}/dreamdesktop.desktop

