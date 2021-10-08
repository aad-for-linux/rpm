%global debug_package ${nil}

Name:           aad-auth
Version:        0.0.1
Release:        0
Summary:        Bundles pam_aad, libnss_aad and dependencies

Group:          System Environment/Base
License:        GPLv3+
URL:            https://github.com/CyberNinjas
Source0:        aad-auth-0.0.1.tar.gz

BuildArch: x86_64
Requires: jansson libcurl libuuid openssl
Provides: libcjson libjwt libsds libsodium

%description
See Package Summary.

%prep
%setup -qD
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc
install -m 0755 -d $RPM_BUILD_ROOT/lib64
install -m 0755 -d $RPM_BUILD_ROOT/lib64/security
install -m 0755 libcjson.so.1.7.10 $RPM_BUILD_ROOT/lib64/libcjson.so.1.7.10
install -m 0755 libjwt.so.0.5.1 $RPM_BUILD_ROOT/lib64/libjwt.so.0.5.1
install -m 0755 libsds.so.2.0.0 $RPM_BUILD_ROOT/lib64/libsds.so.2.0.0
install -m 0755 libsodium.so.23.2.0 $RPM_BUILD_ROOT/lib64/libsodium.so.23.2.0
install -m 0644 pam_aad.conf $RPM_BUILD_ROOT/etc/pam_aad.conf
install -m 0755 pam_aad.so $RPM_BUILD_ROOT/lib64/security/pam_aad.so
install -m 0644 libnss-aad.conf $RPM_BUILD_ROOT/etc/libnss-aad.conf
install -m 0755 libnss_aad.so.2 $RPM_BUILD_ROOT/lib64/libnss_aad.so.2

%post
ln -s /lib64/libcjson.so.1.7.10 /lib64/libcjson.so
ln -s /lib64/libcjson.so.1.7.10 /lib64/libcjson.so.1
ln -s /lib64/libjwt.so.0.5.1 /lib64/libjwt.so
ln -s /lib64/libjwt.so.0.5.1 /lib64/libjwt.so.0
ln -s /lib64/libsds.so.2.0.0 /lib64/libsds.so
ln -s /lib64/libsds.so.2.0.0 /lib64/libsds.so.2
ln -s /lib64/libsodium.so.23.2.0 /lib64/libsodium.so
ln -s /lib64/libsodium.so.23.2.0 /lib64/libsodium.so.23

%files
/lib64/libcjson.so.1.7.10
/lib64/libjwt.so.0.5.1
/lib64/libsds.so.2.0.0
/lib64/libsodium.so.23.2.0
/etc/pam_aad.conf
/lib64/security/pam_aad.so
/etc/libnss-aad.conf
/lib64/libnss_aad.so.2

%changelog
* Mon Apr 22 2019 Lucas Ramage 0.0.1
  - Initial rpm release
