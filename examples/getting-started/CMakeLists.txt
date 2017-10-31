#  minimum required cmake version: 3.1.0
cmake_minimum_required(VERSION 3.1.0)

project(RealsenseExamplesGettingStarted)

# Save the command line compile commands in the build output
set(CMAKE_EXPORT_COMPILE_COMMANDS 1)

# Make project require C++11
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif()

# simple non robust way to find the librealsense library
find_library(REALSENSE2_FOUND realsense2)
message(STATUS "REALSENSE2_FOUND = ${REALSENSE2_FOUND}")

# getting-started
add_executable(rs-getting-started rs-getting-started.cpp ../example.hpp)
include_directories(rs-getting-started ../)
target_link_libraries(rs-getting-started realsense2)
set_target_properties (rs-getting-started PROPERTIES
    FOLDER Examples
)

install(
    TARGETS

    rs-getting-started

    RUNTIME DESTINATION
    ${CMAKE_INSTALL_PREFIX}/bin
)
