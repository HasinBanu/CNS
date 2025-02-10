import string

def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")  
    keyword = "".join(dict.fromkeys(keyword))

    alphabet = string.ascii_uppercase.replace("J", "")  
    remaining_letters = "".join([c for c in alphabet if c not in keyword])

    matrix = keyword + remaining_letters
    playfair_matrix = [list(matrix[i:i+5]) for i in range(0, 25, 5)]

    return playfair_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

keyword = "CIPHER"
playfair_matrix = generate_playfair_matrix(keyword)

print("Playfair Cipher Matrix:")
print_matrix(playfair_matrix)
