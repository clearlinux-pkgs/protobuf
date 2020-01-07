#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : protobuf
Version  : 3.11.1
Release  : 59
URL      : https://github.com/protocolbuffers/protobuf/releases/download/v3.11.1/protobuf-all-3.11.1.tar.gz
Source0  : https://github.com/protocolbuffers/protobuf/releases/download/v3.11.1/protobuf-all-3.11.1.tar.gz
Summary  : Protocol Buffers - Google's data interchange format
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: protobuf-bin = %{version}-%{release}
Requires: protobuf-lib = %{version}-%{release}
Requires: protobuf-license = %{version}-%{release}
Requires: protobuf-python = %{version}-%{release}
Requires: protobuf-python3 = %{version}-%{release}
Requires: setuptools
Requires: six
BuildRequires : apache-maven
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-mvn
BuildRequires : buildreq-php
BuildRequires : emacs
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : zlib-dev
Patch1: 0001-Add-gmock-gtest-at-1.7.0.patch
Patch2: 0002-Ensure-everything-can-build-in-tree.patch
Patch3: 0003-Add-gtest-symlink-to-account-for-the-rest-of-the-bro.patch

%description
This directory contains the Protocol Buffers runtime implementation via both a
pure PHP package and a native c extension. The pure PHP package is intended to
provide usability to wider range of PHP platforms, while the c extension is
intended to provide higher performance. Both implementations provide the same
runtime APIs and share the same generated code. Users don’t need to re-generate
code for the same proto definition when they want to switch the implementation
later.

%package bin
Summary: bin components for the protobuf package.
Group: Binaries
Requires: protobuf-license = %{version}-%{release}

%description bin
bin components for the protobuf package.


%package dev
Summary: dev components for the protobuf package.
Group: Development
Requires: protobuf-lib = %{version}-%{release}
Requires: protobuf-bin = %{version}-%{release}
Provides: protobuf-devel = %{version}-%{release}
Requires: protobuf = %{version}-%{release}
Requires: protobuf = %{version}-%{release}

%description dev
dev components for the protobuf package.


%package lib
Summary: lib components for the protobuf package.
Group: Libraries
Requires: protobuf-license = %{version}-%{release}

%description lib
lib components for the protobuf package.


%package license
Summary: license components for the protobuf package.
Group: Default

%description license
license components for the protobuf package.


%package python
Summary: python components for the protobuf package.
Group: Default
Requires: protobuf-python3 = %{version}-%{release}

%description python
python components for the protobuf package.


%package python3
Summary: python3 components for the protobuf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the protobuf package.


%prep
%setup -q -n protobuf-3.11.1
cd %{_builddir}/protobuf-3.11.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575545692
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1575545692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/protobuf
cp %{_builddir}/protobuf-3.11.1/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
cp %{_builddir}/protobuf-3.11.1/third_party/googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/protobuf-3.11.1/third_party/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/protobuf-3.11.1/third_party/googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/5a2314153eadadc69258a9429104cd11804ea304
%make_install
## install_append content
pushd python
python ./setup.py install --root=%{buildroot} --cpp_implementation
python3 ./setup.py install --root=%{buildroot} --cpp_implementation
popd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/protoc

