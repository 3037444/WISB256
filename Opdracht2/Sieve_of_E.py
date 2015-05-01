import sys
import time

N = int(sys.argv[1])
file = str(sys.argv[2])

T1 = time.perf_counter()

def priemgetallen(integer):
    lijst=[]
    for i in range(N+1):
        lijst.append(i)
    del lijst[0]
    del lijst[0]
    return lijst

def priemtest(integer, lijst):
    i = 0
    n = 2
    while i < len(lijst):
        j = n * lijst[i]
        if j <= integer:
            if j in lijst:
                lijst.remove(j)
                n = n + 1
            else:
                n = n + 1
        if j > integer:
            i = i + 1
            n = 2
    return lijst

lijst = priemgetallen(N)
lijst = priemtest(N, lijst)

T2 = time.perf_counter()

T = T2 - T1

bestand = open(file, 'w')
for number in lijst:
    bestand.write(str(number) + "\n")

bestand.close()

print("Found {:d} Prime numbers smaller than {:d} in {:0.15f} sec".format(len(lijst), N, T)) 