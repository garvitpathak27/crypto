class RSA:
    def __init__(self , p , q  ):
        self.p = p 
        self.q = q
        self.n = p*q
        self.phi = (p-1)(q-1)
        
        self.e =  self.fine_e(self.phi)
        self.d = self.modinv(self.e , self.phi)
        
        self.public_key = (self.e , self.n)
        self.private_key = (self.d , self.n)
        
    def gcd(self , a , b):
        while b : 
            a , b = b , a % b 
        return a
    
    def find_e(self,phi):
        e = 2
        while e < phi:
            if self.gcd(e,phi) == 1:
                return e
            e+=1
        
    def modinv(self , a , m):
        m0 , x0 , x1 = m, 0 ,1
        while a> 1:
            q = a//m
            a , m = m , a %m
            x0 , x1  = x1 -q * x0 , x0 
        return x1 % m0
    
    def encrypt(self , message):
        e , n = self.public_key
        return [pow(ord(char),e,n) for char in message]
    
    def decrypt (self , ciphertext):
        d , n = self.private_key
        return ''.join([chr(pow(char,d,n))for char in ciphertext])   
    
    def displaykey(self):
        print("public key  e, n : ", self.public_key)     
        print("private key : " , self.private_key)

if __name__ == "__main__":
    rsa =RSA (p = 61 , q = 53)
    rsa.displaykey()
    
    msg = "HELLO"
    
    print("\noriginal message is : " , msg)
    encypted = rsa.encrypt(msg)
    
    print("encrypted rsa : " , encypted)

    decrypted = rsa.decrypt(encypted)
    
    print("decrypted rsa : " , decrypted)