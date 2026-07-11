%global tl_name xmltex
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Support for parsing XML documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/xmltex/base
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(dehyph)
Requires:	texlive(firstaid)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(latex)
Requires:	texlive(latex-fonts)
Requires:	texlive(pdftex)
Requires:	texlive(tex)
Requires:	texlive(tex-ini-files)
Requires:	texlive(unicode-data)
Requires:	texlive(xmltex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an implementation of a parser for documents
matching the XML 1.0 and XML Namespace Recommendations. In addition to
parsing commands are provided to attach TeX typesetting instructions to
the various markup elements as they are encountered. Sample files for
typesetting a subset of TEI, MathML, are included. Element and Attribute
names, as well as character data, may use any characters allowed in XML,
using UTF-8 or a suitable 8-bit encoding.

