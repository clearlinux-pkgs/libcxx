#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0FC3042E345AD05D (hans@chromium.org)
#
Name     : libcxx
Version  : 10.0.0
Release  : 1
URL      : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/libcxx-10.0.0.src.tar.xz
Source0  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/libcxx-10.0.0.src.tar.xz
Source1  : https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.0/libcxx-10.0.0.src.tar.xz.sig
Summary  : Google microbenchmark framework
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: libcxx-lib = %{version}-%{release}
Requires: libcxx-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : llvm

%description
This directory contains a partial implementation of the xlocale APIs for
Solaris.  Some portions are lifted from FreeBSD libc, and so are covered by a
2-clause BSD license instead of the MIT/UUIC license that the rest of libc++ is
distributed under.

%package dev
Summary: dev components for the libcxx package.
Group: Development
Requires: libcxx-lib = %{version}-%{release}
Provides: libcxx-devel = %{version}-%{release}
Requires: libcxx = %{version}-%{release}

%description dev
dev components for the libcxx package.


%package lib
Summary: lib components for the libcxx package.
Group: Libraries
Requires: libcxx-license = %{version}-%{release}

%description lib
lib components for the libcxx package.


%package license
Summary: license components for the libcxx package.
Group: Default

%description license
license components for the libcxx package.


