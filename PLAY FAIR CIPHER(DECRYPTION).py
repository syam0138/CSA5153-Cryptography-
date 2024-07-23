#PLAY FAIR IMPLEMENTATION OF DECRYPTION USING PYTHON
def toLowerCase(plain):
    # Convert all the characters of a string to lowercase
    return plain.lower()

def removeSpaces(plain):
    # Remove all spaces in a string
    # can be extended to remove punctuation
    return ''.join(plain.split())

def generateKeyTable(key):
    # generates the 5x5 key square
    keyT = [['' for i in range(5)] for j in range(5)]
    dicty = {chr(i + 97): 0 for i in range(26) if chr(i + 97) != 'j'}
    
    for char in key:
        if char.lower() != 'j':
            dicty[char.lower()] = 2
    
    i, j = 0, 0
    for char in key.lower() + 'abcdefghiklmnopqrstuvwxyz':
        if char != 'j' and dicty[char] != 1:
            keyT[i][j] = char
            dicty[char] = 1
            j += 1
            if j == 5:
                i += 1
                j = 0
            if i == 5:
                break
    
    return keyT

def search(keyT, a, b):
    # Search for the characters of a digraph in the key square and return their position
    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a:
                a_pos = (i, j)
            if keyT[i][j] == b:
                b_pos = (i, j)
    return a_pos + b_pos

def mod5(a):
    # Function to find the modulus with 5
    return (a + 5) % 5

def decrypt(ciphertext, keyT):
    # Function to decrypt
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        a, b = ciphertext[i], ciphertext[i+1]
        a_row, a_col, b_row, b_col = search(keyT, a, b)
        
        if a_row == b_row:
            plaintext += keyT[a_row][mod5(a_col-1)] + keyT[b_row][mod5(b_col-1)]
        elif a_col == b_col:
            plaintext += keyT[mod5(a_row-1)][a_col] + keyT[mod5(b_row-1)][b_col]
        else:
            plaintext += keyT[a_row][b_col] + keyT[b_row][a_col]
        
        i += 2
    
    return plaintext

def decryptByPlayfairCipher(ciphertext, key):
    # Function to call decrypt
    key = removeSpaces(toLowerCase(key))
    ciphertext = removeSpaces(toLowerCase(ciphertext))
    keyT = generateKeyTable(key)
    return decrypt(ciphertext, keyT)

if __name__ == '__main__':
    ciphertext = "gatlmzclrqtx"
    key = "Monarchy"
    
    print("Key text:", key)
    print("Cipher text:", ciphertext)
    
    decrypted_text = decryptByPlayfairCipher(ciphertext, key)
    print("Decrypted text:", decrypted_text)

# Python Code Written By Kushal Prajapati
# Corrected and improved by Claude