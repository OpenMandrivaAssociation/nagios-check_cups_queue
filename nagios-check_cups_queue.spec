%define name	nagios-check_cups_queue
%define version	20060627
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios cups plugin
Group:		Networking/Other
License:	BSD
URL:		http://dev.lusis.org/nagios/
Source0:	http://dev.lusis.org/nagios/check_cups_queue.txt
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin will check the status of a remote CUPS print queue. It will provide
the size of the queue and optionally the age of the queue

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins/check_cups_queue

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_cups_queue

