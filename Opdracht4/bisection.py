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
    
def findRoots(f, a, b, epsilon):
    m = (float(a)+float(b))/2.0
    if f(m) == 0:
        root = m
    if math.fabs(b-a) < epsilon:
        root = m
    elif f(a)*f(m) < 0:
        root = findRoots(f, a, m, epsilon)
    elif f(b)*f(m) < 0:
        root = findRoots(f, m, b, epsilon)
    return root
    
def findAllRoots(f, a, b, epsilon):
    n = math.fabs(b-a)/epsilon
    lijst = []
    i = 0
    while i < n:
        c = a + i * epsilon
        d = a + (i+1) * epsilon
        if f(c)*f(d) < 0:
            root = float(findRoots(f,c,d, epsilon))
            print(root)
            lijst.append(root)
        i = i +1
    return lijst
        