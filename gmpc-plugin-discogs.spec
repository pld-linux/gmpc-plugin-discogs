# TODO:
# - desc

%define		source_name gmpc-discogs
Summary:	DiscoGS art fetcher plugin for Gnome Music Player Client
Summary(pl.UTF-8):Wtyczka DiscoGS dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-discogs
Version:	0.19.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	c9b96ee13eeccd5a56f09ae65ebf0472
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_DISCOGS
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool => 0.21
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%find_lang gmpc-discogs

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gmpc-discogs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
