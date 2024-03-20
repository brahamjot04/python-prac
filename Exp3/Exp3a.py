# Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher. The script should work for any printable characters.

plaintext = input("Enter a line of plaintext: ")
distance = int(input("Enter the distance value: "))

encrypted_text = ""
for char in plaintext:
    if char.isprintable():
        encrypted_char = chr((ord(char) + distance) % 256)
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print("Encrypted text:", encrypted_text)
