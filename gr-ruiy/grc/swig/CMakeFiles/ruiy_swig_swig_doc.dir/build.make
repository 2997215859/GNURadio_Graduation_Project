# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ruiy/gnuradio/gr-ruiy

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ruiy/gnuradio/gr-ruiy/grc

# Utility rule file for ruiy_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/ruiy_swig_swig_doc.dir/progress.make

swig/CMakeFiles/ruiy_swig_swig_doc: swig/ruiy_swig_doc.i

swig/ruiy_swig_doc.i: swig/ruiy_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ruiy/gnuradio/gr-ruiy/grc/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating python docstrings for ruiy_swig_doc"
	cd /home/ruiy/gnuradio/gr-ruiy/docs/doxygen && /usr/bin/python2 -B /home/ruiy/gnuradio/gr-ruiy/docs/doxygen/swig_doc.py /home/ruiy/gnuradio/gr-ruiy/grc/swig/ruiy_swig_doc_swig_docs/xml /home/ruiy/gnuradio/gr-ruiy/grc/swig/ruiy_swig_doc.i

swig/ruiy_swig_doc_swig_docs/xml/index.xml: swig/_ruiy_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ruiy/gnuradio/gr-ruiy/grc/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for ruiy_swig_doc docs"
	cd /home/ruiy/gnuradio/gr-ruiy/grc/swig && ./_ruiy_swig_doc_tag
	cd /home/ruiy/gnuradio/gr-ruiy/grc/swig && /usr/bin/doxygen /home/ruiy/gnuradio/gr-ruiy/grc/swig/ruiy_swig_doc_swig_docs/Doxyfile

ruiy_swig_swig_doc: swig/CMakeFiles/ruiy_swig_swig_doc
ruiy_swig_swig_doc: swig/ruiy_swig_doc.i
ruiy_swig_swig_doc: swig/ruiy_swig_doc_swig_docs/xml/index.xml
ruiy_swig_swig_doc: swig/CMakeFiles/ruiy_swig_swig_doc.dir/build.make
.PHONY : ruiy_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/ruiy_swig_swig_doc.dir/build: ruiy_swig_swig_doc
.PHONY : swig/CMakeFiles/ruiy_swig_swig_doc.dir/build

swig/CMakeFiles/ruiy_swig_swig_doc.dir/clean:
	cd /home/ruiy/gnuradio/gr-ruiy/grc/swig && $(CMAKE_COMMAND) -P CMakeFiles/ruiy_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/ruiy_swig_swig_doc.dir/clean

swig/CMakeFiles/ruiy_swig_swig_doc.dir/depend:
	cd /home/ruiy/gnuradio/gr-ruiy/grc && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ruiy/gnuradio/gr-ruiy /home/ruiy/gnuradio/gr-ruiy/swig /home/ruiy/gnuradio/gr-ruiy/grc /home/ruiy/gnuradio/gr-ruiy/grc/swig /home/ruiy/gnuradio/gr-ruiy/grc/swig/CMakeFiles/ruiy_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/ruiy_swig_swig_doc.dir/depend

