# goit-algo-hw-03

# Task 1

Write a Python program that recursively copies files from a source directory, moves them to a new directory, and sorts them into subdirectories based on their file extensions.

Also, take the following requirements into account:

1. Argument parsing
   The script should accept two command-line arguments:

The path to the source directory.

The path to the destination directory.

If the destination path is not provided, it should default to a directory named dist.

2. Recursive directory traversal
   There should be a function that takes a directory path as an argument.

This function should iterate over all items in the directory.

If an item is a directory, the function should call itself recursively on that subdirectory.

If an item is a file, it should be prepared for copying.

3. File copying
   For each file type (based on extension), a new path in the destination directory should be created using the file extension as the subdirectory name.

The file should then be copied into the corresponding subdirectory.

4. Exception handling
   The code should handle exceptions correctly, such as access errors to files or directories.
