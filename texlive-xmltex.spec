# revision 23409
# category Package
# catalog-ctan /macros/xmltex/base
# catalog-date 2006-12-16 17:11:43 +0100
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-xmltex
Version:	0.8
Release:	4
Summary:	Support for parsing XML documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xmltex/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xmltex.doc.tar.xz
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
%{_texmfdistdir}/tex/xmltex/base/iso-8859-1.xmt
%{_texmfdistdir}/tex/xmltex/base/iso-8859-2.xmt
%{_texmfdistdir}/tex/xmltex/base/koi8-r.xmt
%{_texmfdistdir}/tex/xmltex/base/langtest.xmt
%{_texmfdistdir}/tex/xmltex/base/mathml2.xmt
%{_texmfdistdir}/tex/xmltex/base/sec.xmt
%{_texmfdistdir}/tex/xmltex/base/utf-16.xmt
%{_texmfdistdir}/tex/xmltex/base/windows-1250.xmt
%{_texmfdistdir}/tex/xmltex/base/xmltex.cfg
%{_texmfdistdir}/tex/xmltex/base/xmltex.tex
%{_texmfdistdir}/tex/xmltex/config/pdfxmltex.ini
%{_texmfdistdir}/tex/xmltex/config/xmltex.ini
%_texmf_fmtutil_d/xmltex
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/englishutf16.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/englishutf8.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/langtest.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/manual.html
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/manual.tex
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/manual.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/manual.xsl
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/portugeselatin1.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/readme.txt
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/russiankoi8.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/russianutf8.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/testascii.cfg
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/testascii.tex
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/testascii.xml
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/testsec.tex
%doc %{_texmfdistdir}/doc/otherformats/xmltex/base/testsec.xml

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
