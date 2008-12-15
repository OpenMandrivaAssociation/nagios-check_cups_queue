%define name	nagios-check_cups_queue
%define version	20060627
%define release	%mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios cups plugin
Group:		Networking/Other
License:	BSD
URL:		http://dev.lusis.org/nagios/
Source0:	http://dev.lusis.org/nagios/check_cups_queue.txt
Patch:      nagios/check_cups_queue-force-locales.patch
Requires:   cups-common
Requires:   bc
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin will check the status of a remote CUPS print queue. It will provide
the size of the queue and optionally the age of the queue

%prep
cp %{SOURCE0} check_cups_queue.txt
%patch -p0

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_cups_queue.txt %{buildroot}%{_datadir}/nagios/plugins/check_cups_queue

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_cups_queue.cfg <<'EOF'
define command{
	command_name	check_cups_queue
	command_line	%{_datadir}/nagios/plugins/check_cups_queue -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_cups_queue
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_cups_queue.cfg