%prep
%setup -q -n libcxx-10.0.0.src
cd %{_builddir}/libcxx-10.0.0.src

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587505057
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DPYTHON_EXECUTABLE=/usr/bin/python3 \
-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
-DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
-DLIBCXX_ENABLE_STATIC=NO \
-DLIBCXX_ENABLE_SHARED=YES \
-DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=NO
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587505057
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcxx
cp %{_builddir}/libcxx-10.0.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/libcxx/7b75a5471af8b3d49e60df0a5d72f95ea8214231
cp %{_builddir}/libcxx-10.0.0.src/utils/google-benchmark/LICENSE %{buildroot}/usr/share/package-licenses/libcxx/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/c++/v1/__bit_reference
/usr/include/c++/v1/__bsd_locale_defaults.h
/usr/include/c++/v1/__bsd_locale_fallbacks.h
/usr/include/c++/v1/__config
/usr/include/c++/v1/__debug
/usr/include/c++/v1/__errc
/usr/include/c++/v1/__functional_03
/usr/include/c++/v1/__functional_base
/usr/include/c++/v1/__functional_base_03
/usr/include/c++/v1/__hash_table
/usr/include/c++/v1/__libcpp_version
/usr/include/c++/v1/__locale
/usr/include/c++/v1/__mutex_base
/usr/include/c++/v1/__node_handle
/usr/include/c++/v1/__nullptr
/usr/include/c++/v1/__split_buffer
/usr/include/c++/v1/__sso_allocator
/usr/include/c++/v1/__std_stream
/usr/include/c++/v1/__string
/usr/include/c++/v1/__threading_support
/usr/include/c++/v1/__tree
/usr/include/c++/v1/__tuple
/usr/include/c++/v1/__undef_macros
/usr/include/c++/v1/algorithm
/usr/include/c++/v1/any
/usr/include/c++/v1/array
/usr/include/c++/v1/atomic
/usr/include/c++/v1/bit
/usr/include/c++/v1/bitset
/usr/include/c++/v1/cassert
/usr/include/c++/v1/ccomplex
/usr/include/c++/v1/cctype
/usr/include/c++/v1/cerrno
/usr/include/c++/v1/cfenv
/usr/include/c++/v1/cfloat
/usr/include/c++/v1/charconv
/usr/include/c++/v1/chrono
/usr/include/c++/v1/cinttypes
/usr/include/c++/v1/ciso646
/usr/include/c++/v1/climits
/usr/include/c++/v1/clocale
/usr/include/c++/v1/cmath
/usr/include/c++/v1/codecvt
/usr/include/c++/v1/compare
/usr/include/c++/v1/complex
/usr/include/c++/v1/complex.h
/usr/include/c++/v1/condition_variable
/usr/include/c++/v1/csetjmp
/usr/include/c++/v1/csignal
/usr/include/c++/v1/cstdarg
/usr/include/c++/v1/cstdbool
/usr/include/c++/v1/cstddef
/usr/include/c++/v1/cstdint
/usr/include/c++/v1/cstdio
/usr/include/c++/v1/cstdlib
/usr/include/c++/v1/cstring
/usr/include/c++/v1/ctgmath
/usr/include/c++/v1/ctime
/usr/include/c++/v1/ctype.h
/usr/include/c++/v1/cwchar
/usr/include/c++/v1/cwctype
/usr/include/c++/v1/deque
/usr/include/c++/v1/errno.h
/usr/include/c++/v1/exception
/usr/include/c++/v1/execution
/usr/include/c++/v1/experimental/__config
/usr/include/c++/v1/experimental/__memory
/usr/include/c++/v1/experimental/algorithm
/usr/include/c++/v1/experimental/coroutine
/usr/include/c++/v1/experimental/deque
/usr/include/c++/v1/experimental/filesystem
/usr/include/c++/v1/experimental/forward_list
/usr/include/c++/v1/experimental/functional
/usr/include/c++/v1/experimental/iterator
/usr/include/c++/v1/experimental/list
/usr/include/c++/v1/experimental/map
/usr/include/c++/v1/experimental/memory_resource
/usr/include/c++/v1/experimental/propagate_const
/usr/include/c++/v1/experimental/regex
/usr/include/c++/v1/experimental/set
/usr/include/c++/v1/experimental/simd
/usr/include/c++/v1/experimental/string
/usr/include/c++/v1/experimental/type_traits
/usr/include/c++/v1/experimental/unordered_map
/usr/include/c++/v1/experimental/unordered_set
/usr/include/c++/v1/experimental/utility
/usr/include/c++/v1/experimental/vector
/usr/include/c++/v1/ext/__hash
/usr/include/c++/v1/ext/hash_map
/usr/include/c++/v1/ext/hash_set
/usr/include/c++/v1/fenv.h
/usr/include/c++/v1/filesystem
/usr/include/c++/v1/float.h
/usr/include/c++/v1/forward_list
/usr/include/c++/v1/fstream
/usr/include/c++/v1/functional
/usr/include/c++/v1/future
/usr/include/c++/v1/initializer_list
/usr/include/c++/v1/inttypes.h
/usr/include/c++/v1/iomanip
/usr/include/c++/v1/ios
/usr/include/c++/v1/iosfwd
/usr/include/c++/v1/iostream
/usr/include/c++/v1/istream
/usr/include/c++/v1/iterator
/usr/include/c++/v1/limits
/usr/include/c++/v1/limits.h
/usr/include/c++/v1/list
/usr/include/c++/v1/locale
/usr/include/c++/v1/locale.h
/usr/include/c++/v1/map
/usr/include/c++/v1/math.h
/usr/include/c++/v1/memory
/usr/include/c++/v1/module.modulemap
/usr/include/c++/v1/mutex
/usr/include/c++/v1/new
/usr/include/c++/v1/numeric
/usr/include/c++/v1/optional
/usr/include/c++/v1/ostream
/usr/include/c++/v1/queue
/usr/include/c++/v1/random
/usr/include/c++/v1/ratio
/usr/include/c++/v1/regex
/usr/include/c++/v1/scoped_allocator
/usr/include/c++/v1/set
/usr/include/c++/v1/setjmp.h
/usr/include/c++/v1/shared_mutex
/usr/include/c++/v1/span
/usr/include/c++/v1/sstream
/usr/include/c++/v1/stack
/usr/include/c++/v1/stdbool.h
/usr/include/c++/v1/stddef.h
/usr/include/c++/v1/stdexcept
/usr/include/c++/v1/stdint.h
/usr/include/c++/v1/stdio.h
/usr/include/c++/v1/stdlib.h
/usr/include/c++/v1/streambuf
/usr/include/c++/v1/string
/usr/include/c++/v1/string.h
/usr/include/c++/v1/string_view
/usr/include/c++/v1/strstream
/usr/include/c++/v1/support/android/locale_bionic.h
/usr/include/c++/v1/support/fuchsia/xlocale.h
/usr/include/c++/v1/support/ibm/limits.h
/usr/include/c++/v1/support/ibm/locale_mgmt_aix.h
/usr/include/c++/v1/support/ibm/support.h
/usr/include/c++/v1/support/ibm/xlocale.h
/usr/include/c++/v1/support/musl/xlocale.h
/usr/include/c++/v1/support/newlib/xlocale.h
/usr/include/c++/v1/support/solaris/floatingpoint.h
/usr/include/c++/v1/support/solaris/wchar.h
/usr/include/c++/v1/support/solaris/xlocale.h
/usr/include/c++/v1/support/win32/limits_msvc_win32.h
/usr/include/c++/v1/support/win32/locale_win32.h
/usr/include/c++/v1/support/xlocale/__nop_locale_mgmt.h
/usr/include/c++/v1/support/xlocale/__posix_l_fallback.h
/usr/include/c++/v1/support/xlocale/__strtonum_fallback.h
/usr/include/c++/v1/system_error
/usr/include/c++/v1/tgmath.h
/usr/include/c++/v1/thread
/usr/include/c++/v1/tuple
/usr/include/c++/v1/type_traits
/usr/include/c++/v1/typeindex
/usr/include/c++/v1/typeinfo
/usr/include/c++/v1/unordered_map
/usr/include/c++/v1/unordered_set
/usr/include/c++/v1/utility
/usr/include/c++/v1/valarray
/usr/include/c++/v1/variant
/usr/include/c++/v1/vector
/usr/include/c++/v1/version
/usr/include/c++/v1/wchar.h
/usr/include/c++/v1/wctype.h
/usr/lib64/libc++.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libc++.so.1
/usr/lib64/libc++.so.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcxx/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/libcxx/7b75a5471af8b3d49e60df0a5d72f95ea8214231
