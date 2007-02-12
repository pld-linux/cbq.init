Summary:	Shell script for setting up CBQ
Summary(pl.UTF-8):	Skrypt umożliwiający prostą konfigurację CBQ
Name:		cbq.init
Version:	0.7.3
Release:	0.1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/cbqinit/%{name}-v%{version}
# Source0-md5:	c319f136059aadf7b3f0a38a12f3f3e0
URL:		http://www.sourceforge.net/projects/cbqinit/
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	iproute2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CBQ.init is a simple shell script for setting up a smart ethernet
shaper based on CBQ (Class Based Queueing) for Linux 2.2 and 2.4.

%description -l pl.UTF-8
CBQ.init jest prostym skryptem umożliwiającym konfigurację CBQ w
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
