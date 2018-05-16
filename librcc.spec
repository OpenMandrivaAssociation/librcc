%define major 0
%define libname %mklibname rcc %{major}
%define libnameui %mklibname rccui %{major}
%define devname %mklibname rcc -d

Summary:	Russian Charset Conversion Library
Name:		librcc
Version:	0.2.12
Release:	4
Url:		http://rusxmms.sourceforge.net/
Source0:	http://darksoft.org/files/rusxmms/%{name}-%{version}.tar.bz2
Group:		System/Libraries
License:	LGPLv2.1+
BuildRequires:	aspell-devel
BuildRequires:	librcd-devel
BuildRequires:	pkgconfig(libxml-2.0)
# In fact, is not used now because it's not properly detected
BuildRequires:	pkgconfig(libguess)

%description
Library providing means to work with multiple encodings of the same language
through adapting them to local settings on-the-fly.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Russian Charset Conversion Library
Group:		System/Libraries
Obsoletes:	%{libnameui}

%description -n %{libname}
Library providing means to work with multiple encodings of the same language
through adapting them to local settings on-the-fly.

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_libdir}/rcc/

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Russian Charset Conversion Library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Library providing means to work with multiple encodings of the same language
through adapting them to local settings on-the-fly.

This package contains files required for development only.

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README ToDo
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/librcc.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
