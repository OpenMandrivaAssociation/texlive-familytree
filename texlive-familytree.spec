%global tl_name familytree
%global tl_revision 63739

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Draw family trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/familytree
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/familytree.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Boxes describe individuals; lines connecting boxes represent sibling or
parent-child relationships, or marriages. Excluding the marriage box,
you can get a maleline/patrilineal tree, or a femaleline/matrilineal
tree. For Japanese, the jlreq.cls vertical option (tate) is supported.

