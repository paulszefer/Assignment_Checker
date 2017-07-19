REM This script compiles a list of paths to Java source files
REM found in the directory navigated to. The list is then
REM output to a sources.txt file.

@echo off

REM Navigate to the correct directory
cd %1

REM Redirect a generated list of Java source files to a
REM sources.txt file.
dir /s /B *.java > sources.txt
