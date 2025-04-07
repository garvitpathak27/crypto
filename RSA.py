class RSA:
    def __init__(self, p, q):
        """
        Initialize the RSA system with two prime numbers p and q.
        Generates public and private keys.
        """

        self.p = p
        self.q = q
        self.n = p * q                           # Modulus for both public and private keys
        self.phi = (p - 1) * (q - 1)             # Euler's totient function

        self.e = self.find_e(self.phi)           # Public exponent e
        self.d = self.modinv(self.e, self.phi)   # Private exponent d

        self.public_key = (self.e, self.n)       # Public key (e, n)
        self.private_key = (self.d, self.n)      # Private key (d, n)


    def gcd(self, a, b):
        """Calculate the Greatest Common Divisor using Euclidean Algorithm."""
        while b:
            a, b = b, a % b
        return a

    def find_e(self, phi):
        """
        Find an integer e such that:
        1 < e < phi and gcd(e, phi) = 1 (i.e., e and phi are coprime).
        """
        e = 2
        while e < phi:
            if self.gcd(e, phi) == 1:
                return e
            e += 1

    def modinv(self, a, m):
        """
        Compute modular inverse of a under modulo m
        using Extended Euclidean Algorithm.
        """
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 % m0

    def encrypt(self, message):
        """
        Encrypt the message using the public key.
        Each character is encrypted separately as: c = (m^e) % n
        """
        e, n = self.public_key
        return [pow(ord(char), e, n) for char in message]

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using the private key.
        Each integer is decrypted back to character as: m = (c^d) % n
        """
        d, n = self.private_key
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])

    def display_keys(self):
        """Display the public and private keys."""
        print("Public Key (e, n):", self.public_key)
        print("Private Key (d, n):", self.private_key)


# --- Usage ---
if __name__ == "__main__":
    # Create an RSA object with small primes (for demo)
    rsa = RSA(p=61, q=53)

    rsa.display_keys()  # Display generated keys

    msg = "HELLO"
    print("\nOriginal Message:", msg)

    encrypted = rsa.encrypt(msg)  # Encrypt the message
    print("Encrypted Message:", encrypted)

    decrypted = rsa.decrypt(encrypted)  # Decrypt the ciphertext
    print("Decrypted Message:", decrypted)
