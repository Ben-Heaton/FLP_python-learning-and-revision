# Opening the file & using the write mode.
file = open('chapter_6_managing_strings/read_example.txt', 'w') # If you just have a file name, a new file is made in the directory above.

# Displays to the console the file name and mode
print('File Name:\t', file.name)
print('File Open Mode:\t', file.mode)

# Display the file access permissions
print("Readable:\t", file.readable())
print("Writable:\t", file.writable())

# A function that determines a file's status
def get_status(filename):
    if (filename.closed == True):
        return "Closed"
    else:
        return "Open"

# Displays to console current file status, closes file, displays status.
print("File status:\t", get_status(file))
file.close()
print("File status:\t", get_status(file))