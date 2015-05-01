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

def priemtest(integer, lijst):
    i = 2
    j = 4
    lijst2 = []
    
    while i < len(lijst):
        if lijst[i]!=0:
            if j <= integer:
                lijst[j]=0
                j = j + i
            if j > integer:
                i = i + 1
                j = 2*1
        else:
            i = i + 1
            
    for i in range(len(lijst)-1):
        if lijst[i] != 0:
            lijst2.append(lijst[i])
    return lijst2

lijst = priemgetallen(N)
lijst = priemtest(N, lijst)
print(lijst)

T2 = time.perf_counter()

T = T2 - T1

bestand = open(file, 'w')
for number in lijst:
    bestand.write(str(number) + "\n")

bestand.close()

print("Found {:d} Prime numbers smaller than {:d} in {:0.15f} sec".format(len(lijst), N, T)) 