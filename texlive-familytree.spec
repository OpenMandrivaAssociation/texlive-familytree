Name:		texlive-familytree
Version:	63739
Release:	2
Summary:	Draw family trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/familytree
License:	gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Boxes describe individuals; lines connecting boxes represent
sibling or parent-child relationships, or marriages. Excluding
the marriage box, you can get a maleline/patrilineal tree, or a
femaleline/matrilineal tree. For Japanese, the jlreq.cls
vertical option (tate) is supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/familytree
%{_texmfdistdir}/tex/latex/familytree
%doc %{_texmfdistdir}/doc/latex/familytree

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
