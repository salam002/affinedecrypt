from math import gcd
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def mod_inverse(a, m):
    for x in range(1,m):
        if (a*x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    m = 26  # Size of the alphabet
    a_inv = mod_inverse(a, m)

    if a_inv is None:
        return None  

    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('a')  # Convert character to 0-25
            x = (a_inv * (y - b)) % m  # Apply decryption formula
            decrypted_char = chr(x + ord('a'))  # Convert back to character
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  

    return decrypted_text 

# Example ciphertext
dString = "znk gtyckx zu znk waof wakyzout oy iuskz"

results = []
for a in range(1, 26):
    # if gcd(a, 26) == 1:  # a must be coprime to 26
    for b in range(26):
        decrypted = affine_decrypt(dString, a, b)
        results.append((a, b, decrypted))

# Print the results
for a, b, text in results:
    print(f"a={a}, b={b}: {text}")