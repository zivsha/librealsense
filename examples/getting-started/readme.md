# Getting Started Example

## Overview

The Getting Started example is a simple stand-alone example that requires only librealsense headers and library without additional third party dependencies. 

You can take this project as is, build and compile it in a seperate directory and it should simply work and allow you to play with the code.

## Expected Output

The application should open console and print a single line indicating the distance of the center pixel from the camera.

<p align="center"><img src="expected_output.PNG" alt="expected_output image"/></p>

## How to start?

1. Copy the `rs-getting-started` folder to your desired location
2. open terminal in your folder
3. run:
   - `mkdir build`
   - `cd build`
   - `cmake ../`
   - `make -j4`
   - `./rs-getting-started`