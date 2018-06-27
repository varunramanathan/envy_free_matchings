import heapq
'''
input starts with number of hospitals and number of doctors space separated
For each hospital, there are two lines of input
the first line contains "l u" (without the quotes) which are the lower and upper quotas
the second line contains a list of space seperated values, the ith of which denotes the ith preferred doctor

For each doctor, there is a single line of input
The line contains a list of space seperated values, the ith of which denotes the ith preferred hospital
'''

hd = list(map(int,input().rstrip().split(" ")))
h = hd[0]
d = hd[1]
print(h)
h_l_u = [] # (lower quota,upper quota) of hospital i at ith index
h_list = dict() # a dict of (key,value)->(doctor,preference) of hospital i at ith index
# # h_list_dict = dict()
d_list = dict() # tuples of the kind (doctor number, a dict of (key,value)->(hospital,preference) of
# # doctor i at ith index, a dict of (key, value)->(preference,hospital) of doctor i at ith index)
# # d_list_2 = [] #a dict of (key, value)->(preference,hospital) of doctor i at ith index
# # d_list_dict = dict()
for i in range(h):
    lu = list(map(int,input().rstrip().split(" ")))
    h_l_u.append((lu[0],lu[1]))
    ar = list(map(int,input().rstrip().split(" ")))
    h_list[i] = ({ar[j]:j for j in range(len(ar))},{j:ar[j] for j in range(len(ar))})
print(h_list)
for i in range(d):
    ar = list(map(int, input().rstrip().split(" ")))
    d_list[i] = ({ar[j]:j for j in range(len(ar))},{j:ar[j] for j in range(len(ar))})
print(d_list)
unassigned = set([i for i in range(d)])
print("unassigned = "+str(unassigned))
assigned = set()
cant_assign = set()
start_from = [0 for i in range(d)]
h_docs_assigned_heaps = [[] for i in range(h)]
while(unassigned):
    d = unassigned.pop()
    unassigned.add(d)
    print("popping "+str(d)+" right now (but also added it)")
    for h in d_list[d][0]:
        print("looking at hospital "+str(h))
        if h<start_from[d]:
            print("already looked at this hospital for this doctor")
            continue #if you have already evaluated this hospital, you won't need to come here again
        start_from[d] = h+1
        if d not in h_list[h][0]: #d is not acceptable for hospital h
            print(str(d)+" is not accepted by "+str(h))
            continue
        else:
            if len(h_docs_assigned_heaps[h])==h_l_u[h][0]: #all places are filled
                print("all the places have been filled at "+str(h))
                min_doc_removed_pref = heapq.heappop(h_docs_assigned_heaps[h]) #the worst ranked doc's ranking
                min_doc_removed = h_list[h][1][min_doc_removed_pref]

                if min_doc_removed_pref>h_list[h][0][d]: #if d has a better rank than the worst ranked doc's rank
                    #add d to assigned and add d to h_docs_assigned_heaps[h][0]
                    print("assigned was: "+str(assigned))
                    assigned.add(d)
                    print("assigned is "+str(assigned))
                    print("unassigned was: " + str(unassigned))
                    unassigned.remove(d)
                    print("unassigned is: " + str(unassigned))
                    heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])

                    print("assigned was: " + str(assigned))
                    assigned.remove(min_doc_removed)
                    print("assigned is " + str(assigned))
                    print("unassigned was: " + str(unassigned))
                    unassigned.add(min_doc_removed)
                    print("unassigned is: " + str(unassigned))
                else: #cannot replace anyone
                    heapq.heappush(h_docs_assigned_heaps[h],min_doc_removed_pref)
                    continue
            else: #some space is still left
                heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])
                print("assigned doc "+str(d)+" to hospital "+str(h))
                assigned.add(d)
                print("unassigned-")
                print(unassigned)
                unassigned.remove(d)
    if start_from[d]>= h: #no more hospitals left to start
        if d in unassigned:
            unassigned.remove(d)
            cant_assign.add(d)
            if d in assigned:
                print("Wtf")
print("assigned -")
print(assigned)
print("unassigned -")
print(unassigned)
print("can't assign -")
print(cant_assign)
print("h is "+str(h))
for i in range(hd[0]):
    print("hospital "+str(i)+" has the following doctors")
    for pref in h_docs_assigned_heaps[i]:
        print(h_list[i][1][pref])