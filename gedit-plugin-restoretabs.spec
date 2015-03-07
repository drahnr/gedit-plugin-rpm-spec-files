Name:			gedit-restore-tabs
Summary:		Plugin that restores last sessions tabs
Version:		0.1
Release:		1%{?dist}
License:		GPLv2+
Group:			Applications/Editors
Source0:		https://github.com/Quixotix/%{name}/archive/master.tar.gz
Url:			https://github.com/Quixotix/%{name}

BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  cairo-devel
BuildRequires:  atk-devel
BuildRequires:  python3-gobject

%description
Restore tabs plugin for gedit.

%prep
%setup -q -n gedit-restore-tabs-master master.tar.gz


%build
echo "Nothing to build"


%install
install -D org.gnome.gedit.plugins.restoretabs.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.restoretabs.gschema.xml
install -D restoretabs.plugin $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/restoretabs.plugin
install -D restoretabs.py $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/restoretabs.py


%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%clean
rm -rf "$RPM_BUILD_ROOT"





%files
%defattr(-, root, root)

%doc README.markdown

%{_libdir}/gedit/plugins/restoretabs.p*
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
* Sat Mar 07 2015  Bernhard Schuster  <bernhard@ahoi.io> 0.0.1
- Initial version
