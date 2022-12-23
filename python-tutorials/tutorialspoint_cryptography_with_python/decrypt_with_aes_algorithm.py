# Import the necessary libraries
from Crypto.Cipher import AES
import base64

# Set the encryption key and algorithm
key = b'1234567890abcdef'
algorithm = AES.MODE_CBC

# Read the encrypted password from a file
with open('encrypted_password.txt', 'rb') as f:
    encrypted_password = f.read()

# Decrypt the password using the encryption key and algorithm
decryptor = AES.new(key, algorithm)
decrypted_password = decryptor.decrypt(base64.b64decode(encrypted_password))

# Print the decrypted password
print(decrypted_password)
