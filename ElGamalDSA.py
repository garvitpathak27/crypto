import random

class ElGamalDSA:
    def __init__(self, p, g, x):
        """
        Initialize ElGamal Digital Signature parameters.
        p : Large prime number
        g : Primitive root modulo p
        x : Private key (1 < x < p-1)
        """
        self.p = p
        self.g = g
        self.x = x                          # Private key
        self.y = pow(g, x, p)               # Public key: y = g^x mod p

    def modinv(self, a, m):
        """Compute modular inverse using Extended Euclidean Algorithm."""
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            a, m = m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 % m0

    def sign(self, msg, k):
        """
        Sign the message.
        msg : Integer hash of message (or message itself for simplicity)
        k   : Random integer such that gcd(k, p-1) = 1
        Returns: (r, s) as signature
        """
        if self.gcd(k, self.p - 1) != 1:
            raise ValueError("k must be coprime with p-1")

        r = pow(self.g, k, self.p)                         # r = g^k mod p
        k_inv = self.modinv(k, self.p - 1)                 # k^(-1) mod (p-1)
        s = (k_inv * (msg - self.x * r)) % (self.p - 1)    # s = k^(-1) * (msg - x*r) mod (p-1)
        return (r, s)

    def verify(self, msg, r, s):
        """
        Verify the signature.
        msg : Integer hash of message (or message itself)
        r, s: Signature pair
        Returns: True if valid, False otherwise
        """
        if not (0 < r < self.p):
            return False

        lhs = pow(self.g, msg, self.p)                    # g^msg mod p
        rhs = (pow(self.y, r, self.p) * pow(r, s, self.p)) % self.p  # y^r * r^s mod p
        return lhs == rhs

    def gcd(self, a, b):
        """Compute GCD of two numbers."""
        while b:
            a, b = b, a % b
        return a

    def display_keys(self):
        print(f"Prime (p): {self.p}")
        print(f"Primitive root (g): {self.g}")
        print(f"Private Key (x): {self.x}")
        print(f"Public Key (y = g^x mod p): {self.y}")


# --- Usage Example ---
def main():
    p = 467       # Prime number
    g = 2         # Primitive root modulo p
    x = 127       # Private key
    k = 79        # Random k such that gcd(k, p-1) = 1
    msg = 123     # Message to be signed (can also use hash of a message)

    elg_dsa = ElGamalDSA(p, g, x)
    elg_dsa.display_keys()

    print("\nSigning Message:", msg)
    r, s = elg_dsa.sign(msg, k)
    print(f"Signature: r = {r}, s = {s}")

    is_valid = elg_dsa.verify(msg, r, s)
    print("\nSignature Verified:", is_valid)


if __name__ == "__main__":
    main()
