def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # check if the character is alphabetic
            shift_amount = shift % 26  # ensure shift is within 0-25
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift_amount) % 26 + base
            result += chr(shifted)
        else:
            result += char  # if the character is not alphabetic, keep it unchanged
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (an integer): "))
        
        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, -shift, 'decrypt')
            print("Decrypted text:", decrypted_text)
        
        again = input("Do you want to try again? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
