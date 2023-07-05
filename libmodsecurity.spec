Summary:	A library that loads/interprets rules written in the ModSecurity SecRules
Name:		libmodsecurity
Version:	3.0.9
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
# Source0-md5:	17f78ea7c2cff1be1f570f38ae6f7a30
URL:		https://www.modsecurity.org/
BuildRequires:	GeoIP-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libmaxminddb-devel
BuildRequires:	libxml2-devel
BuildRequires:	lua54-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	ssdeep-devel
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmodsecurity is one component of the ModSecurity v3 project. The
library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content
provided by your application via Connectors.

%package devel
Summary:	Header files and develpment documentation for libmodsecurity
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Libraries and header files for developing applications that use
libmodsecurity.

%package static
Summary:	Static libmodsecurity library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the static library used for development.

%prep
%setup -q -n modsecurity-v%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
		--with-lua=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README.md SECURITY.md
%attr(755,root,root) %{_bindir}/modsec-rules-check
%attr(755,root,root) %{_libdir}/libmodsecurity.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmodsecurity.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmodsecurity.la
%attr(755,root,root) %{_libdir}/libmodsecurity.so
%{_includedir}/modsecurity
%{_pkgconfigdir}/modsecurity.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmodsecurity.a
