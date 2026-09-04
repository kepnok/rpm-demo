Name:           hello
Version:        0.0.0
Release:        1
Summary:        A simple hello world application

License:        GPL
BuildArch:      noarch

%description
A simple hello world application packaged as an RPM.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_sourcedir}/hello.sh %{buildroot}/usr/bin/hello

%files
/usr/bin/hello

%changelog

* Fri Sep 04 2026 CI [ci@example.com](mailto:ci@example.com) - 0.0.0-1

- Initial RPM package
