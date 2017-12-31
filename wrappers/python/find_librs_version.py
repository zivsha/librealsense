import io
import re

librs_version = ''
with io.open('librealsense/include/librealsense2/rs.h', 'r') as f:
    file_content = f.read()
    major = re.search(r"#define\s*RS2_API_MAJOR_VERSION\s*(\d+)",file_content)
    if not major:
        raise Exception('No major number')
    librs_version += major.group(1)
    librs_version += '.'
    minor = re.search(r"#define\s*RS2_API_MINOR_VERSION\s*(\d+)",file_content)
    if not minor:
        raise Exception('No minor number')
    librs_version += minor.group(1)
    librs_version += '.'
    patch = re.search(r"#define\s*RS2_API_PATCH_VERSION\s*(\d+)",file_content)
    if not patch:
        raise Exception('No patch number')
    librs_version += patch.group(1)

print("Librealsense Version: ", librs_version)

with open('librealsense/wrappers/python/rs_version.py', 'w') as f:
    f.write('librs_version = "{}"'.format(librs_version))
