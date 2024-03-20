# Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a Caesar cipher. The script should work for any printable characters.

def caesar_cipher(text, distance):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr(
                (ord(char) - ascii_offset - distance) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

plaintext = caesar_cipher(encrypted_text, distance)
print("Plaintext:", plaintext)
