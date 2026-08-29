Name:		mugshot
Version:	0.4.3
Release:	1
URL:		https://github.com/bluesabre/mugshot
Source0:	https://github.com/bluesabre/mugshot/archive/refs/tags/%{name}-%{version}.tar.gz
Summary:	Allows user to set profile picture on xfce/lightdm
License:	GPL-3.0-only
Group:		Graphical Desktop/Xfce
BuildArch:  noarch

BuildRequires:	typelib(Gtk)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:  python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(pexpect)
BuildRequires:	intltool
BuildRequires:	desktop-file-utils

Requires:	python%{pyver}dist(pycairo)
Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pexpect)

# Optional dependencies for webcam support
Recommends: gstreamer1.0-plugins-good
Recommends: gstreamer-tools
Recommends: typelib(Cheese)
Recommends: typelib(GtkClutter)

%description
Allows user to set profile picture on xfce/lightdm

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
%py_build

%install
# Fix translations not found
install -dm 0755 %{buildroot}%{_datadir}/locale
cp -a build/mo/* %{buildroot}%{_datadir}/locale/

# Fix desktop file not found
install -Dm 0644 build/share/applications/org.bluesabre.Mugshot.desktop %{buildroot}/usr/share/applications/org.bluesabre.Mugshot.desktop

%py_install

# Remove unused doc directory
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Fix permissions of .py files
chmod a+x %{buildroot}%{py_sitedir}/%{name}/*.py
chmod a+x %{buildroot}%{py_sitedir}/%{name}_lib/*.py

# Fix python-bytecode-inconsistent-mtime.
pushd %{buildroot}%{py_sitedir}/%{name}_lib
%py_compile .
popd

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{py_sitedir}/%{name}*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/org.bluesabre.Mugshot.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/org.bluesabre.mugshot.gschema.xml
%{_datadir}/man/man1/mugshot.1.zst