from conan import ConanFile
from conan.tools.cmake import cmake_layout


class PerspectiveServerConan(ConanFile):
    name = "perspective-server"
    version = "4.3.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualBuildEnv"

    def requirements(self):
        # Latest versions with pre-built MSVC 194 binaries on conancenter
        # (shared=False, runtime=dynamic, cppstd=17).
        self.requires("arrow/22.0.0")
        self.requires("protobuf/6.33.5")
        self.requires("re2/20251105")
        self.requires("abseil/20260107.1", force=True)
        self.requires("rapidjson/cci.20230929")
        self.requires("boost/1.86.0")
        self.requires("date/3.0.4")
        self.requires("tsl-hopscotch-map/2.3.1")
        self.requires("tsl-ordered-map/1.1.0")
        self.requires("exprtk/0.0.2")

    def configure(self):
        # Boost: header-only avoids compiling Boost libraries.
        self.options["boost"].header_only = True

        # Arrow: enable CSV (required - used for CSV parsing/export).
        # Only Arrow builds from source; all other deps use pre-built.
        self.options["arrow"].with_csv = True
        self.options["arrow"].with_json = False
        self.options["arrow"].parquet = False
        self.options["arrow"].with_flight_rpc = False
        self.options["arrow"].gandiva = False
        self.options["arrow"].with_re2 = False
        self.options["arrow"].with_utf8proc = False
        self.options["arrow"].with_brotli = False
        self.options["arrow"].with_bz2 = False
        self.options["arrow"].with_lz4 = False
        self.options["arrow"].with_snappy = False
        self.options["arrow"].with_zlib = False
        self.options["arrow"].with_zstd = False
        self.options["arrow"].with_thrift = False

    def layout(self):
        cmake_layout(self)
