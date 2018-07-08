from random import randint,shuffle
# hd = list(map(int,input().rstrip().split(" ")))
hd = [4,12]
print(str(hd[0])+" "+str(hd[1]))
for h in range(1,hd[0]+1):
    l = randint(1,hd[1]//2)
    u = randint(hd[1]//2,hd[1])
    doctors = []
    while (doctors == []):
        for d in range(1, hd[1]+1):
            doc = randint(0, 1)
            if doc == 1:
                doctors.append(d)
    shuffle(doctors)
    print(str(l)+" "+str(u))
    print(*doctors)
for d in range(1,hd[1]+1):
    hospitals = []
    while hospitals == []:
        for h in range(1, hd[0]+1):
            hos = randint(0, 1)
            if hos == 1:
                hospitals.append(h)
    shuffle(hospitals)
    print(*hospitals)