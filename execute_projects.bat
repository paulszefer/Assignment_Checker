@echo off
cd %1
cd bin
IF [%3] == [] (
    java %2
) ELSE (
    java %2 < ../../assignment_config/%3
)
