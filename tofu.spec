%define name		tofu
%define oname		Tofu
%define version		0.5
%define pyversion	2.5
%define pysystemver	2.5
%define release		%mkrel 2

Summary:	Network game engine written with python and twisted
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{oname}-%{version}.tar.bz2
License:	LGPL
Group:		Development/Python
URL:		http://pyserial.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libpython-devel >= %pyversion
BuildArch:	noarch
Requires:	python, python-twisted-core

%description
Tofu is a practical high-level network game engine, written in Python and 
based on Twisted.

Tofu is designed for games where players play one or several characters 
accross several levels. This includes jump'n run games, RPG or RTS, but not 
Tetris-like games or board game (chess, go,...).

It currently support client-server and single player mode; peer-to-peer mode 
may be added later.

Tofu is Free Software, under the GNU LGPL license.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README demo/*
%attr(0755,root,root) %{_libdir}/python%{pysystemver}/site-packages/*


