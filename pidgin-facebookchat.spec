Name:           pidgin-facebookchat
Version:        1.63
Release:        %mkrel 1
Summary:        Libpurple plug-in supporting facebook IM
Group:          Networking/Instant messaging
License:        GPLv3+
URL:            http://code.google.com/p/pidgin-facebookchat/
Source0:	http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-source-%{version}.tar.bz2
Source3:        %{name}-Makefile
Provides:       pidgin-facebookchat = %{version}-%{release}
Obsoletes:      pidgin-facebookchat < 1.35-3
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pidgin-devel
BuildRequires:	libjson-glib-devel
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
%setup -q -n %{name}
# Upstream Makefile is totally horrible, use our own instead.
mv Makefile Makefile.orig
install -p %{SOURCE3} Makefile

%build

export CFLAGS="$RPM_OPT_FLAGS"
make LIBDIR=%{_libdir}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}
chmod 0755 %{buildroot}%{_libdir}/purple-2/libfacebook.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/facebook.png
