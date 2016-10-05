cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES
    "src/local_course.cpp"
    "src/interface.cpp"
    "src/matlab_kalman.cpp"
    "src/ekf.cpp"
)

set(HEADERS
    "include/local_course/local_course.h"
    "include/local_course/matlab_kalman.h"
    "include/local_course/ekf.h"
)
include_directories(
        include
        /usr/local/include
        /usr/include
        /usr/local/include/eigen3
        /usr/include/eigen3
        /usr/include/qt5

)

#set compiler flags
if((${CMAKE_CXX_COMPILER_ID} STREQUAL "Clang") OR (${CMAKE_CXX_COMPILER_ID} STREQUAL "GNU"))
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -Wreturn-type -Wpedantic ")
endif()

set(KALMAN "Matlab/codegen/lib/kalman_filter_lr")
include_directories("include")
include_directories("${KALMAN}")
file(GLOB kalman "${KALMAN}/*.cpp" "${KALMAN}/*.h")
add_library(local_course_service SHARED ${SOURCES} ${HEADERS} ${kalman})
target_link_libraries(local_course_service PRIVATE ${CONAN_LIBS})
