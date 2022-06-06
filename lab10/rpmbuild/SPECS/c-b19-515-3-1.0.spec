Name:		c-b19-515-3
Version:	1.0
Release:	1%{?dist}
Summary:	Program of student Velikoivanenko, group b19-515

Group:		Testing
License:	GPL
URL:		https://github.com/godfuzz3r/oos_2021/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc

%description
A test package


%prep
%setup -q

%build
gcc -O2 -o c-b19-515-3 c-b19-515-3.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-515-3 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/x86_64/c-b19-515-3-1.0-1.el7.x86_64.rpm --force

%files
%{_bindir}/c-b19-515-3


%changelog
* Mon Jun  6 2022 Velikoivanenko
- Added %{_bindir}/b19-515-3
