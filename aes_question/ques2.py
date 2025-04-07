# Given 2nd round key as 4 words (columns)
w = [
    [0x56, 0x08, 0x20, 0x07],  # W0
    [0xC7, 0x1A, 0xB1, 0x8F],  # W1
    [0x76, 0x43, 0x55, 0x69],  # W2
    [0xA0, 0x3A, 0xF7, 0xFA]   # W3
]

# Round constant Rcon[3] = 0x04
rcon_3 = 0x04

# Step 1: RotWord(W3) → [0x3A, 0xF7, 0xFA, 0xA0]
rot_word = [0x3A, 0xF7, 0xFA, 0xA0]

# Step 2: SubWord using S-box (looked manually from table):
# 3A -> 8C, F7 -> 7F, FA -> 38, A0 -> 32
sub_word = [0x8C, 0x7F, 0x38, 0x32]

# Step 3: Apply Rcon to first byte
sub_word[0] ^= rcon_3  # 0x8C ^ 0x04 = 0x88

# Step 4: W4 = W0 ^ sub_word
w4 = [w[0][i] ^ sub_word[i] for i in range(4)]

# Step 5: W5 = W4 ^ W1
w5 = [w4[i] ^ w[1][i] for i in range(4)]

# Step 6: W6 = W5 ^ W2
w6 = [w5[i] ^ w[2][i] for i in range(4)]

# Step 7: W7 = W6 ^ W3
w7 = [w6[i] ^ w[3][i] for i in range(4)]

# Final 3rd round key
round3_key = w4 + w5 + w6 + w7

# Format for display
formatted_key = ' '.join(f'{byte:02X}' for byte in round3_key)
print("3rd Round Key:")
print(formatted_key)
