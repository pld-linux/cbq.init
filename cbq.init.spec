Summary:	Shell script for setting up CBQ
Summary(pl):	Skrypt umo¿liwiaj±cy prost± konfiguracjê CBQ
Name:		cbq.init
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://ftp.lj.pl/pub/linux/%{name}-%{version}.tar.gz
URL:		ftp://ftp.equinox.gu.net/pub/linux/cbq/
Requires:	iproute2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
CBQ.init is a simple shell script for setting up a smart ethernet
shaper based on CBQ (Class Based Queueing) for Linux 2.2 and 2.4.

%description -l pl
CBQ.init jest prostym skryptem umo¿liwiaj±cym konfiguracjê CBQ w
Linuksie 2.2 i 2.4.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/rc.d/init.d,%{_sysconfdir}/sysconfig/cbq}

install %{name}-v%{version} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add cbq.init

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del cbq.init
fi
	
%files
%defattr(644,root,root,755)
%doc README.gz doc/*
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/sysconfig/cbq
