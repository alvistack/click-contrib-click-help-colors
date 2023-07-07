# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-click-help-colors
Epoch: 100
Version: 0.9.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Colorization of help messages in Click
License: MIT
URL: https://github.com/click-contrib/click-help-colors/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Colorization of help messages in Click.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-click-help-colors
Summary: Colorization of help messages in Click
Requires: python3
Requires: python3-click >= 7.0
Provides: python3-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python3dist(click-help-colors) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(click-help-colors) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(click-help-colors) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-click-help-colors
Colorization of help messages in Click.

%files -n python%{python3_version_nodots}-click-help-colors
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-click-help-colors
Summary: Colorization of help messages in Click
Requires: python3
Requires: python3-click >= 7.0
Provides: python3-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python3dist(click-help-colors) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(click-help-colors) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-click-help-colors = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(click-help-colors) = %{epoch}:%{version}-%{release}

%description -n python3-click-help-colors
Colorization of help messages in Click.

%files -n python3-click-help-colors
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
