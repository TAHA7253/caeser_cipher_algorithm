def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    :param text: The input text to be encrypted or decrypted.
    :param shift: The number of positions each character in the text will be shifted.
    :param mode: Mode of operation - 'encrypt' or 'decrypt'. Default is 'encrypt'.
    :return: The encrypted or decrypted text.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char

    return result


def main():
    print("Welcome to the Caesar Cipher Program!")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {result}")


if __name__ == "__main__":
    main()
