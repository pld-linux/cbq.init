Summary:	Shell script for setting up CBQ
Summary(pl):	Skrypt umo¿liwiaj±cy prost± konfiguracjê CBQ
Name:		cbq.init
Version:	0.7.2
Release:	0.1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/cbqinit/%{name}-v%{version}
# Source0-md5:	f58368ae779f32acbbf1aeaa4e28b4c5
URL:		http://www.sourceforge.net/projects/cbqinit/
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/sysconfig/cbq}

install %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

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
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%dir /etc/sysconfig/cbq
