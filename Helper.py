import os
import subprocess


# Returns true if the given path refers to a zip folder
def is_zip_folder(path):
    return has_extension(path, 'zip')


# Returns true if the given path refers to a Java source file
def is_java_source_file(path):
    return has_extension(path, 'java')


# Returns true if the given path refers to a file with the given extension
def has_extension(path, ext):
    return path.name.endswith(ext)


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
# The report file generated is: checkstyle_report.txt
def run_checkstyle(folder_name):
    command = subprocess.Popen(
        'java -jar checkstyle-8.0-all.jar -c checkstyle_config.xml -o ' + folder_name + '/checkstyle_report.txt ' + folder_name + '/src/*',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    output, errors = command.communicate()
    output_str = decode_to_str(output)
    errors_str = decode_to_str(errors)
    print('Checkstyle output: ' + output_str)
    print(output_str)
    print('Checkstyle errors: ' + errors_str)
    print(errors_str)

    checkstyle_log = open(folder_name + '/checkstyle_report.txt', 'a')
    checkstyle_log.write('\r\n' + output_str)
    checkstyle_log.write('\r\n' + errors_str)
    checkstyle_log.close()


# Compiles all Java source files found in the src directory to a bin
# folder a folder with the given folder name. Compilation errors
# are recorded in a file in the same directory
# as the bin folder.
#
# The report file generated is: compile_errors.txt
def compile_sources(folder_name):
    subprocess.Popen('get_sources.bat ' + folder_name)

    os.makedirs(str(folder_name).replace('.zip', '') + '/bin/', exist_ok=True)
    command = subprocess.Popen(
        'javac -d ' + folder_name + '/bin/ @' + folder_name + '/sources.txt',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    output, errors = command.communicate()
    output_str = decode_to_str(output)
    errors_str = decode_to_str(errors)
    print('Compile output: ' + output_str)
    print('Compile errors: ' + errors_str)

    error_log = open(folder_name + '/compile_errors.txt', 'w')
    if errors_str == "":
        error_log.write('No errors')
    else:
        error_log.write(errors_str)
    error_log.close()


def execute_projects(folder_name):
    structure_file = open('assignment_config/run_structure.txt', 'r')
    for line in structure_file.readlines():
        print("Executing " + line.split()[0])
        command = subprocess.Popen('execute_projects.bat ' + folder_name + ' ' + line,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        output, errors = command.communicate()
        output_str = decode_to_str(output)
        errors_str = decode_to_str(errors)
        print('Execute output: ' + output_str)
        print('Execute errors: ' + errors_str)

        with open(folder_name + '/output.txt', 'a') as output_file:
            output_file.write(output_str)
            output_file.close()
    structure_file.close()


# Returns a string with the byte characters removed.
# These byte characters consist of:
#   b' to start the string
#   '  to end the string
def decode_to_str(byte_array):
    return byte_array.decode('utf-8')
