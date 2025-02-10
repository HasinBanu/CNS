import string

def generate_cipher_alphabet(keyword):
    # Remove duplicate letters while maintaining order
    keyword = "".join(dict.fromkeys(keyword.upper()))

    # Create the rest of the alphabet without letters in the keyword
    remaining_letters = "".join(sorted(set(string.ascii_uppercase) - set(keyword)))

    # Combine keyword and remaining letters to form the cipher alphabet
    cipher_alphabet = keyword + remaining_letters
    return cipher_alphabet

def encrypt(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    alphabet = string.ascii_uppercase
    cipher_text = ""

    for char in plaintext:
        if char in alphabet:
            cipher_text += cipher_alphabet[alphabet.index(char)]
        else:
            cipher_text += char  

    return cipher_text

def decrypt(ciphertext, cipher_alphabet):
    alphabet = string.ascii_uppercase
    plain_text = ""

    for char in ciphertext:
        if char in cipher_alphabet:
            plain_text += alphabet[cipher_alphabet.index(char)]
        else:
            plain_text += char  

    return plain_text


keyword = "CIPHER"


cipher_alphabet = generate_cipher_alphabet(keyword)
print("Cipher Alphabet:", cipher_alphabet)


plaintext = "HELLO WORLD"
ciphertext = encrypt(plaintext, cipher_alphabet)
decrypted_text = decrypt(ciphertext, cipher_alphabet)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text)
