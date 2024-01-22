fh = open('some.txt', 'rt')  # default
data = fh.read()
print(data)
fh.close()

fh = open('some.txt', 'w')
fh.write('Smth\n')
fh.write('SmthOther\n')
fh.close()

# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#
#

fh = open('some.txt', 'r')
# data = fh.read()
data = fh.readlines()  # list of lines
print(data)
fh.close()
