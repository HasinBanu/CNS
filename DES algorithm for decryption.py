from Crypto.Cipher import DES

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = b'8bytekey'
ciphertext = b'\x85\xd6\x0e\xf4\x56\x1d\x0c\x3f'  
plaintext = des_decrypt(ciphertext, key)
print("Decrypted Text:", plaintext.decode('utf-8'))
