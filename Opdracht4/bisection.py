import math

def findRoot(f, a, b, epsilon):
    Nmax = 100000
    N = 0
    m = (float(a)+float(b))/2.0
    while math.fabs(a-b) > epsilon and N < Nmax:
        if f(a) * f(m) < 0:
            b = m
            m = (float(a)+float(b))/2.0
            N= N +1
        elif f(m)*f(b) < 0:
            a = m
            m = (float(a)+float(b))/2.0
            N = N +1
        else:
            print("Fout!")
            exit(0)
    return m
