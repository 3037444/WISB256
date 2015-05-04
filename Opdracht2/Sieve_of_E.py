import sys
import time

N = int(sys.argv[1])
file = str(sys.argv[2])

T1 = time.perf_counter()

def priemgetallen(integer):
    lijst=[]
    for i in range(N+1):
        lijst.append(i)
    return lijst

def priemtest(integer):
    lijst = priemgetallen(integer)
    lijst[0] = 0
    lijst[1] = 0
    i = 2
    while i < len(lijst):
        if lijst[i] == 0:
            i = i +1
        else:
            j = i + i
            while j < len(lijst):
                lijst[j] = 0
                j = j + i
            if j >= len(lijst):
                i = i + 1
    return lijst

def lijstopschonen(lijst):
    schonelijst = []
    i = 0
    while i < len(lijst):
        if lijst[i] != 0:
            schonelijst.append(lijst[i])
            i = i + 1
        else:
            i = i +1
    return schonelijst
    
lijst = priemtest(N)
lijst = lijstopschonen(lijst)

T2 = time.perf_counter()

T = T2 - T1

bestand = open(file, 'w')
for number in lijst:
    bestand.write(str(number) + "\n")

bestand.close()

print("Found {:d} Prime numbers smaller than {:d} in {:0.15f} sec".format(len(lijst), N, T)) 