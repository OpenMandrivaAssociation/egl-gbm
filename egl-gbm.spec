%global major 1
%define libname %mklibname nvidia-egl-gbm
%define devname %mklibname -d nvidia-egl-gbm

Name:		egl-gbm
Version:	1.1.2.1
Release:	1
Group:		System/Libraries
Summary:	GBM EGL External Platform library for nvidia GPUs
License:	MIT
URL:		https://github.com/NVIDIA/egl-gbm
Source0:	https://github.com/NVIDIA/egl-gbm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(eglexternalplatform) >= 1.0
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(wayland-server) >= 1.15.0
BuildRequires:	pkgconfig(wayland-client) >= 1.15.0
BuildRequires:	pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:	pkgconfig(wayland-protocols)
Requires:	%{libname} >= %{EVRD}
BuildSystem:	meson

%description
%{summary}.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name}

%description -n %{libname}
%{summary}.

%package -n %{devname}
Summary:	Nvidia GBM EGL External Platform library development package
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Nvidia GBM EGL External Platform library development package.

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.%{major}*
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%files -n %{devname}
%{_libdir}/libnvidia-egl-gbm.so
