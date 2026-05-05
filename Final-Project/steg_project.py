from PIL import Image
from cryptography.fernet import Fernet
import base64
import hashlib
import os

END_MARKER = "###END###"


def make_key(password):
    password_bytes = password.encode()
    hash_bytes = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(hash_bytes)


def message_to_bits(message):
    bits = ""
    for character in message:
        bits += format(ord(character), "08b")
    return bits


def bits_to_message(bits):
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        message += chr(int(byte, 2))
    return message


def hide_message():
    image_file = input("Enter the absolute path of the PNG: ")
    output_name = input("Enter a name for the encrypted PNG (include .png): ")
    message = input("Enter the message you want to encrypt: ")
    password = input("Enter a password for encryption: ")

    folder = os.path.dirname(image_file)
    output_file = os.path.join(folder, output_name)

    key = make_key(password)
    fernet = Fernet(key)

    encrypted_message = fernet.encrypt(message.encode()).decode()
    encrypted_message += END_MARKER

    bits = message_to_bits(encrypted_message)

    image = Image.open(image_file).convert("RGB")

    pixels = []
    px = image.load()

    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixels.append(px[x, y])
    
    if len(bits) > len(pixels) * 3:
        print("The message is too large for this image.")
        return

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel

        if bit_index < len(bits):
            r = (r & 254) | int(bits[bit_index])
            bit_index += 1

        if bit_index < len(bits):
            g = (g & 254) | int(bits[bit_index])
            bit_index += 1

        if bit_index < len(bits):
            b = (b & 254) | int(bits[bit_index])
            bit_index += 1

        new_pixels.append((r, g, b))

    image.putdata(new_pixels)
    image.save(output_file)

    print("Message saved to:", output_file)


def reveal_message():
    image_file = input("Enter the absolute path of the encrypted PNG: ")
    password = input("Enter the encryption password: ")

    image = Image.open(image_file).convert("RGB")

    pixels = []
    px = image.load()

    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixels.append(px[x, y]) 
        bits = ""

    for pixel in pixels:
        r, g, b = pixel
        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)

    hidden_text = ""

    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        character = chr(int(byte, 2))
        hidden_text += character

        if END_MARKER in hidden_text:
            hidden_text = hidden_text.replace(END_MARKER, "")
            break

    key = make_key(password)
    fernet = Fernet(key)

    try:
        decrypted_message = fernet.decrypt(hidden_text.encode()).decode()
        print("\nHidden message:")
        print(decrypted_message)
    except:
        print("Wrong password or no hidden message found.")


def main():
    print("Welcome to Landon's Steganography Tool")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        hide_message()
    elif choice == "2":
        reveal_message()
    else:
        print("Invalid choice.")


main()
