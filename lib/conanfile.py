from conans import ConanFile, CMake

class LineFittingConan(ConanFile):
    name = "lms_line_fitting"
    version = "1.0"
    settings = None
    exports = "include/*","src/*","README.md","CMakeLists.txt"
    requires = "Eigen3/3.2.8@bilke/stable"

    def package(self):
        self.copy("*.h", dst="include", src="include")
