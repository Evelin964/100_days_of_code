# This is a Caesar Cipher Game for Day 8 project


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_code = ord(char)
            is_upper = char.isupper()

            shifted_code = (ascii_code - ord("A" if is_upper else "a") + shift) % 26
            encrypted_char = chr(shifted_code + ord("A" if is_upper else "a"))

            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_code = ord(char)
            is_upper = char.isupper()

            shifted_code = (ascii_code - ord("A" if is_upper else "a") - shift) % 26
            decrypted_char = chr(shifted_code + ord("A" if is_upper else "a"))

            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    print("Caesar Cipher Encryption and Decryption")

    while True:
        choice = input("Do you want to encrypt or decrypt (Encript/Decript)? ").lower()
        if choice not in ["encript", "decript"]:
            print("Invalid choice. Please enter 'Encript' or 'Decript'.")
            continue

        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choice == "encript":
            encrypted_message = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)

        another = input("Do you want to perform another operation (yes/no)? ").lower()
        if another != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
