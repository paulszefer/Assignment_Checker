# Assignment_Checker
Assignment_Checker processes Java assignments. 

This will generate a folder for each zip file assignment, processed accordingly.

# Run Instructions

The project can be downloaded in whole and run using AssignmentChecker.py.
The checkstyle jar is not included; you will need to download <a href="https://sourceforge.net/projects/checkstyle/files/checkstyle/">checkstyle-8.0-all.jar</a>
and put it in the same directory as AssignmentChecker.py

Required folders/files for running AssignmentChecker.py are:
- AssignmentChecker.py
- Helper.py
- assignment_config/run_structure.txt (plus any input files for file redirection)
- <a href="https://sourceforge.net/projects/checkstyle/files/checkstyle/">checkstyle-8.0-all.jar</a>
- checkstyle_config.xml (can be replaced by any checkstyle configuration file renamed to this)
- suppressions.xml
- get_sources.bat
- execute_projects.bat
- ZIP folders to process

# Configuration Instructions
To configure the main classes that need to be run, use the run_structure.txt file inside the assignment_config folder.
One class can be referenced per line.

To add an input text file to redirect to the program at execution time, add it after a space in the run_structure.txt file.

Example:

q1/TriangleArea

Example with file redirect:

q1/TriangleArea triangle_area_input.txt

# Example Assignments
- A00123456.zip has no checkstyle warnings and no compiler errors
- A00234566.zip fails to complete the checkstyle check due to compile errors
- A00345678.zip has various checkstyle warnings and no compiler errors
