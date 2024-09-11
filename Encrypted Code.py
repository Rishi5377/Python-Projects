import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT CODE
plain_text = input("Enter message to encrypt : ")
cipher_text = ""
for _ in plain_text :
    idx = chars.index(_)
    cipher_text += key[idx]

print(f"The Encrypted message : {cipher_text}")

# DECRYPT CODE
cipher_text= input("Enter message to be Decrypted : ")
plain_text = ""
for _ in cipher_text :
    idx = key.index(_)
    plain_text += chars[idx]

print(f"The Decrypted message : {plain_text}")
