
%define		module	scanf

Summary:	The C-scanf-like string parsing in pure Python
Summary(pl.UTF-8):	Parser ciągów znaków w składni scanf napisany w czystym Pythonie
Name:		python-%{module}
Version:	1.2
Release:	3
License:	unknown
Group:		Libraries/Python
Source0:	http://hkn.eecs.berkeley.edu/~dyoo/python/scanf/%{module}-%{version}.tar.gz
# Source0-md5:	e4c3ff4629933d5ec854743bf77017ca
URL:		http://hkn.eecs.berkeley.edu/~dyoo/python/scanf/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scanf provides formatted input from standard input, strings, or files,
using a format-string syntax that's similar to C's scanf(). The syntax
should be familiar to C programmers, and offers very simple pattern
matching against strings and files.

%description -l pl.UTF-8
scanf jest modułem Pythona umożliwiającym wczytywanie danych ze
standardowego wejścia, ciągów znaków lub plików, używając ciągów
formatujących zgodnych ze znaną z języka C funkcją scanf().

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir}}

%py_install \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}.py[oc]
