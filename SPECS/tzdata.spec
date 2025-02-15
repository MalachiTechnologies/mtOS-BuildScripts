Summary:	Time zone data
Name:		tzdata
Version:	2015a
Release:	1
URL:		http://www.iana.org/time-zones
License:	GPLv3
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source1:	http://www.iana.org//time-zones/repository/releases/%{name}%{version}.tar.gz
BuildArch:	noarch
%description
Sources for time zone and daylight saving time data
%define blddir		%{name}-%{version}
%prep
rm -rf %{blddir}
install -vdm 755 %{blddir}
cd %{blddir}
tar xf %{SOURCE1}
%build
%install
cd %{blddir}
ZONEINFO=%{buildroot}%{_datarootdir}/zoneinfo
install -vdm 755 $ZONEINFO/{posix,right}
for tz in etcetera southamerica northamerica europe africa antarctica  \
	asia australasia backward pacificnew systemv; do
	zic -L /dev/null	-d $ZONEINFO		-y "sh yearistype.sh" ${tz}
	zic -L /dev/null	-d $ZONEINFO/posix	-y "sh yearistype.sh" ${tz}
	zic -L leapseconds	-d $ZONEINFO/right	-y "sh yearistype.sh" ${tz}
done
cp -v zone.tab iso3166.tab $ZONEINFO
zic -d $ZONEINFO -p America/New_York
install -vdm 755 %{buildroot}%{_sysconfdir}
install -vm 555 %{buildroot}/%{_datarootdir}/zoneinfo/America/New_York %{buildroot}%{_sysconfdir}/localtime
%files
%defattr(-,root,root)
%{_sysconfdir}/localtime
%{_datadir}/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2015a-1
*	Sat Mar 22 2014 baho-utot <baho-utot@columbus.rr.com> 2013i-1
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 2013d-1
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 2013c-1
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2013b-1
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2012j-1
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2012e-1
