import math

class Vector(object):

    def __init__(self, n, v = 0.0):
        if isinstance(n, int):
            self.arg = n
            if isinstance(v, int):
                self.elements = n * [float(v)]
            if isinstance(v, float):
                self.elements = n * [v]
            elif isinstance(v,list):
                self.elements = v
        elif isinstance(n, list):
            self.arg = len(n)
            self.elements = n
        
        
    def __str__(self):
        temp = ''
        for i in self.elements:
            temp = temp + ("{0:.5f}".format(i) + "\n")
        return temp
    
    def scalar(self, alpha):
        product = []
        for i in self.elements:
            product.append(alpha * i)
        temp = Vector(product)
        return temp
    
    def add(self, other):
        temp = Vector(self.arg)
        for i in range(self.arg):
            temp.elements[i] = self.elements[i] + other.elements[i]
        return temp
    
    def lincomb(self, other, alpha, beta):
        temp1 = self.scalar(alpha)
        temp2 = other.scalar(beta)
        temp = temp1.add(temp2)
        return temp
        
    def inner(self, other):
        temp = 0
        for i in range(self.arg):
            temp = temp + self.elements[i]*other.elements[i]
        return temp
    
    def norm(self):
        temp = self.inner(self)
        temp = math.sqrt(temp)
        return temp
        
    def project(self, other):
        teller = self.inner(other)
        noemer = self.inner(self)
        breuk = teller/noemer
        temp = self.scalar(breuk)
        return temp
    
    def normaliseer(self):
        factor = self.norm()
        factor = 1/ factor
        temp = self.scalar(factor)
        return temp

def GrammSchmidt(self):
    temp = self
    for i in range(len(self)):
        j = i -1
        while j >= 0:
            verschil = temp[j].project(temp[i])
            temp[i] = temp[i].lincomb(verschil, 1, -1)
            j = j -1
        temp[i] = temp[i].normaliseer()
    return temp