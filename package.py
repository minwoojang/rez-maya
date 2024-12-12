# Based and improved from https://github.com/piratecrew/rez-maya

name = "maya"

version = "2023.0.3"

authors = [
    "Autodesk"
]

description = \
    """
    Autodesk Maya offers a comprehensive creative feature set for 3D computer animation, modeling, simulation,
    rendering, and compositing on a highly extensible production platform.
    """

requires = [
    "cmake-3+",
    # "license_manager"
]

variants = [['platform-linux', 'arch-x86_64']]

tools = [
    "maya",
    "maya2013",
    'Render',
    'mayapy',
    'register_maya'
]

has_plugins = True

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "maya-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.PATH.prepend("{root}/maya/bin")
    env.MAYA_LOCATION.set("{root}/maya")

    env.PYTHONPATH.append("/usr/autodesk/maya2023/maya/lib/python3.9/site-packages")
    env.MAYA_VP2_USE_GPU_MAX_TARGET_SIZE.set("1")
    env.ADSKFLEX_LICENSE_FILE="2080@localhost"
    env.MAYA_SCRIPT_PATH = "/cocoa/inhouse/tool/maya"
    import os
    maya_script_path = os.getenv("MAYA_SCRIPT_PATH")
    if maya_script_path:
        env.MAYA_SCRIPT_PATH.append(maya_script_path)

    # Helper environment variables.
    env.MAYA_BINARY_PATH.set("{root}/maya/bin")
    env.MAYA_INCLUDE_PATH.set("{root}/maya/include")
    env.MAYA_LIBRARY_PATH.set("{root}/maya/lib")

