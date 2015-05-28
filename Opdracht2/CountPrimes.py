import sys
import math

file = str(sys.argv[1])

lijst =[]

with open(file) as bestand:
    lijst = bestand.readlines()
for i in range(len(lijst)):
    lijst[i] = int(lijst[i])

def priemtweeling(lijst):
    t = 0
    lang = len(lijst)
    lang = lang -1
    lang = int(lang)
    for i in range(lang):
        if lijst[i + 1] == lijst[i] + 2:
            t = t +1
    return t

lengte = len(lijst)
N = lijst[lengte-1]
M = math.log(N)
O = N/M
R = lengte/O
T = priemtweeling(lijst)
C = 0.6601618
U = (2 * C * N) / (M**2)
V = T/ U


    
print("Largest Prime = " + str(N) + "\n"
+ "----------------------------------" + "\n"
+ "Pi(N)         = " + str(lengte) + "\n"
+ "N/log(N)      = " + str(O) + "\n"
+ "ratio         = " + str(R) + "\n"
+ "----------------------------------" + "\n"
+ "Pi_2(N)       = " + str(T) + "\n"
+ "2CN/log(N)^2  = " + str(U) + "\n"
+ "ratio         = " + str(V))