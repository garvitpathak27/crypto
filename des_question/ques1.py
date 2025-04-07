# Input 64-bit hex data
hex_input = "0000000001101023"

# Convert to 64-bit binary string
bin_input = bin(int(hex_input, 16))[2:].zfill(64)
print(bin_input)

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

# Step 1: Apply the permutation to the input binary string.
bin_input = '110101001011'  # Example binary input
IP = [2, 1, 4, 3, 6, 5]  # Example permutation positions

# Initialize an empty string for the permuted binary output
permuted_bin = ""

# Iterate over each index in IP to reorder the bits
for i in IP:
    # Since the positions in IP are 1-based (e.g., 1, 2, 3...), we subtract 1 to make them 0-based
    permuted_bin += bin_input[i-1]

# Step 2: Convert permuted binary to hexadecimal
# Convert permuted binary to an integer
decimal_value = int(permuted_bin, 2)
print("Decimal Value:", decimal_value)

# Convert the decimal integer to hexadecimal
hex_value = hex(decimal_value)
print("Hex Value (with '0x' prefix):", hex_value)

# Remove the '0x' prefix and pad the hexadecimal value to 16 characters
hex_output = hex_value[2:].zfill(16).upper()

print("Hex Output (Final):", hex_output)


print("After Initial Permutation:")
print("Hex:", hex_output)
