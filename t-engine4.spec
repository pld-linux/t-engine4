%define		_beta	beta26
Summary:	Roguelike game set in the world of Eyal
Summary(pl.UTF-8):	Gra roguelike osadzona w świecie Eyal
Name:		t-engine4
Version:	1.0.0
Release:	0.%{_beta}.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://te4.org/dl/t-engine/%{name}-src-%{version}%{_beta}.tar.bz2
# Source0-md5:	d490b6a3fa3c44f138af1d0267e6bd5e
URL:		http://te4.org/
BuildRequires:	SDL_ttf-devel
BuildRequires:	premake >= 4.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tales of Maj'Eyal (ToME) is a tactical role-playing roguelike and
action game set in the world of Eyal.

%description -l pl.UTF-8
Tales of Maj'Eyal (ToME) to pełna akcji, taktyczna gra RPG typu
roguelike osadzona w świecie Eyal.

%prep
%setup -q -n %{name}-src-%{version}%{_beta}

# set proper path to bootstrap
%{__sed} -i 's,/bootstrap,%{_datadir}/games/t-engine/bootstrap,' src/main.c

# set proper path to game's data
%{__sed} -i 's,game/,%{_datadir}/games/t-engine/game/,' src/main.c

%build
premake4 gmake

%{__make} \
	config=release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/t-engine}

cp -a t-engine $RPM_BUILD_ROOT%{_bindir}
cp -a bootstrap game $RPM_BUILD_ROOT%{_datadir}/games/t-engine

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING CREDITS
%attr(755,root,root) %{_bindir}/t-engine
%{_datadir}/games/t-engine
