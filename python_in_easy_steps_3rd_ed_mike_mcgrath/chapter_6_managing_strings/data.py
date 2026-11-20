# importing the 'pickle' and 'os' modules to for data storage and checking is the file exists respectively.
import pickle, os

# Checks to see IF the pickle data exists or not.
if not os.path.isfile('chapter_6_managing_strings/pickle.dat'):
    
    # If not found creates a list.
    data = [0, 1]

    # Asks users to input data which is assigned to the list.
    data[0] = input("Enter Topic: ")
    data[1] = input("Enter Series: ")

    # Creates a binary file for writing the data to. The 'wb' mode means 'write-binary'.
    file = open('pickle.dat', 'wb')

    # Stores the data in the file.
    pickle.dump(data, file)

    # Make sure to close the file
    file.close()

    # ELSE the file exists, do this. The 'rb' mode means 'read-binary'.
else:
    file = open('chapter_6_managing_strings/pickle.dat', 'rb')

    # Load the data stored into a variable, then close it.
    data = pickle.load(file)
    file.close()
    print("\nWelcome back to:", data[0], data[1])