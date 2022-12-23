def encrypt(text, s):
    result = ""
    
    # Caesar cypher first reverses the plain text
    # Then it takes each letter and encrypts by offsetting the ASCII value of each letter
    
    # reverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


# check the above function
text = "CAESAR CIPHER DEMO"
s = 5

print(f"Plain Text :     {text}")
print(f"Shift pattern :  {str(s)}")
print(f"Cipher:  {encrypt(text,s)}")
