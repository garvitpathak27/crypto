# 9th round key as 4 words (each word = 4 bytes = 1 column in the matrix)
w = [
    [0xBF, 0xE2, 0xBF, 0x90],  # W0
    [0x45, 0x59, 0xFA, 0xB2],  # W1
    [0xA1, 0x64, 0x80, 0xB4],  # W2
    [0xF7, 0xF1, 0xCB, 0xD8]   # W3
]

# Round constant Rcon[10] = 0x36
rcon_10 = 0x36

# S-box values manually extracted from the table for RotWord(W3)
rot_word = [0xF1, 0xCB, 0xD8, 0xF7]  # RotWord of W3

# Use S-box to get SubWord (manually from image):
# F1 -> 73, CB -> BB, D8 -> 5D, F7 -> 7F
sub_word = [0x73, 0xBB, 0x5D, 0x7F]

# XOR Rcon with first byte of sub_word
sub_word[0] ^= rcon_10  # 0x73 ^ 0x36 = 0x45

# Step 1: W4 = W0 ^ sub_word
w4 = [w[0][i] ^ sub_word[i] for i in range(4)]

# Step 2: W5 = W4 ^ W1
w5 = [w4[i] ^ w[1][i] for i in range(4)]

# Step 3: W6 = W5 ^ W2
w6 = [w5[i] ^ w[2][i] for i in range(4)]

# Step 4: W7 = W6 ^ W3
w7 = [w6[i] ^ w[3][i] for i in range(4)]

# Collect the 10th round key
round10_key = w4 + w5 + w6 + w7

# Format the key into hex string
formatted_key = ' '.join(f'{byte:02X}' for byte in round10_key)
print("10th Round Key:")
print(formatted_key)
