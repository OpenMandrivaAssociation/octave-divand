%global octpkg divand

Summary:	Functions for n-dimensional variational analysis with Octave
Name:		octave-divand
Version:	1.1.2
Release:	3
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/divand/
Source0:	https://downloads.sourceforge.net/octave/divand-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Performs an n-dimensional variational analysis (interpolation) of
arbitrarily located observations.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

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

