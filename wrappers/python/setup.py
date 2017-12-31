from setuptools import setup, find_packages
from setuptools.dist import Distribution
import os
import io
import re

package_name = "pyrealsense2"
package_data = {}

def get_version():
    with io.open('../../include/librealsense2/rs.h', 'r') as f:
        file_content = f.read()
        major = re.search(r"#define\s*RS2_API_MAJOR_VERSION\s*(\d+)",file_content).group(1)
        minor = re.search(r"#define\s*RS2_API_MINOR_VERSION\s*(\d+)",file_content).group(1)
        micro = re.search(r"#define\s*RS2_API_PATCH_VERSION\s*(\d+)",file_content).group(1)
        return major + '.' + minor + '.' + micro

def load_readme():
     with io.open('README.rst', encoding="utf-8") as f:
        return f.read()

if os.name == 'posix':
    package_data[package_name] = ['*.so']
else:
    package_data[package_name] = ['*.pyd', '*.dll']

package_data[package_name] += ["LICENSE.txt"]

setup(
    name=package_name,
    version=get_version(),
    author='Intel(R) RealSense(TM)',
    author_email='realsense@intel.com',
    url='https://github.com/IntelRealSense/librealsense',
    scripts=['examples/align-depth2color.py',
            'examples/export_ply_example.py',
            'examples/opencv_viewer_example.py',
            'examples/python-rs400-advanced-mode-example.py',
            'examples/python-tutorial-1-depth.py'
    ],
    license='Apache License, Version 2.0',
    description='Python Wrapper for Intel Realsense SDK 2.0.',
    long_description=load_readme(),
    install_requires=[],
    include_package_data=True,
    packages=find_packages(),
    package_data=package_data
)
