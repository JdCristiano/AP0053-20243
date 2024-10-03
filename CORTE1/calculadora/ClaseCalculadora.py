class Add_Sud:
    def add(self, a, b):
        self.r = a+b
    def sud(self, a, b):
        self.r = a-b    
    def multi(self, a, b):
        self.r = a*b
    def divi(self, a, b):
     if b==0:
        print("no se puede dividir entre 0")
     else:
        self.r = a/b
    def imprimirResultado(self):
        print("el resultado es", self.r)


