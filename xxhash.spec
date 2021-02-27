%define major 0
%define libname	%mklibname %name %{major}
%define devname	%mklibname -d %name


Name:		xxhash
Version:	0.8.0
Release:	1
Summary:	Extremely fast hash algorithm

#		The source for the library (xxhash.c and xxhash.h) is BSD
#		The source for the command line tool (xxhsum.c) is GPLv2+
License:	BSD and GPLv2+
URL:		http://www.xxhash.com/
Source0:	https://github.com/Cyan4973/xxHash/archive/v%{version}/%{name}-%{version}.tar.gz

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package -n	%{libname}
Summary:	Extremely fast hash algorithm - library
License:	BSD


%description -n %{libname}
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for the xxhash library

%prep
%setup -q -n xxHash-%{version}

%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif
%setup_compile_flags
%make_build CFLAGS="%{optflags} -fPIC -O3" FLAGS="%{ldflags}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm %{buildroot}/%{_libdir}/libxxhash.a

%check
make check
make test-xxhsum-c

%files
%{_bindir}/xxh*sum
%{_mandir}/man1/xxh*sum.1*

%files -n %{libname}
%{_libdir}/libxxhash.so.*

%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/xxhash.h
%{_includedir}/xxh3.h
%{_libdir}/libxxhash.so
%{_libdir}/pkgconfig/libxxhash.pc
