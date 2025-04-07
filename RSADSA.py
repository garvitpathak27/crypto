class RSADSA: 
    def __init__(self, p, q, e, msg): 
        self.p = p 
        self.q = q 
        self.e = e 
        self.msg = msg 
        self.n = p * q 
        self.phi = (p - 1) * (q - 1) 
        self.d = pow(self.e, -1, self.phi) 
        self.public_key = (self.e, self.n) 
        self.private_key = (self.d, self.n) 
 
    def sign(self): 
        s = pow(self.msg, self.d, self.n) 
        return s 
     
    def verify(self): 
        s = self.sign() 
        rec_msg = pow(s, self.e, self.n) 
        print(rec_msg) 
 
rsadsa = RSADSA(p=61, q=53, e=17, msg=123) 
rsadsa.verify()
