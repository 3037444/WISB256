import sys
import random
import math

try:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
except:
    print("Use: estimate_pi.py N L")
    exit(1)

try:
    seed = int(sys.argv[3])
except:
    seed = None

random.seed(seed)
n = 1
h = 0

def drop_needle(integer):
    x = random.random()
    a = random.vonmisesvariate(0,0)
    verschil = math.cos(a)
    eindpunt = x + (integer * math.cos(a))
    if 0 < eindpunt and eindpunt < 1:
        return False
    else:
        return True

while n < N:
    waar = drop_needle(L)
    if waar == True:
        h = h +1
    n = n+1

if L <= 1:
    x = (2*n*L)/h
    print("{:d} hits in {:d} tries".format(h, n) + "\n"
    + "Pi = " + str(x))
else:
    invers = math.asin(L**(-1))
    teller = 2*(L -  math.sqrt(L**2 -1) - invers)
    noemer = h/n -1
    x = teller/noemer
    print("{:d} hits in {:d} tries".format(h, n) + "\n"
    + "Pi = " + str(x))