Summary: Generic Security Services Application Programming Interface Library
Name: libgssglue
Version: 0.1
Release: 8.1%{?dist}
URL: http://www.citi.umich.edu/projects/nfsv4/linux/
License: GPL+
Source0:http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: krb5-libs >= 1.5

Provides: libgssapi = %{version}-%{release}
Provides: libgssapi-devel = %{version}-%{release}
Obsoletes: libgssapi <= 0.11 libgssapi-devel <= 0.11

Patch0: libgssglue-0.1-gssglue.patch

%description
This library exports a gssapi interface, but doesn't implement any gssapi
mechanisms itself; instead it calls gssapi routines in other libraries,
depending on the mechanism.

%package devel
Summary: Development files for the gssclug library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package includes header files and libraries necessary for
developing programs which use the gssapi library.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags} all 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}
make DESTDIR=%{buildroot} install
install -p -m 644 doc/gssapi_mech.conf %{buildroot}/%{_sysconfdir}/gssapi_mech.conf
rm -f %{buildroot}/%{_libdir}/*.a %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgssglue.so.*
%config(noreplace) %{_sysconfdir}/gssapi_mech.conf

%files devel
%defattr(0644,root,root,755)
%{_libdir}/libgssglue.so
%dir %{_includedir}/gssglue
%dir %{_includedir}/gssglue/gssapi
%{_includedir}/gssglue/gssapi/gssapi.h
%{_libdir}/pkgconfig/libgssglue.pc

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 27 2008 Steve Dickson <steved@redhat.com> 0.1-6
- Changed gssapi_mech.conf to use libgssapi_krb5.so.2 
  instead of libgssapi_krb5.so (bz 447503)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1-5
- Autorebuild for GCC 4.3

* Wed Oct 17 2007 Steve Dickson <steved@redhat.com> 0.1-4
- updated Obsoletes: (0.1-3)
- Obsolete -devel package

* Mon Sep 17 2007 Steve Dickson <steved@redhat.com> 0.1-2
- RPM review

* Tue Sep 11 2007 Steve Dickson <steved@redhat.com>
- Initial commit
