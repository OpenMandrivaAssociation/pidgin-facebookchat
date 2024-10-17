Name:           pidgin-facebookchat
Version:        1.69
Release:        2
Summary:        Libpurple plug-in supporting facebook IM
Group:          Networking/Instant messaging
License:        GPLv3+
URL:            https://code.google.com/p/pidgin-facebookchat/
Source0:	http://pidgin-facebookchat.googlecode.com/files/pidgin-facebookchat-source-%{version}.tar.bz2
Source3:        %{name}-Makefile
Provides:       pidgin-facebookchat = %{version}-%{release}
Obsoletes:      pidgin-facebookchat < 1.35-3
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  pidgin-devel
BuildRequires:	libjson-glib-devel
BuildRequires:  zlib-devel

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
%setup_compile_flags

%make LIBDIR=%{_libdir}

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


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.69-1mdv2011.0
+ Revision: 645378
- update to new version 1.69

* Fri Oct 22 2010 Zombie Ryushu <ryushu@mandriva.org> 1.68-1mdv2011.0
+ Revision: 587186
- Update to 1.68
- Update to 1.68

* Sun Aug 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.67-1mdv2011.0
+ Revision: 573994
- update to new version 1.67
- enable zlib support

* Thu Apr 15 2010 Nicholas Brown <nickbrown@mandriva.org> 1.65-1mdv2010.1
+ Revision: 535090
- New Version

* Tue Dec 15 2009 Zombie Ryushu <ryushu@mandriva.org> 1.64-1mdv2010.1
+ Revision: 478778
- Upgrade to 1.64
- Upgrade to 1.64

* Wed Nov 18 2009 Zombie Ryushu <ryushu@mandriva.org> 1.63-1mdv2010.1
+ Revision: 467191
- Update to 1.63

* Fri Nov 06 2009 Nicholas Brown <nickbrown@mandriva.org> 1.62-1mdv2010.1
+ Revision: 461587
- new version

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.61-1mdv2010.0
+ Revision: 443242
- Update to new version 1.61

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.60-2mdv2010.0
+ Revision: 398815
- Fix file list in custom makefile (fixes #52209: unresolvable
  symbols in pidgin-facebookchat prevent it to load correctly)
- Don't package standard GPLv3 license

* Wed Jul 22 2009 Frederik Himpe <fhimpe@mandriva.org> 1.60-1mdv2010.0
+ Revision: 398615
- update to new version 1.60

* Sat Jul 11 2009 Frederik Himpe <fhimpe@mandriva.org> 1.54-1mdv2010.0
+ Revision: 394792
- Update to new version 1.54
- BuildRequires libclutter0.9-devel libjson-glib-devel now
- Update custom Makefile from Fedora

* Mon Feb 16 2009 Jérôme Soyer <saispo@mandriva.org> 1.47-1mdv2009.1
+ Revision: 340928
- Fix BR
- import pidgin-facebookchat


