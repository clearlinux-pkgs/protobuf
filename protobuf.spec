#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 6fa3d52
#
%define keepstatic 1
Name     : protobuf
Version  : 25.3
Release  : 106
URL      : https://github.com/protocolbuffers/protobuf/releases/download/v25.3/protobuf-25.3.tar.gz
Source0  : https://github.com/protocolbuffers/protobuf/releases/download/v25.3/protobuf-25.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: protobuf-bin = %{version}-%{release}
Requires: protobuf-lib = %{version}-%{release}
Requires: protobuf-license = %{version}-%{release}
BuildRequires : abseil-cpp-dev
BuildRequires : cmake
BuildRequires : emacs
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : protobuf-dev
BuildRequires : python3-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is the 'v2' C++ implementation for python proto2.
It is active when:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2

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
Requires: protobuf-staticdev

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


%package staticdev
Summary: staticdev components for the protobuf package.
Group: Default
Requires: protobuf-dev = %{version}-%{release}

%description staticdev
staticdev components for the protobuf package.


%prep
%setup -q -n protobuf-25.3
cd %{_builddir}/protobuf-25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717002225
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -D protobuf_USE_EXTERNAL_GTEST=ON \
-D protobuf_ABSL_PROVIDER=package \
-D protobuf_BUILD_SHARED_LIBS=ON \
-W no-dev
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -D protobuf_USE_EXTERNAL_GTEST=ON \
-D protobuf_ABSL_PROVIDER=package \
-D protobuf_BUILD_SHARED_LIBS=ON \
-W no-dev
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1717002225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/protobuf
cp %{_builddir}/protobuf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6 || :
cp %{_builddir}/protobuf-%{version}/third_party/lunit/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/fdd1d72fcc979c32a5ab8ae278a2dfd967faf820 || :
cp %{_builddir}/protobuf-%{version}/third_party/utf8_range/LICENSE %{buildroot}/usr/share/package-licenses/protobuf/252c7fd154ca740ae6f765d206fbd9119108a0e3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/protoc-25.3.0
/usr/bin/protoc
/usr/bin/protoc-25.3.0

