Summary:	This is a Facebook chat plugin for Pidgin and libpurple
Name:     	pidgin-facebookchat
Version:	1.47
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
Source0: 	http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-1.47.tar.bz2
Patch0:         pidgin-facebookchat-mdv.patch
URL:		http://code.google.com/p/pidgin-facebookchat/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel

%description
Currently the plugin can log into the Facebook servers, grab the buddy list,
send/receive messages, add/remove friends, receive notifications, search for
Facebook friends and set your Facebook status.

%files
%defattr(-, root, root)
%doc COPYING COPYRIGHT
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*

#---------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
export CFLAGS="%optflags"
export LDFLAGS="%ldflags"
%ifarch %{ix86}
%make libfacebook.so
%else
%make libfacebook64.so
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ifarch %{ix86}
install -D -m0755 libfacebook.so %buildroot%{_libdir}/purple-2/libfacebook.so
%else
install -D -m0755 libfacebook64.so %buildroot%{_libdir}/purple-2/libfacebook.so
%endif
install -D -m0644 facebook16.png %buildroot%{_datadir}/pixmaps/pidgin/protocols/16/facebook.png
install -D -m0644 facebook22.png %buildroot%{_datadir}/pixmaps/pidgin/protocols/22/facebook.png
install -D -m0644 facebook48.png %buildroot%{_datadir}/pixmaps/pidgin/protocols/48/facebook.png

%clean
rm -rf $RPM_BUILD_ROOT
