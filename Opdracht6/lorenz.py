import math
import numpy as NP
from scipy import *
from Vector import *
from scipy.integrate import odeint
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

class Lorenz(object):

    def __init__(self, vector, sigma = 10, rho = 28, beta = 8/3):
        self.plaats = vector
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
    
    def f(self, vector,t):
        x = vector[0]
        y = vector[1]
        z = vector[2]
        
        f0 = self.sigma*(y - x)
        f1 = x*(self.rho - z) - y
        f2 = x*y - self.beta*z
        
        return [f0, f1, f2]
    
    def solve(self, T, dt):
        aantal = int(T/dt)
        t  = []
        for i in range(aantal + 1):
            t.append(i*dt)
        opl = odeint(self.f, self.plaats, t)
        return opl
    
    def df(self):
        p = self.f
        J = NP.array[(-self.sigma, self.sigma, 0),(self.rho-p[2], -1, -p[0]),(p[1],p[0],-self.beta)]
        return J
    
    def isStable(self):
        J = self.df
        EV = NP.linalg.eigh(J)
        i = 0
        while i < len(EV):
            if EV[i] < 0:
                i = i + 1
            else:
                return False
        return True
        