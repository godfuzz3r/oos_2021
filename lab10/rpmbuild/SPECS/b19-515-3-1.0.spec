Name:		b19-515-3
Version:	1.0
Release:	1%{?dist}
Summary:	Program of student Velikoivanenko, group b19-515

Group:		Testing
License:	GPL
URL:		https://github.com/godfuzz3r/oos_2021/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	/bin/sh, /usr/bin/date
BuildArch:	noarch

%description
A test package


%prep
%setup -q


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 b19-515-3 %{buildroot}%{_bindir}

%files
%{_bindir}/b19-515-3


%changelog
* Mon Jun  6 2022 Velikoivanenko
- Added %{_bindir}/b19-515-3
