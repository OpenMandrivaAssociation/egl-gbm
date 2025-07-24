%global major 1
%define libname %mklibname nvidia-egl-gbm
%define lib32name %mklib32name nvidia-egl-gbm

%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

Name:		egl-gbm
Version:	1.1.2.1
Release:	1
Group:		System/Libraries
Summary:	GBM EGL External Platform library for nvidia GPUs
License:	MIT
URL:		https://github.com/NVIDIA/egl-gbm
Source0:	https://github.com/NVIDIA/egl-gbm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(eglexternalplatform)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(gbm)

%if %{with compat32}
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libgbm)
%endif

Requires:	%{libname} >= %{EVRD}
BuildSystem:	meson

%description
%{summary}.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
%{summary}.

%package -n %{lib32name}
Summary:	%{summary}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{lib32name}
%{summary}.

%files -n %{libname}
%license COPYING
%{_libdir}/*.so*
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so*
%endif
