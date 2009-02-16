Name:           pidgin-facebookchat
Version:        1.47
Release:        %mkrel 1
Summary:        Libpurple plug-in supporting facebook IM
Group:          Networking/Instant messaging
License:        GPLv3+
URL:            http://code.google.com/p/pidgin-facebookchat/
Source0: http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-source-%{version}.tar.bz2
Source3:        %{name}-Makefile
Provides:       pidgin-facebookchat = %{version}-%{release}
Obsoletes:      pidgin-facebookchat < 1.35-3
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  libpurple-devel
#BuildRequires:  zlib-devel

%description
This is a Facebook chat plugin for Pidgin and libpurple
messengers. It connects to the new Facebook Chat IM service
without the need for an API key.

Currently the plugin can log into the Facebook servers, grab the
buddy list, send/receive messages, add/remove friends, receive
notifications, search for Facebook friends and set your Facebook
status.

%prep
%setup -q -n pidgin-facebookchat
# Upstream Makefile is totally horrible, use our own instead.
mv Makefile Makefile.orig
install -p %{SOURCE3} Makefile

%build

export CFLAGS="$RPM_OPT_FLAGS"
make LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/purple-2/libfacebook.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/facebook.png
