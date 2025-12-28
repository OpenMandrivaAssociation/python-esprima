Name:		python-esprima
Version:	4.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/e/esprima/esprima-%{version}.tar.gz
Summary:	ECMAScript parsing infrastructure for multipurpose analysis in Python
URL:		https://pypi.org/project/esprima/
License:	BSD License
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
ECMAScript parsing infrastructure for multipurpose analysis in Python

%files
%{_bindir}/esprima
%{py_sitedir}/esprima
%{py_sitedir}/esprima-*.*-info
