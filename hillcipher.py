def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception(f"No modular inverse for {a} mod {m}")

def matrix_inverse_2x2(matrix, mod):
    a, b = matrix[0]
    c, d = matrix[1]

    det = (a * d - b * c) % mod
    det_inv = mod_inverse(det, mod)

    # Adjugate * det_inv mod 26
    return [
        [(d * det_inv) % mod, (-b * det_inv) % mod],
        [(-c * det_inv) % mod, (a * det_inv) % mod]
    ]

def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join([chr((num % 26) + ord('A')) for num in numbers])

def pad_text(text):
    if len(text) % 2 != 0:
        text += 'X'
    return text

def encrypt_hill(plaintext, key_matrix):
    mod = 26
    plaintext = pad_text(plaintext.upper())
    nums = text_to_numbers(plaintext)
    ciphertext_nums = []

    for i in range(0, len(nums), 2):
        x = nums[i]
        y = nums[i + 1]
        c1 = (key_matrix[0][0] * x + key_matrix[0][1] * y) % mod
        c2 = (key_matrix[1][0] * x + key_matrix[1][1] * y) % mod
        ciphertext_nums.extend([c1, c2])

    return numbers_to_text(ciphertext_nums)

def decrypt_hill(ciphertext, key_matrix):
    mod = 26
    inv_key = matrix_inverse_2x2(key_matrix, mod)
    nums = text_to_numbers(ciphertext)
    plaintext_nums = []

    for i in range(0, len(nums), 2):
        x = nums[i]
        y = nums[i + 1]
        p1 = (inv_key[0][0] * x + inv_key[0][1] * y) % mod
        p2 = (inv_key[1][0] * x + inv_key[1][1] * y) % mod
        plaintext_nums.extend([p1, p2])

    return numbers_to_text(plaintext_nums)

# ==== USAGE ====
key_matrix = [[7, 8], [11, 11]]
plaintext = "HELLOWORLD"
ciphertext = encrypt_hill(plaintext, key_matrix)
decrypted = decrypt_hill(ciphertext, key_matrix)

print("Original Plaintext :", plaintext)
print("Encrypted Ciphertext:", ciphertext)
print("Decrypted Plaintext :", decrypted)
