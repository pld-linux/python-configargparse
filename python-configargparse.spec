%define		module ConfigArgParse
Summary:	A Python module with support for argparse, config files, and env variables
Name:		python-configargparse
Version:	0.13.0
Release:	9
License:	MIT
Source0:	https://pypi.python.org/packages/source/C/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6d3427dce78a17fb48222538f579bdb8
Group:		Libraries/Python
URL:		https://github.com/bw2/ConfigArgParse
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applications with more than a handful of user-settable options are
best configured through a combination of command line args, config
files, hard coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very
limited support for config files and environment variables, so this
module extends argparse to add these features.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/configargparse.py[co]
%{py_sitescriptdir}/%{module}*.egg-info