%files dev
%defattr(-,root,root,-)
/usr/include/google/protobuf/any.h
/usr/include/google/protobuf/any.pb.h
/usr/include/google/protobuf/any.proto
/usr/include/google/protobuf/api.pb.h
/usr/include/google/protobuf/api.proto
/usr/include/google/protobuf/arena.h
/usr/include/google/protobuf/arena_align.h
/usr/include/google/protobuf/arena_allocation_policy.h
/usr/include/google/protobuf/arena_cleanup.h
/usr/include/google/protobuf/arenastring.h
/usr/include/google/protobuf/arenaz_sampler.h
/usr/include/google/protobuf/compiler/allowlists/allowlist.h
/usr/include/google/protobuf/compiler/allowlists/allowlists.h
/usr/include/google/protobuf/compiler/code_generator.h
/usr/include/google/protobuf/compiler/command_line_interface.h
/usr/include/google/protobuf/compiler/cpp/enum.h
/usr/include/google/protobuf/compiler/cpp/extension.h
/usr/include/google/protobuf/compiler/cpp/field.h
/usr/include/google/protobuf/compiler/cpp/field_generators/generators.h
/usr/include/google/protobuf/compiler/cpp/file.h
/usr/include/google/protobuf/compiler/cpp/generator.h
/usr/include/google/protobuf/compiler/cpp/helpers.h
/usr/include/google/protobuf/compiler/cpp/message.h
/usr/include/google/protobuf/compiler/cpp/message_layout_helper.h
/usr/include/google/protobuf/compiler/cpp/names.h
/usr/include/google/protobuf/compiler/cpp/options.h
/usr/include/google/protobuf/compiler/cpp/padding_optimizer.h
/usr/include/google/protobuf/compiler/cpp/parse_function_generator.h
/usr/include/google/protobuf/compiler/cpp/service.h
/usr/include/google/protobuf/compiler/cpp/tracker.h
/usr/include/google/protobuf/compiler/csharp/csharp_doc_comment.h
/usr/include/google/protobuf/compiler/csharp/csharp_enum.h
/usr/include/google/protobuf/compiler/csharp/csharp_enum_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_field_base.h
/usr/include/google/protobuf/compiler/csharp/csharp_generator.h
/usr/include/google/protobuf/compiler/csharp/csharp_helpers.h
/usr/include/google/protobuf/compiler/csharp/csharp_map_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_message.h
/usr/include/google/protobuf/compiler/csharp/csharp_message_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_options.h
/usr/include/google/protobuf/compiler/csharp/csharp_primitive_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_reflection_class.h
/usr/include/google/protobuf/compiler/csharp/csharp_repeated_enum_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_repeated_message_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_repeated_primitive_field.h
/usr/include/google/protobuf/compiler/csharp/csharp_source_generator_base.h
/usr/include/google/protobuf/compiler/csharp/csharp_wrapper_field.h
/usr/include/google/protobuf/compiler/csharp/names.h
/usr/include/google/protobuf/compiler/importer.h
/usr/include/google/protobuf/compiler/java/context.h
/usr/include/google/protobuf/compiler/java/doc_comment.h
/usr/include/google/protobuf/compiler/java/enum.h
/usr/include/google/protobuf/compiler/java/enum_field.h
/usr/include/google/protobuf/compiler/java/enum_field_lite.h
/usr/include/google/protobuf/compiler/java/enum_lite.h
/usr/include/google/protobuf/compiler/java/extension.h
/usr/include/google/protobuf/compiler/java/extension_lite.h
/usr/include/google/protobuf/compiler/java/field.h
/usr/include/google/protobuf/compiler/java/file.h
/usr/include/google/protobuf/compiler/java/generator.h
/usr/include/google/protobuf/compiler/java/generator_factory.h
/usr/include/google/protobuf/compiler/java/helpers.h
/usr/include/google/protobuf/compiler/java/java_features.pb.h
/usr/include/google/protobuf/compiler/java/kotlin_generator.h
/usr/include/google/protobuf/compiler/java/map_field.h
/usr/include/google/protobuf/compiler/java/map_field_lite.h
/usr/include/google/protobuf/compiler/java/message.h
/usr/include/google/protobuf/compiler/java/message_builder.h
/usr/include/google/protobuf/compiler/java/message_builder_lite.h
/usr/include/google/protobuf/compiler/java/message_field.h
/usr/include/google/protobuf/compiler/java/message_field_lite.h
/usr/include/google/protobuf/compiler/java/message_lite.h
/usr/include/google/protobuf/compiler/java/message_serialization.h
/usr/include/google/protobuf/compiler/java/name_resolver.h
/usr/include/google/protobuf/compiler/java/names.h
/usr/include/google/protobuf/compiler/java/options.h
/usr/include/google/protobuf/compiler/java/primitive_field.h
/usr/include/google/protobuf/compiler/java/primitive_field_lite.h
/usr/include/google/protobuf/compiler/java/service.h
/usr/include/google/protobuf/compiler/java/shared_code_generator.h
/usr/include/google/protobuf/compiler/java/string_field.h
/usr/include/google/protobuf/compiler/java/string_field_lite.h
/usr/include/google/protobuf/compiler/objectivec/enum.h
/usr/include/google/protobuf/compiler/objectivec/enum_field.h
/usr/include/google/protobuf/compiler/objectivec/extension.h
/usr/include/google/protobuf/compiler/objectivec/field.h
/usr/include/google/protobuf/compiler/objectivec/file.h
/usr/include/google/protobuf/compiler/objectivec/generator.h
/usr/include/google/protobuf/compiler/objectivec/helpers.h
/usr/include/google/protobuf/compiler/objectivec/import_writer.h
/usr/include/google/protobuf/compiler/objectivec/line_consumer.h
/usr/include/google/protobuf/compiler/objectivec/map_field.h
/usr/include/google/protobuf/compiler/objectivec/message.h
/usr/include/google/protobuf/compiler/objectivec/message_field.h
/usr/include/google/protobuf/compiler/objectivec/names.h
/usr/include/google/protobuf/compiler/objectivec/nsobject_methods.h
/usr/include/google/protobuf/compiler/objectivec/oneof.h
/usr/include/google/protobuf/compiler/objectivec/options.h
/usr/include/google/protobuf/compiler/objectivec/primitive_field.h
/usr/include/google/protobuf/compiler/objectivec/text_format_decode_data.h
/usr/include/google/protobuf/compiler/parser.h
/usr/include/google/protobuf/compiler/php/names.h
/usr/include/google/protobuf/compiler/php/php_generator.h
/usr/include/google/protobuf/compiler/plugin.h
/usr/include/google/protobuf/compiler/plugin.pb.h
/usr/include/google/protobuf/compiler/plugin.proto
/usr/include/google/protobuf/compiler/python/generator.h
/usr/include/google/protobuf/compiler/python/helpers.h
/usr/include/google/protobuf/compiler/python/pyi_generator.h
/usr/include/google/protobuf/compiler/retention.h
/usr/include/google/protobuf/compiler/ruby/ruby_generator.h
/usr/include/google/protobuf/compiler/rust/accessors/accessor_generator.h
/usr/include/google/protobuf/compiler/rust/accessors/accessors.h
/usr/include/google/protobuf/compiler/rust/context.h
/usr/include/google/protobuf/compiler/rust/generator.h
/usr/include/google/protobuf/compiler/rust/message.h
/usr/include/google/protobuf/compiler/rust/naming.h
/usr/include/google/protobuf/compiler/rust/oneof.h
/usr/include/google/protobuf/compiler/rust/relative_path.h
/usr/include/google/protobuf/compiler/scc.h
/usr/include/google/protobuf/compiler/subprocess.h
/usr/include/google/protobuf/compiler/versions.h
/usr/include/google/protobuf/compiler/versions_suffix.h
/usr/include/google/protobuf/compiler/zip_writer.h
/usr/include/google/protobuf/cpp_edition_defaults.h
/usr/include/google/protobuf/cpp_features.pb.h
/usr/include/google/protobuf/cpp_features.proto
/usr/include/google/protobuf/descriptor.h
/usr/include/google/protobuf/descriptor.pb.h
/usr/include/google/protobuf/descriptor.proto
/usr/include/google/protobuf/descriptor_database.h
/usr/include/google/protobuf/descriptor_legacy.h
/usr/include/google/protobuf/descriptor_visitor.h
/usr/include/google/protobuf/duration.pb.h
/usr/include/google/protobuf/duration.proto
/usr/include/google/protobuf/dynamic_message.h
/usr/include/google/protobuf/empty.pb.h
/usr/include/google/protobuf/empty.proto
/usr/include/google/protobuf/endian.h
/usr/include/google/protobuf/explicitly_constructed.h
/usr/include/google/protobuf/extension_set.h
/usr/include/google/protobuf/extension_set_inl.h
/usr/include/google/protobuf/feature_resolver.h
/usr/include/google/protobuf/field_access_listener.h
/usr/include/google/protobuf/field_mask.pb.h
/usr/include/google/protobuf/field_mask.proto
/usr/include/google/protobuf/generated_enum_reflection.h
/usr/include/google/protobuf/generated_enum_util.h
/usr/include/google/protobuf/generated_message_bases.h
/usr/include/google/protobuf/generated_message_reflection.h
/usr/include/google/protobuf/generated_message_tctable_decl.h
/usr/include/google/protobuf/generated_message_tctable_gen.h
/usr/include/google/protobuf/generated_message_tctable_impl.h
/usr/include/google/protobuf/generated_message_util.h
/usr/include/google/protobuf/has_bits.h
/usr/include/google/protobuf/implicit_weak_message.h
/usr/include/google/protobuf/inlined_string_field.h
/usr/include/google/protobuf/internal_message_util.h
/usr/include/google/protobuf/internal_visibility.h
/usr/include/google/protobuf/io/coded_stream.h
/usr/include/google/protobuf/io/gzip_stream.h
/usr/include/google/protobuf/io/io_win32.h
/usr/include/google/protobuf/io/printer.h
/usr/include/google/protobuf/io/strtod.h
/usr/include/google/protobuf/io/tokenizer.h
/usr/include/google/protobuf/io/zero_copy_sink.h
/usr/include/google/protobuf/io/zero_copy_stream.h
/usr/include/google/protobuf/io/zero_copy_stream_impl.h
/usr/include/google/protobuf/io/zero_copy_stream_impl_lite.h
/usr/include/google/protobuf/json/internal/descriptor_traits.h
/usr/include/google/protobuf/json/internal/lexer.h
/usr/include/google/protobuf/json/internal/message_path.h
/usr/include/google/protobuf/json/internal/parser.h
/usr/include/google/protobuf/json/internal/parser_traits.h
/usr/include/google/protobuf/json/internal/unparser.h
/usr/include/google/protobuf/json/internal/unparser_traits.h
/usr/include/google/protobuf/json/internal/untyped_message.h
/usr/include/google/protobuf/json/internal/writer.h
/usr/include/google/protobuf/json/internal/zero_copy_buffered_stream.h
/usr/include/google/protobuf/json/json.h
/usr/include/google/protobuf/map.h
/usr/include/google/protobuf/map_entry.h
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
/usr/include/google/protobuf/raw_ptr.h
/usr/include/google/protobuf/reflection.h
/usr/include/google/protobuf/reflection_internal.h
/usr/include/google/protobuf/reflection_mode.h
/usr/include/google/protobuf/reflection_ops.h
/usr/include/google/protobuf/repeated_field.h
/usr/include/google/protobuf/repeated_ptr_field.h
/usr/include/google/protobuf/serial_arena.h
/usr/include/google/protobuf/service.h
/usr/include/google/protobuf/source_context.pb.h
/usr/include/google/protobuf/source_context.proto
/usr/include/google/protobuf/string_block.h
/usr/include/google/protobuf/struct.pb.h
/usr/include/google/protobuf/struct.proto
/usr/include/google/protobuf/stubs/callback.h
/usr/include/google/protobuf/stubs/common.h
/usr/include/google/protobuf/stubs/platform_macros.h
/usr/include/google/protobuf/stubs/port.h
/usr/include/google/protobuf/stubs/status_macros.h
/usr/include/google/protobuf/text_format.h
/usr/include/google/protobuf/thread_safe_arena.h
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
/usr/include/google/protobuf/varint_shuffle.h
/usr/include/google/protobuf/wire_format.h
/usr/include/google/protobuf/wire_format_lite.h
/usr/include/google/protobuf/wrappers.pb.h
/usr/include/google/protobuf/wrappers.proto
/usr/include/java/core/src/main/java/com/google/protobuf/java_features.proto
/usr/include/utf8_range.h
/usr/include/utf8_validity.h
/usr/lib64/cmake/protobuf/protobuf-config-version.cmake
/usr/lib64/cmake/protobuf/protobuf-config.cmake
/usr/lib64/cmake/protobuf/protobuf-generate.cmake
/usr/lib64/cmake/protobuf/protobuf-module.cmake
/usr/lib64/cmake/protobuf/protobuf-options.cmake
/usr/lib64/cmake/protobuf/protobuf-targets-relwithdebinfo.cmake
/usr/lib64/cmake/protobuf/protobuf-targets.cmake
/usr/lib64/cmake/utf8_range/utf8_range-config.cmake
/usr/lib64/cmake/utf8_range/utf8_range-targets-relwithdebinfo.cmake
/usr/lib64/cmake/utf8_range/utf8_range-targets.cmake
/usr/lib64/libprotobuf-lite.so
/usr/lib64/libprotobuf.so
/usr/lib64/libprotoc.so
/usr/lib64/pkgconfig/protobuf-lite.pc
/usr/lib64/pkgconfig/protobuf.pc
/usr/lib64/pkgconfig/utf8_range.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libprotobuf-lite.so.25.3.0
/V3/usr/lib64/libprotobuf.so.25.3.0
/V3/usr/lib64/libprotoc.so.25.3.0
/usr/lib64/libprotobuf-lite.so.25.3.0
/usr/lib64/libprotobuf.so.25.3.0
/usr/lib64/libprotoc.so.25.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/protobuf/252c7fd154ca740ae6f765d206fbd9119108a0e3
/usr/share/package-licenses/protobuf/fdd1d72fcc979c32a5ab8ae278a2dfd967faf820

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libutf8_range.a
/usr/lib64/libutf8_validity.a
