"""
ASCII = The original 128-character set. Basically the letters, numbers,
punctuation, and control characters found on an English keyboard.

Non-ASCII = Any character that is not part of ASCII, including letters
from other languages, currency symbols, mathematical symbols, and emojis.

Unicode = A universal character system. It assigns a unique code point
to virtually every character and symbol used around the world.

UTF-8 = An encoding that defines how Unicode characters are stored as
bytes in memory and files.
"""

s = "Röd"
print("\nRed String:", s)
print("Type:", type(s), "\tLength:", len(s))

# Encoding the string. Converts it from the default unicode.
s = s.encode('UTF-8')
print("\nEncoded String:", s)
print("Type:", type(s), "\tLength:", len(s))

# Decoding will reveal the hexadecimal code point of the non-ascii character.
s = s.decode('UTF-8')
print("\nDecoded String:", s)
print("Type:", type(s), "\tLength:", len(s))

# Reveals unicode name of each character in the string
import unicodedata
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=' : ')

s = b'Gr\xc3\xb6n'  # A string containing byte adddresses must have the 'b' prefix to denote that string as a byte literal.
print("\nGreen String:", s.decode('utf-8'))

s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print("Green String:", s)