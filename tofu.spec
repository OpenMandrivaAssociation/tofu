%define name		tofu
%define oname		Tofu
%define version		0.5
%define release		%mkrel 8

Summary:	Network game engine written with python and twisted
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{oname}-%{version}.tar.bz2
License:	LGPL
Group:		Development/Python
URL:		http://pyserial.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-buildroot
%py_requires -d
BuildArch:	noarch
Requires:	python-twisted-core

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
%attr(0755,root,root) %{python_sitelib}/*


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.5-8mdv2011.0
+ Revision: 592184
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.5-7mdv2010.0
+ Revision: 445494
- rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 0.5-6mdv2009.1
+ Revision: 327870
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2008.1
+ Revision: 171145
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-2mdv2008.1
+ Revision: 136549
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Emmanuel Andry <eandry@mandriva.org> 0.5-2mdv2007.0
+ Revision: 94090
- rebuild for python 2.5
- Import tofu

* Sun Jun 18 2006 Emmanuel Andry <eandry@mandriva.org> 0.3-%%{1}mdv2007.1
- 0.5

* Mon Sep 12 2005 Guillaume Bedot <ilittletux@mandriva.org> 0.2-1mdk
- First package for tofu (needed for balazar 0.2)

