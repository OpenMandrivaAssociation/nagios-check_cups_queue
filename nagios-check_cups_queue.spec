%define name	nagios-check_cups_queue
%define version	20060627
%define release	13

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20060627-12mdv2011.0
+ Revision: 620432
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 20060627-11mdv2010.0
+ Revision: 440199
- rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-10mdv2009.1
+ Revision: 314634
- now a noarch package

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 20060627-9mdv2009.0
+ Revision: 253530
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060627-8mdv2009.0
+ Revision: 239729
- rebuild

* Wed Mar 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-6mdv2008.1
+ Revision: 179441
- force Unix locales for extracting dates

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-5mdv2008.1
+ Revision: 168928
- fix configuration (thanks oden)

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-4mdv2008.1
+ Revision: 168911
- add a configuration file

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-3mdv2008.1
+ Revision: 168798
- not a noarch package, as nagios plugins installation directory is arch-dependant

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-2mdv2008.1
+ Revision: 162717
- fix dependencies

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-1mdv2008.1
+ Revision: 162716
- import nagios-check_cups_queue


* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20060627-1mdv2008.1
- first mandriva package
