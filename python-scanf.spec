
%define		module	scanf

Summary:	The C-scanf-like string parsing in pure Python
Summary(pl):	Parser ci±gów znaków w sk³adni scanf napisany w czystym Pythonie
Name:		python-%{module}
Version:	1.0
Release:	1
License:	unknown
Group:		Libraries/Python
Source0:	http://hkn.eecs.berkeley.edu/~dyoo/python/scanf/%{module}-%{version}.tar.gz
# Source0-md5:	a617ca749a40c8f76dd98fc7b91a577d
URL:		http://hkn.eecs.berkeley.edu/~dyoo/python/scanf/
BuildRequires:	python >= 1:2.3
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scanf provides formatted input from standard input, strings, or files,
using a format-string syntax that's similar to C's scanf(). The syntax
should be familiar to C programmers, and offers very simple pattern
matching against strings and files.

%description -l pl
scanf jest modu³em Pythona umo¿liwiaj±cym wczytywanie danych ze
standardowego wej¶cia, ci±gów znaków lub plików, u¿ywaj±c ci±gów
formatuj±cych zgodnych ze znan± z jêzyka C funkcj± scanf().

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}.py[oc]
