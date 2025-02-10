import numpy as np

# Convert letter to number (A=0, B=1, ..., Z=25) and vice versa
def letter_to_number(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def number_to_letter(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Hill Cipher encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext_numbers = letter_to_number(plaintext)

    # If length of plaintext is odd, append 'X' (dummy character)
    if len(plaintext_numbers) % 2 != 0:
        plaintext_numbers.append(letter_to_number("X")[0])

    # Convert into 2xN matrix form
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, 2).T

    # Multiply with key matrix mod 26
    ciphertext_matrix = np.dot(key_matrix, plaintext_matrix) % 26

    # Flatten and convert to text
    ciphertext = number_to_letter(ciphertext_matrix.T.flatten())

    return ciphertext

# Compute modular inverse of 2x2 key matrix mod 26
def mod_inverse_matrix(matrix, mod=26):
    determinant = int(round(np.linalg.det(matrix)))  # Determinant
    determinant_inv = pow(determinant, -1, mod)  # Modular inverse of determinant
    adjugate_matrix = np.array([[matrix[1, 1], -matrix[0, 1]],
                                [-matrix[1, 0], matrix[0, 0]]])  # Adjugate
    inverse_matrix = (determinant_inv * adjugate_matrix) % mod  # Modular inverse
    return inverse_matrix.astype(int)

# Hill Cipher decryption
def hill_decrypt(ciphertext, key_matrix):
    ciphertext_numbers = letter_to_number(ciphertext)

    # Convert into 2xN matrix form
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, 2).T

    # Compute modular inverse of key matrix
    inverse_key_matrix = mod_inverse_matrix(key_matrix)

    # Multiply with inverse key matrix mod 26
    decrypted_matrix = np.dot(inverse_key_matrix, ciphertext_matrix) % 26

    # Flatten and convert to text
    decrypted_text = number_to_letter(decrypted_matrix.T.flatten())

    return decrypted_text

# Define 2x2 key matrix
key_matrix = np.array([[9, 4], [5, 7]])

# Given plaintext
plaintext = "MEETMEATTHEUSUALPLACEATTENRATHERTHANEIGHTOCLOCK"

# Encrypt and Decrypt
ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(ciphertext, key_matrix)

# Display results
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
