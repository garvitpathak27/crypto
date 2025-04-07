def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(64)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].zfill(16).upper()

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def apply_final_permutation(hex_data):
    final_permutation = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    
    binary_data = hex_to_bin(hex_data)
    permuted_data = permute(binary_data, final_permutation)
    return bin_to_hex(permuted_data)

# Example
input_hex = "10660099"
result = apply_final_permutation(input_hex)
print(f"Final Permutation Output (Hex): {result}")
