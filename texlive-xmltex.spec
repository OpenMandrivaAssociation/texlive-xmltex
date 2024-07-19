Name:		texlive-xmltex
Version:	71362
Release:	1
Summary:	Support for parsing XML documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xmltex/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-latex
Requires:	texlive-pdftex
Requires:	texlive-tex
Requires:	texlive-xmltex.bin
%rename xmltex

%description
This package provides an implementation of a parser for
documents matching the XML 1.0 and XML Namespace
Recommendations. In addition to parsing commands are provided
to attatch TeX typesetting instructions to the various markup
elemenets as they are encounted. Sample files for typesetting a
subset of TEI, MathML, are included. Element and Attribute
names, as well as character data, may use any characters
allowed in XML, using UTF-8 or a suitable 8-bit encoding.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xmltex
%_texmf_fmtutil_d/xmltex
%doc %{_texmfdistdir}/doc/otherformats/xmltex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/xmltex <<EOF
#
# from xmltex:
xmltex pdftex language.dat *xmltex.ini
pdfxmltex pdftex language.dat *pdfxmltex.ini
EOF
