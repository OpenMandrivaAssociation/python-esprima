Name:		python-esprima
Version:	4.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/e/esprima/esprima-%{version}.tar.gz
Summary:	ECMAScript parsing infrastructure for multipurpose analysis in Python
URL:		https://pypi.org/project/esprima/
License:	BSD License
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
ECMAScript parsing infrastructure for multipurpose analysis in Python

%files
%{_bindir}/esprima
%{py_sitedir}/esprima
%{py_sitedir}/esprima-*.*-info
