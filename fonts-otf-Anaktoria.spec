%define fontname	Anaktoria
%define name		fonts-otf-%{fontname}
%define version		1.01
%define release		3

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Anaktoria fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Grecs du roi was designed by Claude Garamond (1480 - 1561) between
1541 and 1544, commissioned by king Francis I of France, for the
exclusive use by the Imprimerie Nationale in Paris. Greek in Anaktoria
is based on a modern version of Grecs du roi prepared by Mindaugas
Strockis in 2001. Lowercase Latin stems from the titles in the 1623
First Folio Edition of Shakespeare. Scott Mann & Peter Guither
prepared a modern version for The Illinois Shakespeare Festival in
1995. Cyrillic has been designed to match the above Greek and
Latin. The font covers the Windows Glyph List, Greek Extended, various
typographic extras and some Open Type features (Numerators,
Denominators, Fractions, Old Style Figures, Historical Forms,
Stylistic Alternates, Ligatures, Swash Capitals).

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.01-2mdv2011.0
+ Revision: 675506
- br fontconfig for fc-query used in new rpm-setup-build

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 1.01-1mdv2011.0
+ Revision: 562726
- import fonts-otf-Anaktoria

