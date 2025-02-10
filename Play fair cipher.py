import re

def prepare_text(text):
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace("J", "I")  
    prepared = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared += text[i] + "X"
            i += 1
        elif text[i] == text[i + 1]:
            prepared += text[i] + "X"
            i += 1
        else:
            prepared += text[i] + text[i + 1]
            i += 2
    return prepared

def create_playfair_matrix(keyword):
    keyword = re.sub(r'[^A-Za-z]', '', keyword).upper().replace("J", "I")
    matrix = []
    seen = set()
    
    for char in keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, letter):
    for row in range(5):
        if letter in matrix[row]:
            return row, matrix[row].index(letter)
    return None

def encrypt_digraph(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])
    
    if row1 == row2:  
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_playfair(plaintext, keyword):
    matrix = create_playfair_matrix(keyword)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_digraph(matrix, plaintext[i:i+2])
    
    return ciphertext


keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")


ciphertext = encrypt_playfair(plaintext, keyword)
print("Encrypted Text:", ciphertext)
