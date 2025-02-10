
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]


PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19,
       11, 3, 60, 52, 44, 36, 63, 55,
       47, 39, 31, 23, 15, 7, 62, 54,
       46, 38, 30, 22, 14, 6, 61, 53,
       45, 37, 29, 21, 13, 5, 28, 20,
       12, 4]


PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def permute(block, table):
    return [block[i-1] for i in table]


def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]


def generate_keys(key):
    key = permute(key, PC1)
    left, right = key[:28], key[28:]
    round_keys = []
    for shift in SHIFT_SCHEDULE:
        left, right = left_shift(left, shift), left_shift(right, shift)
        round_keys.append(permute(left + right, PC2))
    return round_keys[::-1]  


def feistel(right, key):
    return [r ^ k for r, k in zip(right, key)] 

def des_decrypt(ciphertext, key):
    ciphertext = permute(ciphertext, IP)
    left, right = ciphertext[:32], ciphertext[32:]
    keys = generate_keys(key)  

    for i in range(16):
        new_right = [l ^ f for l, f in zip(left, feistel(right, keys[i]))]
        left, right = right, new_right

    return permute(right + left, FP)


ciphertext = [0, 1, 1, 0, 1, 0, 0, 1] * 8  
key = [1, 0, 1, 0, 0, 1, 1, 1] * 8  

plaintext = des_decrypt(ciphertext, key)
print("Decrypted:", plaintext)
