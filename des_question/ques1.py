# Input 64-bit hex data
hex_input = "0000000001101023"

# Convert to 64-bit binary string
bin_input = bin(int(hex_input, 16))[2:].zfill(64)

# Standard DES Initial Permutation table
IP = [
58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7
]

# Apply initial permutation
permuted_bin = ''.join(bin_input[i-1] for i in IP)

# Convert back to hexadecimal
hex_output = hex(int(permuted_bin, 2))[2:].zfill(16).upper()

print("After Initial Permutation:")
print("Hex:", hex_output)
