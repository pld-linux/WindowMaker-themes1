Summary:	Pack of themes for WindowMaker
Summary(pl):	Zestaw motywów dla WindowMaker-a
Name:		WindowMaker-themes-pack1
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	%{name}.tar.gz
# Source0-md5:	c4f0587d9bd6a38c497f5c91bdd08796
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/WindowMaker/Themes

%description
This is a set of 20 themes for WindowMaker made by jensen
<jensen@optushome.com.au>: Abstract Blues, Abyss of Red, A Feeling of
Rain - Sunset, A Feeling of Rain, Aqua Flower, Aqua Strawberry, Autumn
Leaves, Below The Waterline, Binary, Bionic Instinct, Blue Day, Blue
Flower Dark, Blue Mist, City By Night, Construction, Deoba, Diesel,
Digital Flight, Fire Flower, Foggy Dawn.

%description -l pl
Zestaw 20 motywów dla WindowMaker-a wykonanych przez jensena
<jensen@optushome.com.au>: Abstract Blues, Abyss of Red, A Feeling of
Rain - Sunset, A Feeling of Rain, Aqua Flower, Aqua Strawberry, Autumn
Leaves, Below The Waterline, Binary, Bionic Instinct, Blue Day, Blue
Flower Dark, Blue Mist, City By Night, Construction, Deoba, Diesel,
Digital Flight, Fire Flower, Foggy Dawn.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
