w0 = [0x51, 0xFC, 0x03]
w1 = [0x21, 0x97, 0x45]
w2 = [0x59, 0x06, 0x22]
w3 = [0x96, 0x05, 0x06]

# Step 1: RotWord and SubWord already done
sub_word = [0x33, 0x38, 0x56]
sub_word[0] ^= 0x1B  # Apply Rcon
sub_word[0] = 0x28

# W4 = W0 ^ SubWord
w4 = [w0[i] ^ sub_word[i] for i in range(3)]

# W5 = W4 ^ W1
w5 = [w4[i] ^ w1[i] for i in range(3)]

# W6 = W5 ^ W2
w6 = [w5[i] ^ w2[i] for i in range(3)]

# W7 = W6 ^ W3
w7 = [w6[i] ^ w3[i] for i in range(3)]

# Combine all
round9_key = w4 + w5 + w6 + w7

# Print formatted
print("9th Round Key:")
print(' '.join(f"{b:02X}" for b in round9_key))
