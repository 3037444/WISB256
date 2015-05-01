import sys
import time

N = int(sys.argv[1])
file = str(sys.argv[2])

T1 = time.perf_counter()

def priemgetallen(integer):
    lijst=[]
    lengte = int((N+(N%2))/2-1)
    for i in range(lengte):
        lijst.append(True)
    return lijst

def priemtest(integer):
    lijst = priemgetallen(integer)
    lengte = len(lijst)
    i = 0
    while i**2 < lengte:
        if lijst[i] == False:
            i = i + 1
        else:
            n  =  i + (2*i +3)
            while n < lengte:
                lijst[n] = False
                n = n + (2*i + 3)
            i = i +1
    return lijst

def Bool_naar_int(lijst):
    deflijst= [2]
    for i in range(len(lijst)):
        if lijst[i] == True:
            deflijst.append(2*i+3)
    return deflijst
    
lijst = priemtest(N)
lijst = Bool_naar_int(lijst)

T2 = time.perf_counter()

T = T2 - T1

bestand = open(file, 'w')
for number in lijst:
    bestand.write(str(number) + "\n")

bestand.close()
    
print("Found {:d} Prime numbers smaller than {:d} in {:0.15f} sec".format(len(lijst), N, T)) 
