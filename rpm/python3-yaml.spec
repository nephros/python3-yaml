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
BuildRequires:  pkgconfig(yaml-0.1) >= 0.2.0
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

%prep
%setup -q -n %{name}-%{version}/pyyaml

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README examples
%{python3_sitearch}/*
