import string

class PlayfairCipher:
    def __init__(self, key):
        # Initialize the PlayfairCipher object with a key
        self.key = self.prepare_key(key)  # Prepare the key (cleaning and removing duplicates)
        self.matrix = self.generate_matrix(self.key)  # Generate the Playfair matrix using the key

    def prepare_key(self, key):
        """
        Prepares the key by:
        1. Converting it to lowercase
        2. Replacing 'j' with 'i' (as 'j' and 'i' are treated the same in the Playfair cipher)
        3. Removing duplicate characters
        """
        key = key.lower().replace('j', 'i')  # Normalize the key by treating 'j' as 'i'
        seen = set()  # To keep track of characters we've already added
        new_key = ''  # This will store the cleaned key
        
        # Iterate over each character in the key
        for char in key:
            # Add the character to the key if it's a letter and hasn't been seen before
            if char in string.ascii_lowercase and char not in seen:
                seen.add(char)
                new_key += char
        return new_key  # Return the processed key without duplicates

    def generate_matrix(self, key):
        """
        Generates the 5x5 Playfair matrix using the provided key:
        1. The key is used to fill the matrix (removes duplicates).
        2. The rest of the alphabet is added (except 'j', since it was merged with 'i').
        """
        alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Define the alphabet (note: no 'j')
        
        # Add characters from the alphabet that are not in the key
        for char in alphabet:
            if char not in key:
                key += char

        # Create a 5x5 matrix by slicing the key into rows of 5 characters
        matrix = [list(key[i*5:(i+1)*5]) for i in range(5)]
        return matrix  # Return the generated Playfair matrix

    def find_position(self, char):
        """
        Finds the position of a character in the Playfair matrix.
        The matrix is a 5x5 grid, so this will return the (row, column) of the character.
        """
        for i in range(5):  # Loop through the rows
            for j in range(5):  # Loop through the columns
                if self.matrix[i][j] == char:  # If the character is found in the matrix
                    return i, j  # Return its row and column indices
        return None  # In case the character is not found (should not happen)

    def decrypt_pair(self, a, b):
        """
        Decrypts a pair of characters using the Playfair cipher rules:
        1. If the characters are in the same row, replace them with the characters to their immediate left.
        2. If the characters are in the same column, replace them with the characters above them.
        3. If the characters are in different rows and columns, form a rectangle and swap the columns.
        """
        row1, col1 = self.find_position(a)  # Find the position of the first character
        row2, col2 = self.find_position(b)  # Find the position of the second character

        if row1 == row2:
            # If the characters are in the same row, shift them left (circularly)
            return self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # If the characters are in the same column, shift them up (circularly)
            return self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
        else:
            # If the characters are in different rows and columns, swap the columns
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def decrypt(self, ciphertext):
        """
        Decrypts the entire ciphertext using the Playfair cipher.
        Assumes the ciphertext is in lowercase and that 'j' has already been replaced with 'i'.
        """
        ciphertext = ciphertext.lower().replace('j', 'i')  # Prepare the ciphertext by replacing 'j' with 'i'
        plaintext = ''  # This will store the decrypted message
        i = 0  # Index for iterating through the ciphertext
        
        # Process each pair of characters in the ciphertext
        while i < len(ciphertext):
            a = ciphertext[i]  # First character in the pair
            b = ciphertext[i + 1]  # Second character in the pair
            plaintext += self.decrypt_pair(a, b)  # Decrypt the pair and add to the plaintext
            i += 2  # Move to the next pair
        
        return plaintext  # Return the full decrypted plaintext


# --- Usage Example ---
if __name__ == "__main__":
    key = "monarchy"  # Define the secret key to be used in the cipher
    ciphertext = "gatlmzclrqtx"  # Define the ciphertext to be decrypted

    cipher = PlayfairCipher(key)  # Initialize the Playfair cipher with the provided key
    decrypted = cipher.decrypt(ciphertext)  # Decrypt the ciphertext

    print("Decrypted Message:", decrypted)  # Print the decrypted message
