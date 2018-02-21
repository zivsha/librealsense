##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(realsense_msgs)
set(CMAKE_PREFIX_PATH /opt/ros/kinetic)
##############################################################################
# Dependencies
##############################################################################

find_package(catkin REQUIRED COMPONENTS 
    message_generation std_msgs sensor_msgs
)

##############################################################################
# Messgaes
##############################################################################

file(GLOB_RECURSE rs_messages RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "msg/*.msg")
string(REPLACE "msg/" "" RS_MSGS "${rs_messages}")
message(STATUS "RS_MSGS : ${RS_MSGS}")

add_message_files(
  DIRECTORY msg
  FILES
  ${RS_MSGS}
)


generate_messages(DEPENDENCIES std_msgs sensor_msgs)

##############################################################################
# Package
##############################################################################

catkin_package(
	CATKIN_DEPENDS message_runtime std_msgs sensor_msgs
)
