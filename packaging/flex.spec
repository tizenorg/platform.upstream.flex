Name:           flex
Version:        2.5.35
Release:        0
License:        BSD-3-Clause
Summary:        Fast Lexical Analyzer Generator
Url:            http://flex.sourceforge.net/
Group:          Development/Languages/C and C++
Source:         %{name}-%{version}.tar.bz2
Source1:        lex-wrapper.sh
Source3:        baselibs.conf
Patch1:         flex-2.5.34-fPIC.patch
Patch2:         flex-2.5.33-yylineno.patch
Patch3:         flex-2.5.34-doc-fix.diff
Patch4:         flex-2.5.34-g++44.diff
Patch5:         flex-2.5.34-asneeded.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
Requires:       m4

%description
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

%prep
%setup -q
%patch1
# Patch2 disabled for now, as the testsuite explicitly tests for yylineno in
# all scanners. Let's see if the failing packages got fixed in the meantime.
#patch2
%patch3
%patch4
%patch5

%build
autoreconf -fi
%configure --disable-nls
make %{?_smp_mflags}

%check
%if !0%{?qemu_user_space_build:1}
make check
%endif

%install
%make_install
install %{SOURCE1}  %{buildroot}/%{_bindir}/lex
ln -s flex %{buildroot}/%{_bindir}/flex++
ln -s flex.1.gz %{buildroot}/%{_mandir}/man1/lex.1.gz

%files
%defattr(-,root,root)
/usr/bin/flex
/usr/bin/flex++
/usr/bin/lex
/usr/include/FlexLexer.h
%{_libdir}/libfl.a
%{_mandir}/man1/flex.1.gz
%{_mandir}/man1/lex.1.gz
%{_infodir}/flex*