%files dev
%defattr(-,root,root,-)
/usr/include/google/protobuf/any.h
/usr/include/google/protobuf/any.pb.h
/usr/include/google/protobuf/any.proto
/usr/include/google/protobuf/api.pb.h
/usr/include/google/protobuf/api.proto
/usr/include/google/protobuf/arena.h
/usr/include/google/protobuf/arena_impl.h
/usr/include/google/protobuf/arenastring.h
/usr/include/google/protobuf/compiler/code_generator.h
/usr/include/google/protobuf/compiler/command_line_interface.h
/usr/include/google/protobuf/compiler/cpp/cpp_generator.h
/usr/include/google/protobuf/compiler/csharp/csharp_generator.h
/usr/include/google/protobuf/compiler/csharp/csharp_names.h
/usr/include/google/protobuf/compiler/importer.h
/usr/include/google/protobuf/compiler/java/java_generator.h
/usr/include/google/protobuf/compiler/java/java_names.h
/usr/include/google/protobuf/compiler/js/js_generator.h
/usr/include/google/protobuf/compiler/js/well_known_types_embed.h
/usr/include/google/protobuf/compiler/objectivec/objectivec_generator.h
/usr/include/google/protobuf/compiler/objectivec/objectivec_helpers.h
/usr/include/google/protobuf/compiler/parser.h
/usr/include/google/protobuf/compiler/php/php_generator.h
/usr/include/google/protobuf/compiler/plugin.h
/usr/include/google/protobuf/compiler/plugin.pb.h
/usr/include/google/protobuf/compiler/plugin.proto
/usr/include/google/protobuf/compiler/python/python_generator.h
/usr/include/google/protobuf/compiler/ruby/ruby_generator.h
/usr/include/google/protobuf/descriptor.h
/usr/include/google/protobuf/descriptor.pb.h
/usr/include/google/protobuf/descriptor.proto
/usr/include/google/protobuf/descriptor_database.h
/usr/include/google/protobuf/duration.pb.h
/usr/include/google/protobuf/duration.proto
/usr/include/google/protobuf/dynamic_message.h
/usr/include/google/protobuf/empty.pb.h
/usr/include/google/protobuf/empty.proto
/usr/include/google/protobuf/extension_set.h
/usr/include/google/protobuf/extension_set_inl.h
/usr/include/google/protobuf/field_mask.pb.h
/usr/include/google/protobuf/field_mask.proto
/usr/include/google/protobuf/generated_enum_reflection.h
/usr/include/google/protobuf/generated_enum_util.h
/usr/include/google/protobuf/generated_message_reflection.h
/usr/include/google/protobuf/generated_message_table_driven.h
/usr/include/google/protobuf/generated_message_util.h
/usr/include/google/protobuf/has_bits.h
/usr/include/google/protobuf/implicit_weak_message.h
/usr/include/google/protobuf/inlined_string_field.h
/usr/include/google/protobuf/io/coded_stream.h
/usr/include/google/protobuf/io/gzip_stream.h
/usr/include/google/protobuf/io/io_win32.h
/usr/include/google/protobuf/io/printer.h
/usr/include/google/protobuf/io/strtod.h
/usr/include/google/protobuf/io/tokenizer.h
/usr/include/google/protobuf/io/zero_copy_stream.h
/usr/include/google/protobuf/io/zero_copy_stream_impl.h
/usr/include/google/protobuf/io/zero_copy_stream_impl_lite.h
/usr/include/google/protobuf/map.h
/usr/include/google/protobuf/map_entry.h
/usr/include/google/protobuf/map_entry_lite.h
/usr/include/google/protobuf/map_field.h
/usr/include/google/protobuf/map_field_inl.h
/usr/include/google/protobuf/map_field_lite.h
/usr/include/google/protobuf/map_type_handler.h
/usr/include/google/protobuf/message.h
/usr/include/google/protobuf/message_lite.h
/usr/include/google/protobuf/metadata.h
/usr/include/google/protobuf/metadata_lite.h
/usr/include/google/protobuf/parse_context.h
/usr/include/google/protobuf/port.h
/usr/include/google/protobuf/port_def.inc
/usr/include/google/protobuf/port_undef.inc
/usr/include/google/protobuf/reflection.h
/usr/include/google/protobuf/reflection_ops.h
/usr/include/google/protobuf/repeated_field.h
/usr/include/google/protobuf/service.h
/usr/include/google/protobuf/source_context.pb.h
/usr/include/google/protobuf/source_context.proto
/usr/include/google/protobuf/struct.pb.h
/usr/include/google/protobuf/struct.proto
/usr/include/google/protobuf/stubs/bytestream.h
/usr/include/google/protobuf/stubs/callback.h
/usr/include/google/protobuf/stubs/casts.h
/usr/include/google/protobuf/stubs/common.h
/usr/include/google/protobuf/stubs/fastmem.h
/usr/include/google/protobuf/stubs/hash.h
/usr/include/google/protobuf/stubs/logging.h
/usr/include/google/protobuf/stubs/macros.h
/usr/include/google/protobuf/stubs/map_util.h
/usr/include/google/protobuf/stubs/mutex.h
/usr/include/google/protobuf/stubs/once.h
/usr/include/google/protobuf/stubs/platform_macros.h
/usr/include/google/protobuf/stubs/port.h
/usr/include/google/protobuf/stubs/status.h
/usr/include/google/protobuf/stubs/stl_util.h
/usr/include/google/protobuf/stubs/stringpiece.h
/usr/include/google/protobuf/stubs/strutil.h
/usr/include/google/protobuf/stubs/template_util.h
/usr/include/google/protobuf/text_format.h
/usr/include/google/protobuf/timestamp.pb.h
/usr/include/google/protobuf/timestamp.proto
/usr/include/google/protobuf/type.pb.h
/usr/include/google/protobuf/type.proto
/usr/include/google/protobuf/unknown_field_set.h
/usr/include/google/protobuf/util/delimited_message_util.h
/usr/include/google/protobuf/util/field_comparator.h
/usr/include/google/protobuf/util/field_mask_util.h
/usr/include/google/protobuf/util/json_util.h
/usr/include/google/protobuf/util/message_differencer.h
/usr/include/google/protobuf/util/time_util.h
/usr/include/google/protobuf/util/type_resolver.h
/usr/include/google/protobuf/util/type_resolver_util.h
/usr/include/google/protobuf/wire_format.h
/usr/include/google/protobuf/wire_format_lite.h
/usr/include/google/protobuf/wrappers.pb.h
/usr/include/google/protobuf/wrappers.proto
/usr/lib64/libprotobuf-lite.so
/usr/lib64/libprotobuf.so
/usr/lib64/libprotoc.so
/usr/lib64/pkgconfig/protobuf-lite.pc
/usr/lib64/pkgconfig/protobuf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-lite.so.22
/usr/lib64/libprotobuf-lite.so.22.0.1
/usr/lib64/libprotobuf.so.22
/usr/lib64/libprotobuf.so.22.0.1
/usr/lib64/libprotoc.so.22
/usr/lib64/libprotoc.so.22.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/protobuf/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/protobuf/5a2314153eadadc69258a9429104cd11804ea304

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
