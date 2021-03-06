#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-incremental
Version  : 21.3.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/4f/c5/430765c697afc217c8491785de321a21fa4d983dda14bcd82feb965b0593/incremental-21.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4f/c5/430765c697afc217c8491785de321a21fa4d983dda14bcd82feb965b0593/incremental-21.3.0.tar.gz
Summary  : A small library that versions your Python projects.
Group    : Development/Tools
License  : MIT
Requires: pypi-incremental-license = %{version}-%{release}
Requires: pypi-incremental-python = %{version}-%{release}
Requires: pypi-incremental-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
===========
        
        |travis|
        |pypi|
        |coverage|
        
        Incremental is a small library that versions your Python projects.

%package license
Summary: license components for the pypi-incremental package.
Group: Default

%description license
license components for the pypi-incremental package.


%package python
Summary: python components for the pypi-incremental package.
Group: Default
Requires: pypi-incremental-python3 = %{version}-%{release}

%description python
python components for the pypi-incremental package.


%package python3
Summary: python3 components for the pypi-incremental package.
Group: Default
Requires: python3-core
Provides: pypi(incremental)

%description python3
python3 components for the pypi-incremental package.


%prep
%setup -q -n incremental-21.3.0
cd %{_builddir}/incremental-21.3.0
pushd ..
cp -a incremental-21.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656604746
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-incremental
cp %{_builddir}/incremental-21.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-incremental/e44181fdc1f061e9214ce18615a8e3b2a74593df
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-incremental/e44181fdc1f061e9214ce18615a8e3b2a74593df

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
