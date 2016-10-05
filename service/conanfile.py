from conans import ConanFile, CMake

class LocalCourseServiceConan(ConanFile):
    name = "local_course_service"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    exports = "src/*","include/*","CMakeLists.txt","README.md"
    requires = "street_environment/1.0@lms/stable","lms/2.0@lms/stable","phoenix_service/1.0@lms/stable","lms_line_fitting/1.0@lms/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include",src="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")
        self.copy("*.so",dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["local_course_service"]
