"""
Previously programmers use this method but now
         This one is not preferable.
========================================================================
modes:
------------------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
========================================================================
"""
try:
    file = open('01.previous_method.txt', 'w+')
    file.write(open.__doc__)     # Write documentation of open function
    print("Writing successful.")

except Exception as e:
    print("File Error: ", e)

finally:                # Always use finally to close file
    file.close()

