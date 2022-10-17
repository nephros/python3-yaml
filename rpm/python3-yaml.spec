%bcond_with docs

Name:       python3-yaml
Summary:    YAML parser and emitter for Python
Version:    5.4.1.1
Release:    1
License:    MIT
URL:        http://pyyaml.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# do not use internal yaml implementation
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  python3dist(cython)
Provides:       PyYAML

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that allow
to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%if %{with docs}
%package doc
Summary: Documentation and examples for %{name}
Requires: %{name}-%{version}
BuildArch: noarch

%description doc
%{summary}.
%endif

%prep
%setup -q -n %{name}-%{version}/pyyaml

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install
%if 0%{!with docs}
rm -rf %{buildroot}/%{_docdir}
%endif

%files
%defattr(-,root,root,-)
%license LICENSE
%{python3_sitearch}/*

%if 0%{with docs}
%files doc
%defattr(-,root,root,-)
%doc README examples
%endif
