class ecc:
    def __init__(self , a , b , p , gx , gy , d , k):
        self.a = a
        self.b = b
        self.p = p
        self.g = (gx , gy)  # Use this instead of self.gy
        self.d = d
        self.k = k
        self.Q = self.mult(self.d ,self.g)
    
    def pointadd(self , P , Q):
        if P == (None , None) : return Q
        if Q == (None , None) : return P
        
        x1 , y1 = P
        x2 , y2 = Q
        
        if x1 == x2 and y1 == -y2 % self.p:
            return (None , None)
        
        if P == Q:
            m = (3 * x1 ** 2 + self.a) * pow(2 * y1 , -1 , self.p)
        else:
            m = (y2 - y1) * pow(x2 - x1 , -1 , self.p)
        m %= self.p
        x3 = (m**2 - x1 - x2 ) % self.p
        y3 = (m * (x1 - x2) - y1) % self.p
        return (x3 , y3)
    
    def mult(self , d , P):
        res = (None , None)
        addend = P
        while d:
            if d & 1:
                res = self.pointadd(res, addend)
            addend = self.pointadd(addend , addend)
            d >>= 1
        return res
    
    def encrypt(self , PM):
        C1 = self.mult(self.k , self.g)
        kQ = self.mult(self.k , self.Q)
        C2 = self.pointadd(PM , kQ)
        return (C1 , C2)
    
    def decrypt(self , C1 , C2):
        dC1 = self.mult(self.d , C1)
        neg_dC1 = (dC1[0], -dC1[1] % self.p)  # Negating the y-coordinate
        PM = self.pointadd(C2 , neg_dC1)
        return PM
    
    def display(self):  # Changed this to match method name in main
        print(f"Elliptic Curve: y² = x³ + {self.a}x + {self.b} (mod {self.p})")
        print(f"Base Point G: {self.g}")
        print(f"Private Key: {self.d}")
        print(f"Public Key Q: {self.Q}")
        
def main():
    # Define elliptic curve parameters
    p = 751
    a = -1
    b = 188
    Gx, Gy = 0, 376  # Base point
    d = 85           # Private key
    k = 113          # Ephemeral key for this encryption

    ecc_curve = ecc(a, b, p, Gx, Gy, d, k)
    ecc_curve.display()  # Corrected method name here

    PM = (443, 253)  # Message point on the curve
    print("\nEncrypting Message Point:", PM)

    # Encrypt the message
    C1, C2 = ecc_curve.encrypt(PM)
    print(f"Ciphertext: C1 = {C1}, C2 = {C2}")

    # Decrypt the ciphertext
    decrypted_PM = ecc_curve.decrypt(C1, C2)
    print("\nDecrypted Message Point:", decrypted_PM)

main()
