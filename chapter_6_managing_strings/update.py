quote = "'It's the economy stupid.' (James Carville, 1992)"

# When working with files it''s good prcactice to group file operational statments with the 'with' keyword.
# This ensures the file is properly closed aftrer operations end.
with open('chapter_6_managing_strings/quote.txt', 'w') as file:
    file.write(quote)
    print("\nFile now closed?\t", file.closed)

# Closes the file, and confirm through Boolean closed property.
file.close()
print("File now closed?\t", file.closed)

# Re-opens the file in read plus mode to confirm the contents.
with open('chapter_6_managing_strings/quote.txt', 'r+') as file:
    contents = file.read()
    print("\n",contents)
    file.close()
print("File now closed?\t", file.closed)

# The seek() method accepts an integer argument to determine how many characters from 0 to start from.
# The tell() methods returns an integer.
# With the seek() method it will go to the character postion. The code then writes 'silly' from that position. 
with open('chapter_6_managing_strings/quote.txt', 'r+') as file:
    contents = file.read()
    file.write("\n")
    file.write(quote)
    print(contents)

    file.seek(70)
    print("\nPosition in file now:\t", file.tell())
    file.write("silly")
    print(contents)
    file.close()
print("File now closed?\t", file.closed)
print("\n====")
with open('chapter_6_managing_strings/quote.txt', 'r') as file:
    contents = file.read()
    print("\n", contents)

# This will find and replace a specific word.
# string.replace(oldvalue, newvalue, count)
print("\n==== BONUS ====")
print("Quote:\t", quote)
new_quote = quote.replace("economy", "banana")
print("New Quote:\t", new_quote)