%define		_ver  44
Summary:	Download file manager (official core)
Summary(pl):	¦ci±gacz plików (oficialny)
Name:		overnet
Version:	0.%{_ver}
Release:	1
Epoch:		1
License:	unknown
Group:		Applications/Communications
Source0:	http://www.overnet.com/files/%{name}%{version}.tar.gz
Source1:	%{name}.sh
URL:		http://www.overnet.com/
Provides:	eDonkey-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Download file manager hosted by http://www.overnet.com/
Overnet is the serverless successor of eDonkey2000, 
and both programs are very similar in many respects.

%description -l pl
¦ci±gacz plików z http://www.overnet.com/
Jest podobny do eDonkey2000 lecz nie u¿ywa serwerów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install overnet_s_%{_ver} $RPM_BUILD_ROOT%{_bindir}/overnet_s_v%{_ver}

ln -s %{_bindir}/overnet_s_v%{_ver} $RPM_BUILD_ROOT%{_bindir}/overnet

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/overnet-conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
