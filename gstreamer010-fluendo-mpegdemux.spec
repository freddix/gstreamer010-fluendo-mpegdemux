%define		gstname		fluendo-mpegdemux
%define		gst_major_ver   0.10

Summary:	GStreamer MPEG-2 demuxer plugin
Name:		gstreamer010-%{gstname}
Version:	0.10.72
Release:	1
License:	MPL v1.1
Group:		Libraries
Source0:	http://core.fluendo.com/gstreamer/src/gst-fluendo-mpegdemux/gst-%{gstname}-%{version}.tar.bz2
# Source0-md5:	df726579404af65b9536428661ab4322
URL:		http://gstreamer.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer010-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluendo GStreamer plug-in for MPEG demuxing.

%prep
%setup -qn gst-%{gstname}-%{version}

%build
%if 0
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%endif
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstflumpegdemux.so

