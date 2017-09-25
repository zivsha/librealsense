{
  'variables': {
    'build_arch': '<!(node -p "process.arch")',
  },
  "targets": [
    {
      "target_name": "node_librealsense",
      "variables": {
      },
      "sources": [
        "./src/addon.cpp",
      ],
      "include_dirs": [
         "../../include",
         "<!(node -e \"require('nan')\")",
      ],
      "cflags!": [
        "-fno-exceptions"
      ],
      "cflags": [
        "-Wno-deprecated-declarations",
        "-Wno-switch",
        "-std=c++11",
        "-fstack-protector-strong",
        "-fPIE -fPIC",
        "-O2 -D_FORTIFY_SOURCE=2",
        "-Wformat -Wformat-security"
      ],
      "cflags_cc!": [
        "-fno-exceptions"
      ],
      "cflags_cc": [
        "-Wno-switch",
        "-Wno-deprecated-declarations"
      ],
      "conditions": [
        [
          "OS==\"win\"",
          {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'WarnAsError': 'false',
                'DisableSpecificWarnings': ['4996', '4244'],
                'SuppressStartupBanner': 'true',
              }
            },
            "libraries": [
              # TODO: Identify builddir and buildtype
              "<(module_root_dir)/../../build/Debug/realsense2.lib",
            ],
          }
        ],
        [
          "OS!=\"win\"",
          {
            "libraries": [
              "-lrealsense2"
            ],
            'ldflags': [
              # rpath for build from source
              '-Wl,-rpath,\$$ORIGIN/../../../../build',
              '-L<(module_root_dir)/../../build',
              # rpatch for build debian package
              '-Wl,-rpath,\$$ORIGIN/../../../../obj-x86_64-linux-gnu',
              '-L<(module_root_dir)/../../obj-x86_64-linux-gnu'
            ],
            "cflags+": [
              "-std=c++11"
            ],
            "cflags_c+": [
              "-std=c++14"
            ],
            "cflags_cc+": [
              "-std=c++14"
            ]
          }
        ]
      ]
    },
    {
      "target_name": "copy_dll",
      "type":"none",
      "dependencies" : [ "node_librealsense" ],
      "conditions": [
        ['OS=="win"', {
           "copies":
            [
              {
                'destination': '<(module_root_dir)/build/Release',
                'files': ['<(module_root_dir)/../../build/Debug/realsense2.dll']
              }
            ]
        }]
      ]
    }
  ]
}
