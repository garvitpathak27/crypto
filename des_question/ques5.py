# Define S-box 7
SBOX_7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

# Define S-box 2
SBOX_2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

def sbox_lookup(input_bits: str, sbox: list) -> tuple:
    row = int(input_bits[0] + input_bits[5], 2)
    col = int(input_bits[1:5], 2)
    value = sbox[row][col]
    return value, format(value, '04b')

# a. 000000 through S-box 7
bits_a = '000000'
decimal_a, binary_a = sbox_lookup(bits_a, SBOX_7)

# b. 111111 through S-box 2
bits_b = '111111'
decimal_b, binary_b = sbox_lookup(bits_b, SBOX_2)

# Output
print(f"(a) S-box 7 input '000000': Decimal = {decimal_a}, Binary = {binary_a}")
print(f"(b) S-box 2 input '111111': Decimal = {decimal_b}, Binary = {binary_b}")
