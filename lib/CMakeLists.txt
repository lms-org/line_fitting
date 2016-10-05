cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES
# src/foo.cpp
)

set(HEADERS
    include/kalman_filter/ctra_measurement_model.h
    include/kalman_filter/ctra_system_model.h
    include/kalman_filter/line_ekf.h
    include/kalman_filter/ctra_ekf.h
    include/kalman_filter/mass_ekf.h
    include/filter/line_line_x.h
    include/filter/sgd.h
    include/filter/adam.h
    include/utils.h
)


include_directories(include)
#set compiler flags
if((${CMAKE_CXX_COMPILER_ID} STREQUAL "Clang") OR (${CMAKE_CXX_COMPILER_ID} STREQUAL "GNU"))
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -Wreturn-type -Wpedantic ")
endif()

add_library(lms_line_fitting SHARED ${SOURCES} ${HEADERS})
target_link_libraries(lms_line_fitting PRIVATE ${CONAN_LIBS})


#TODO just for testing
#QT
# Find includes in corresponding build directories
#set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed.
#set(CMAKE_AUTOMOC ON)

# Find the QtWidgets library
#find_package(Qt5Core)
#find_package(Qt5Widgets)
#find_package(Qt5Charts)

#add_executable(km
#    ${SOURCES} ${HEADERS}
#)

#target_link_libraries(km PRIVATE Qt5::Widgets Qt5::Charts Qt5Core)

#target_link_libraries(kalman_filter PRIVATE lmscore)
#add_library(kalman_filter SHARED ${SOURCES} ${HEADERS})
#target_link_libraries(kalman_filter PRIVATE lmscore)
