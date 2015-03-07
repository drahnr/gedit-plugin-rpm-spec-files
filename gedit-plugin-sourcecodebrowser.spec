Name:			gedit-source-code-browser
Summary:		Gedit plugin source code browser
Version:		3.12
Release:		1%{?dist}
License:		Other
Group:			Applications/Editors
Source0:		https://github.com/Quixotix/%{name}/archive/master.zip
Url:			https://github.com/Quixotix/%{name}

BuildRequires:  python3-gobject
Requires:		gedit

%description
Restore tabs plugin for gedit.

%prep
%setup -q -n %{name}-master master.zip


%build
echo "Nothing to build"

%install
install -D sourcecodebrowser/data/org.gnome.gedit.plugins.sourcecodebrowser.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.sourcecodebrowser.gschema.xml
install -D sourcecodebrowser.plugin $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/sourcecodebrowser.plugin
install -d $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/sourcecodebrowser/data
cp -Rvf sourcecodebrowser $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/sourcecodebrowser


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

%{_libdir}/gedit/plugins/sourcecodebrowser.plugin
%{_libdir}/gedit/plugins/sourcecodebrowser/*
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
* Sat Mar 07 2015  Bernhard Schuster  <bernhard@ahoi.io> 3.12
- Initial version
