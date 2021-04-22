# 配置CMAKE环境
- 1、安装cmake，cmake tools插件
- 2、创建CMakeLists.txt文件
```cmake
cmake_minimum_required(VERSION 2.8)
project(vs_project_test)#工程名称
SET(MODULE_NAME "hello_pcl")
set(CMAKE_BUILD_TYPE "Debug" ) # 调试模式
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
find_package(Eigen3 REQUIRED)
include_directories(
        ${EIGEN3_INCLUDE_DIR}
)
FILE(GLOB_RECURSE SRC_FILES ./source/*.cpp ./src/*.cpp)

include_directories(/usr/include/pcl-1.7)

add_executable(${MODULE_NAME} ${SRC_FILES}) # 测试代码
```
- 3、配置.vscode/launch.json,增加一条
```json
{
    "name": "(gdb) Launch",
    "type": "cppdbg",
    "request": "launch",
    "program": "${workspaceFolder}/parking/build/hello_pcl",
    "args": [],
    "stopAtEntry": false,
    "cwd": "${workspaceFolder}/parking",
    "environment": [],
    "externalConsole": false,
    "MIMode": "gdb",
    "setupCommands": [
        {
            "description": "Enable pretty-printing for gdb",
            "text": "-enable-pretty-printing",
            "ignoreFailures": true
        }
    ],
    "preLaunchTask": "make"   # 与task中的label名一致
},
```
- 4、配置task.json
```json
{
    "tasks": [
        {
            "label": "make",
            "type": "shell",
            "command": "sh /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city/project/parking/build.sh"
        }
    ],
    "version": "2.0.0"
}
```
- 5、新增build.sh
```bash
cd /media/l/e6aa5997-4a1e-42e4-8782-83e2693751bd/city/project/parking/build
rm -rf *
cmake ..
make -j4
```