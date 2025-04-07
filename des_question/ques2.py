# Define S-box 3 (Table 6.5)
sbox3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 12, 2],
]

# Define S-box 4 (Table 6.6)
sbox4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
]

# Function to look up an S-box given a 6-bit input
def sbox_lookup(six_bit_input: str, sbox: list) -> tuple:
    # Row = bits 1 and 6 (first and last bits)
    row = int(six_bit_input[0] + six_bit_input[5], 2)
    # Column = bits 2 to 5 (middle 4 bits)
    col = int(six_bit_input[1:5], 2)
    
    # Lookup the value
    value = sbox[row][col]
    # Convert to 4-bit binary string
    bin_value = format(value, '04b')
    
    return bin_value, value

# Main logic
if __name__ == "__main__":
    # Part a: S-box 3 with input 110111
    input_a = "110111"
    result_a_bin, result_a_dec = sbox_lookup(input_a, sbox3)
    print(f"a. Input: {input_a} → Binary: {result_a_bin}, Decimal: {result_a_dec}")

    # Part b: S-box 4 with input 001100
    input_b = "001100"
    result_b_bin, result_b_dec = sbox_lookup(input_b, sbox4)
    print(f"b. Input: {input_b} → Binary: {result_b_bin}, Decimal: {result_b_dec}")
