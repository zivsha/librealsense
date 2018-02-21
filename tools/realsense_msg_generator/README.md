# Realsense ROS-Message Generator

ROS uses a simplified messages description language for describing the data values (aka messages) that ROS nodes publish. 
This description makes it easy for ROS tools to automatically generate source code for the message type in several target languages. 
Message descriptions are stored in .msg files.
There are two parts to a .msg file: fields and constants. Fields are the data that is sent inside of the message. 
Constants define useful values that can be used to interpret those fields (e.g. enum-like constants for an integer value).

Additional information can be found [here](http://wiki.ros.org/message_generation).

This tool allows creation of proprietary ROS messages.
The messages used with this tool are used as part of the [RealSense SDK](https://github.intel.com/PercHW/librealsense) media files


--------------
### Dependencies

In order for the tool to work the following [ROS CATKIN](http://wiki.ros.org/catkin) componenets are required:
- message_generation 
- std_msgs 
- sensor_msgs 

--------------
### How to use the tool

1. Clone this repo
2. Run `./build.sh` (might need to run `chmod a+x build.sh` before) 
3. Auto generated file will be dropped to `output` folder

--------------

### Generated Messages

This tool currently generates the following Realsense messages:

 - [StreamInfo](#stream-info)
 - [ImuIntrinsic](#motion-intrinsic)
 - [Notification](#notification)

--------------

# This message defines meta information for a stream

#### Stream Info

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Format</th>
  </tr>
    <tr>
      <td>is_recommended</td>
      <td>Indicates if this stream is recommended by RealSense SDK</td>
      <td>bool</td>
    </tr>
  <tr>
    <td>fps</td>
    <td>Frame per second value</td>
    <td>uint32</td>
  </tr>
  <tr>
    <td>encoding</td>
    <td>Stream's data format<br>
    [Supported encoding are listed below](#supported-encoding)</td>
    <td>string</td>
  </tr>
</table>

[:arrow_up: Back to Top](#generated-messages)

##### Supported Encoding

For video streams, the supported encoding types can be found at <a href="http://docs.ros.org/jade/api/sensor_msgs/html/namespacesensor__msgs_1_1image__encodings.html">ros documentation</a><br>
IMU encodings are:
- "XYZ-32" : Three 32-bit floating point values

[:arrow_up: Back to Top](#generated-messages)

--------------

#### Motion Intrinsics

<table>
   <tbody>
      <tr>
         <th>Name</th>
         <th>Description</th>
         <th>Format</th>
      </tr>
      <tr>
         <td>&nbsp;data</td>
         <td>
            <p>Interpret data array values</p>
            <table>
               <tbody>
                  <tr>
                     <td>Scale X</td>
                     <td>Cross Axis</td>
                     <td>Cross Axis</td>
                     <td>Bias X</td>
                  </tr>
                  <tr>
                     <td>Cross Axis</td>
                     <td>Scale Y</td>
                     <td>Cross Axis</td>
                     <td>Bias Y</td>
                  </tr>
                  <tr>
                     <td>Cross Axis</td>
                     <td>Cross Axis</td>
                     <td>Scale Z</td>
                     <td>Cross Axis</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td>float32[12]</td>
      </tr>
      <tr>
         <td>noise_variances</td>
         <td>Variance of noise for X, Y, and Z axis</td>
         <td>float32[3]</td>
      </tr>
      <tr>
         <td>bias_variances</td>
         <td>Variance of bias for X, Y, and Z axis</td>
         <td>float32[3]</td>
      </tr>
   </tbody>
</table>

[:arrow_up: Back to Top](#generated-messages)

--------------

#### Notification

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Format</th>
  </tr>
    <tr>
      <td>timestamp</td>
      <td>The time of occurance </td>
      <td>RosTime</td>
    </tr>
  <tr>
    <td>categroy</td>
    <td>The category of the notification</td>
    <td>string</td>
  </tr>
  <tr>
    <td>severity</td>
    <td>The severity of the notification</td>
    <td>string</td>
  </tr>
    <tr>
    <td>description</td>
    <td>Human readable description of the notification</td>
    <td>string</td>
  </tr>
    <tr>
    <td>serizlied_data</td>
    <td>JSON string with additional data</td>
    <td>string</td>
  </tr>
</table>

[:arrow_up: Back to Top](#generated-messages)

--------------