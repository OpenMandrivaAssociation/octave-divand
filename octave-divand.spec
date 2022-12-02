%define octpkg divand

Summary:	Functions for n-dimensional variational analysis with Octave
Name:		octave-%{octpkg}
Version:	1.1.2
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
divand performs an n-dimensional variational analysis (interpolation) of
arbitrarily located observations with Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

