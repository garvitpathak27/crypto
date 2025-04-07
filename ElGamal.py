import random

class ElGamal:
    def __init__(self, q, a, x, k, msg):
        """
        Initializes ElGamal encryption parameters.

        Parameters:
        - q : A large prime number
        - a : A primitive root modulo q
        - x : Private key (random number < q)
        - k : Random integer used for encryption (session key)
        - msg : Message to encrypt (numeric form)

        This function computes the public key: y = a^x mod q
        """
        self.q = q
        self.a = a
        self.x = x      # Private key (kept secret)
        self.k = k      # Random session key (different each encryption)
        self.msg = msg  # Message to encrypt (as a number)
        self.y = pow(self.a, self.x, self.q)  # Public key: y = a^x mod q

    def encrypt(self):
        """
        Encrypts the message using ElGamal encryption.

        Returns:
        - C1 : a^k mod q
        - C2 : (msg * y^k) mod q

        C1 and C2 together form the ciphertext.
        """
        K = pow(self.y, self.k, self.q)         # Shared secret key: K = y^k mod q
        C1 = pow(self.a, self.k, self.q)        # First part of ciphertext: C1 = a^k mod q
        C2 = (self.msg * K) % self.q            # Second part: C2 = (msg * K) mod q
        return (C1, C2)

    def decrypt(self, C1, C2):
        """
        Decrypts the ciphertext using the private key.

        Parameters:
        - C1 : First part of ciphertext
        - C2 : Second part of ciphertext

        Returns:
        - M : Original decrypted message
        """
        K = pow(C1, self.x, self.q)             # Recover shared secret: K = C1^x mod q
        K_inv = pow(K, -1, self.q)              # Compute modular inverse: K^(-1) mod q
        M = (C2 * K_inv) % self.q               # Decrypt: M = (C2 * K^(-1)) mod q
        return M

    def display_keys(self):
        """Displays all keys used in the ElGamal encryption."""
        print(f"Prime (q): {self.q}")
        print(f"Primitive root (a): {self.a}")
        print(f"Private Key (x): {self.x}")
        print(f"Public Key (y = a^x mod q): {self.y}")


def main():
    # Define parameters for ElGamal system
    q = 751        # A large prime number
    a = 6          # Primitive root modulo q
    x = 85         # Private key (chosen randomly)
    k = 113        # Random session key used for encryption
    msg = 443      # Message to encrypt (converted to a number)

    # Initialize ElGamal system with given parameters
    elgamal = ElGamal(q, a, x, k, msg)

    # Display public and private key values
    elgamal.display_keys()

    # Encrypt the message
    print("\nEncrypting Message:", msg)
    C1, C2 = elgamal.encrypt()
    print(f"Ciphertext: C1 = {C1}, C2 = {C2}")

    # Decrypt the message to verify correctness
    decrypted_msg = elgamal.decrypt(C1, C2)
    print("\nDecrypted Message:", decrypted_msg)


# Start the program
if __name__ == "__main__":
    main()
