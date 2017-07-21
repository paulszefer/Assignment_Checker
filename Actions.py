# ------------------------------------------------------------------
# Actions.py
#
# By: Paul Szefer
#
# This file defines the action functions called by
# AssignmentChecker.py.
# ------------------------------------------------------------------

import platform
import subprocess
from Helper import *


# Extracts the Java source files from the given zip folder to a src folder
# in a folder with the given folder name.
def extract_sources(folder_name, zip_folder):
    for _ in zip_folder.filelist:
        zip_folder.extractall(folder_name + '/src/')


# Runs checkstyle on all Java source files found in the src directory and
# generates a report with the output in the same directory as the src
# folder.
#
# The checkstyle jar used is: checkstyle-8.0-all.jar
# The checkstyle configuration file used is: checkstyle_config.xml
# The report file generated is: UserID/checkstyle_report.txt
def run_checkstyle(folder_name):

    # Run checkstyle on the source files
    command = subprocess.Popen(
        'java -jar checkstyle-8.0-all.jar -c checkstyle_config.xml -o '
        + os.path.join(folder_name, 'checkstyle_report.txt') + ' '
        + os.path.join(folder_name, 'src', '*'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    output, errors = command.communicate()

    # Print and log output and errors
    output_str = decode_to_str(output)
    errors_str = decode_to_str(errors)
    print('Checkstyle output:')
    print(output_str)
    print('Checkstyle errors:')
    print(errors_str)

    with open(os.path.join(folder_name, 'checkstyle_report.txt'), 'a') as checkstyle_log:
        checkstyle_log.write('\r\n' + output_str)
        checkstyle_log.write('\r\n' + errors_str)


# Compiles all Java source files found in the src directory to a bin
# folder in the given directory. Compilation errors are recorded in
# the same directory.
#
# The report file generated is: UserID/compile_errors.txt
def compile_sources(folder_name):

    # Generate the bin folder for compiled files
    os.makedirs(str(folder_name).replace('.zip', '') + '/bin/', exist_ok=True)

    with open(folder_name + '/compile_errors.txt', 'w') as error_log:

        # Generate a space-delimited string of the Java source files
        sources = ''
        for dir_ in os.listdir(os.path.join(folder_name, 'src')):
            if os.path.isdir(os.path.join(folder_name, 'src', dir_)):
                for file_ in os.listdir(os.path.join(folder_name, 'src', dir_)):
                    if is_java_source_file(file_):
                        sources += os.path.join(folder_name, 'src', dir_, file_) + ' '

        # Compile the collection of Java source files
        command = subprocess.Popen(
            'javac -d ' + folder_name + '/bin/ ' + sources,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        output, errors = command.communicate()

        # Print and log output and errors
        output_str = decode_to_str(output)
        errors_str = decode_to_str(errors)
        print('Compile output:')
        print(output_str)
        print('Compile errors:')
        print(errors_str)

        if errors_str == "":
            error_log.write('No errors')
        else:
            error_log.write(errors_str)


# Executes the main classes referenced in assignment_config/class_list.txt.
# If an input file is provided, then it will be redirected to standard input
# of the executing class. The execution output is directed to
# UserID/output.txt.
def execute_projects(folder_name):

    with open(os.path.join('assignment_config', 'class_list.txt'), 'r') as class_list:

        # Execute each listed class (with the stated input file, if given)
        for line in class_list.readlines():
            class_name = line.split()[0]
            class_input_path = ''
            if len(line.split()) == 2:
                class_input_path = os.path.join('..', '..', 'assignment_config', line.split()[1])

            with open(os.path.join(folder_name, 'output.txt'), 'a') as output_file:

                print("Executing " + class_name)
                with cd(os.path.join(folder_name, 'bin')):
                    if class_input_path == '':
                        command = subprocess.Popen(
                            'java ' + class_name,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
                    else:
                        if platform.system() == 'Windows':
                            # PowerShell is now the default command line interface for Windows,
                            # but it does not support file redirection with '<'
                            command = subprocess.Popen(
                                'cmd /c java ' + class_name + ' < ' + class_input_path,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
                        else:
                            command = subprocess.Popen(
                                'java ' + class_name + ' < ' + class_input_path,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

                    # Print and log output and errors
                    output, errors = command.communicate()
                    output_str = decode_to_str(output)
                    errors_str = decode_to_str(errors)
                    print('Execute output: ' + output_str)
                    print('Execute errors: ' + errors_str)
                    output_file.write(output_str)
