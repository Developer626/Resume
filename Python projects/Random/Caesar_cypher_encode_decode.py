# Coded by Aaron Waruszewski
# Date 4/10/19
# 
# Description:
# This script takes plain text from a file and shifts the letters in it by the amount
# issued by the user to create a caesar cypher text.
# 
# Use:
# terminal> python3 caesar_cypher_encode_decode.py some_text_file.txt <number>
# 
# Where <number> is the amount to shift the characters by.

import sys

def caesar_cypher_encode_decode(file_to_open, shift):

    # Make sure the shift doesn't go beyond the size of the alphabet.
    if shift > 26:
        shift = shift % 26
    elif shift < -26:
        shift = shift % -26

    # Get the text to convert.
    with open(file_to_open) as f:
        words = f.read()
    
    for i in range(0, len(words)):
        
        # Convert a character into an integer
        num = ord(words[i])

        # Check to see if the character is part of the alphabet, and capital.
        if (num >= 65 and num <= 90):

            # If the character goes out of bounds correct it and covert it, 
            # otherwise just convert it.
            if num + shift < 65:
                num = num + shift + 26
            elif num + shift > 90:
                num = num + shift - 26
            else:
                num += shift
        
        # Check to see if the character is part of the alphabet, and lower case.
        elif (num >= 97 and num <= 122):

            # If the character goes out of bounds correct it and covert it, 
            # otherwise just convert it.
            if num + shift < 97:
                num = num + shift + 26
            elif num + shift > 122:
                num = num + shift - 26
            else:
                num += shift

        # Create a new string, slice out the old character, and add in the converted one.
        words = words[0:i] + chr(num) + words[i+1:len(words)]
    
    print(words)

caesar_cypher_encode_decode(sys.argv[1], int(sys.argv[2]))