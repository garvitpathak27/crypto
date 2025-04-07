# Convert hex key to 64-bit binary
def hex_to_bin(hex_key):
    bin_key = bin(int(hex_key, 16))[2:].zfill(64)
    return bin_key

# Apply permutation using a given table
def permute(input_bits, table):
    return ''.join(input_bits[i - 1] for i in table)

# Perform left circular shift
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Main function
def generate_round_keys(hex_key):
    # Parity Drop Table (PC-1)
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

    # Compression Box Table (PC-2)
    pc2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    # Step 1: Convert hex key to binary
    bin_key = hex_to_bin(hex_key)

    # Step 2: Apply PC-1 to get 56-bit key
    key_56 = permute(bin_key, pc1)

    # Split into C and D halves
    C = key_56[:28]
    D = key_56[28:]

    # List to store round keys
    round_keys = []

    # Number of shifts per round
    shifts = [1, 1]  # Only first two rounds needed

    for i in range(2):
        # Step 3: Left shift C and D
        C = left_shift(C, shifts[i])
        D = left_shift(D, shifts[i])

        # Step 4: Combine C and D, apply PC-2
        combined = C + D
        round_key = permute(combined, pc2)

        round_keys.append((i + 1, round_key, hex(int(round_key, 2))[2:].zfill(12).upper()))

    return round_keys

# Driver code
if __name__ == "__main__":
    key_hex = "AABB09182736CCDD"
    round_keys = generate_round_keys(key_hex)

    for i, bin_key, hex_key in round_keys:
        print(f"Round {i} Key:\nBinary: {bin_key}\nHex: {hex_key}\n")
