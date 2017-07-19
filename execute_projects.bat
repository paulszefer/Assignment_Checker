REM This script executes the Java class files provided
REM and redirects an input file to standard input, if provided.

@echo off

REM Navigate to correct directory
cd %1
cd bin

REM Execute the class file, or execute and redirect a given
REM input file.
IF [%3] == [] (
    java %2
) ELSE (
    java %2 < ../../assignment_config/%3
)
