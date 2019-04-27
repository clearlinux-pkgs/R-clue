#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clue
Version  : 0.3.57
Release  : 21
URL      : https://cran.r-project.org/src/contrib/clue_0.3-57.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clue_0.3-57.tar.gz
Summary  : Cluster Ensembles
Group    : Development/Tools
License  : GPL-2.0
Requires: R-clue-lib = %{version}-%{release}
BuildRequires : R-ape
BuildRequires : R-cclust
BuildRequires : R-e1071
BuildRequires : R-fpc
BuildRequires : R-lpSolve
BuildRequires : R-mlbench
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-clue package.
Group: Libraries

%description lib
lib components for the R-clue package.


%prep
%setup -q -c -n clue

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552727922

%install
export SOURCE_DATE_EPOCH=1552727922
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clue
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clue
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  clue || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clue/CITATION
/usr/lib64/R/library/clue/DESCRIPTION
/usr/lib64/R/library/clue/INDEX
/usr/lib64/R/library/clue/Meta/Rd.rds
/usr/lib64/R/library/clue/Meta/data.rds
/usr/lib64/R/library/clue/Meta/features.rds
/usr/lib64/R/library/clue/Meta/hsearch.rds
/usr/lib64/R/library/clue/Meta/links.rds
/usr/lib64/R/library/clue/Meta/nsInfo.rds
/usr/lib64/R/library/clue/Meta/package.rds
/usr/lib64/R/library/clue/Meta/vignette.rds
/usr/lib64/R/library/clue/NAMESPACE
/usr/lib64/R/library/clue/R/clue
/usr/lib64/R/library/clue/R/clue.rdb
/usr/lib64/R/library/clue/R/clue.rdx
/usr/lib64/R/library/clue/data/CKME.rda
/usr/lib64/R/library/clue/data/Cassini.rda
/usr/lib64/R/library/clue/data/GVME.rda
/usr/lib64/R/library/clue/data/GVME_Consensus.rda
/usr/lib64/R/library/clue/data/Kinship82.rda
/usr/lib64/R/library/clue/data/Kinship82_Consensus.rda
/usr/lib64/R/library/clue/data/Phonemes.rda
/usr/lib64/R/library/clue/doc/clue.R
/usr/lib64/R/library/clue/doc/clue.Rnw
/usr/lib64/R/library/clue/doc/clue.pdf
/usr/lib64/R/library/clue/doc/index.html
/usr/lib64/R/library/clue/help/AnIndex
/usr/lib64/R/library/clue/help/aliases.rds
/usr/lib64/R/library/clue/help/clue.rdb
/usr/lib64/R/library/clue/help/clue.rdx
/usr/lib64/R/library/clue/help/paths.rds
/usr/lib64/R/library/clue/html/00Index.html
/usr/lib64/R/library/clue/html/R.css
/usr/lib64/R/library/clue/po/en@quot/LC_MESSAGES/R-clue.mo

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/clue/libs/clue.so
/usr/lib64/R/library/clue/libs/clue.so.avx2
/usr/lib64/R/library/clue/libs/clue.so.avx512
