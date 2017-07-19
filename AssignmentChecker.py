# ------------------------------------------------------------------
# AssignmentChecker.py
#
# By: Paul Szefer
#
# This program processes Java assignments.
#
# The assignment will consist of a zip folder containing one or
# more packages of Java projects.
#
# 1. A new folder named after the UserID will be created in the
# same directory as the zip folder.
# 2. The source files will be extracted from the zip folder
# into a src folder within the UserID folder, maintaining their
# package structure.
# 3. Checkstyle will be run across all of the Java source files
# and a report named checkstyle_report will be created in the
# UserID folder.
# 4. The source files will be compiled into a bin folder inside
# the UserID folder, with a file named compile_errors storing
# all errors occurring during compilation.
# 5. Each source file package will be executed. If an input file
# is provided, it will be redirected to standard input of the
# applicable class at execution time.
#
# Assignments have the following structure:
#
#   (UserID).zip
#       |
#       |-------(package1)------(java sources), (other resources)
#       |
#       |-------(package2)------(java sources), (other resources)
#       |
#       |-------(package3)------(java sources), (other resources)
#       |
#       ...
#       |
#       readme.txt
#
# TODO - check for/handle incorrect submission zip format
# TODO - consider issue with discarding standard input by
# TODO -     creating a new Scanner
#
# ------------------------------------------------------------------

from pathlib import Path
import zipfile
from Helper import *


# The point of entry into the program.
def main():
    for zipFolder in filter(is_zip_folder, Path().iterdir()):
        folder_name = zipFolder.name.rstrip('.zip')
        print('Processing assignment for: ' + folder_name)

        with zipfile.ZipFile(str(zipFolder)) as this_zip:
            extract_sources(folder_name, this_zip)

            run_checkstyle(folder_name)

            compile_sources(folder_name)

            execute_projects(folder_name)


# Begins execution with the main() method
print('Assignment processing beginning...')
main()
print('Assignment processing finished.')
