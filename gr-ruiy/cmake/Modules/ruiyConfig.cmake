INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RUIY ruiy)

FIND_PATH(
    RUIY_INCLUDE_DIRS
    NAMES ruiy/api.h
    HINTS $ENV{RUIY_DIR}/include
        ${PC_RUIY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RUIY_LIBRARIES
    NAMES gnuradio-ruiy
    HINTS $ENV{RUIY_DIR}/lib
        ${PC_RUIY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RUIY DEFAULT_MSG RUIY_LIBRARIES RUIY_INCLUDE_DIRS)
MARK_AS_ADVANCED(RUIY_LIBRARIES RUIY_INCLUDE_DIRS)

