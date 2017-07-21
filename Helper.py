# ------------------------------------------------------------------
# Helper.py
#
# By: Paul Szefer
#
# This file defines helper functions used by Actions.py.
# ------------------------------------------------------------------

import os
from contextlib import contextmanager


# Returns true if the given path refers to a zip folder
def is_zip_folder(path):
    return path.name.endswith('.zip')


# Returns true if the given file refers to a Java source file
def is_java_source_file(file):
    return file.endswith('.java')


# Returns a string representation of the given byte array.
def decode_to_str(byte_array):
    return byte_array.decode('utf-8')


# Allows for creating a new context in which the current directory is changed
# to the given directory. Upon leaving the context, the current directory
# is returned to the original directory.
@contextmanager
def cd(new_dir):
    original_dir = os.getcwd()
    try:
        os.chdir(new_dir)
        yield
    finally:
        os.chdir(original_dir)
