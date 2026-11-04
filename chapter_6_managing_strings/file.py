poem = "\nShall I compare thee to a summer’s day?"
poem += "\nThou art more lovely and more temperate."
poem += "\nRough winds do shake the darling buds of May,"
poem += "\nAnd summer’s lease hath all too short a date."
poem += "\nSometime too hot the eye of heaven shines,"
poem += "\nAnd often is his gold complexion dimmed;"
poem += "\nAnd every fair from fair sometime declines,"
poem += "\nBy chance, or nature’s changing course, untrimmed;"
poem += "\nBut thy eternal summer shall not fade,"
poem += "\nNor lose possession of that fair thou ow’st,"
poem += "\nNor shall death brag thou wand’rest in his shade,"
poem += "\nWhen in eternal lines to Time thou grow’st."
poem += "\nSo long as men can breathe, or eyes can see,"
poem += "\nSo long lives this, and this gives life to thee."

# Open the poem file in write mode.
file = open('chapter_6_managing_strings/poem.txt', 'w')

# Write the poem variable (in this file) to the poem.txt file, then close it.
file.write(poem)
file.close()

# Open the new poem file in read mode, and prints to the console the lines.
file = open('chapter_6_managing_strings/poem.txt', 'r')

for line in file:
    print(line)
file.close()

# Open the new poem file in write mode, appends the author, then closes.
file = open('chapter_6_managing_strings/poem.txt', 'w')
file.write("\n(Author: William Shakespeare)")
file.close()

# Open the new poem file in read mode and prints the lines.
file = open('chapter_6_managing_strings/poem.txt', 'r')
for line in file:
    print(line)
file.close()