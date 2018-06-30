import heapq
'''
This code finds the stable matching for the HR instance where lower bounds are replaced by zero
and upper bounds are replaced by the original lower bounds.

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
h_l_u = [(0,0)] # (lower quota,upper quota) of hospital i at ith index
h_list = dict() # a dict of (key,value)->(doctor,preference) of hospital i at ith index
# # h_list_dict = dict()
d_list = dict() # tuples of the kind (doctor number, a dict of (key,value)->(hospital,preference) of
# # doctor i at ith index, a dict of (key, value)->(preference,hospital) of doctor i at ith index)
# # d_list_2 = [] #a dict of (key, value)->(preference,hospital) of doctor i at ith index
# # d_list_dict = dict()
for i in range(1,h+1):
    lu = list(map(int,input().rstrip().split(" ")))
    h_l_u.append((lu[0],lu[1]))
    ar = list(map(int,input().rstrip().split(" ")))
    h_list[i] = ({ar[j]:j for j in range(len(ar))},{j:ar[j] for j in range(len(ar))})
print(h_list)
for i in range(1,d+1):
    ar = list(map(int, input().rstrip().split(" ")))
    d_list[i] = ({ar[j]:j for j in range(len(ar))},{j:ar[j] for j in range(len(ar))})
print(d_list)
unassigned = set([i+1 for i in range(d)])
print("unassigned = "+str(unassigned))
assigned = set()
cant_assign = set()
start_from = [0 for i in range(d+1)]
h_docs_assigned_heaps = [[] for i in range(h+1)]
while(unassigned):
    d = unassigned.pop()
    unassigned.add(d)
    print("Doctor: "+str(d))
    for pref in range(len(d_list[d][1])):
        h = d_list[d][1][pref]
        print("Hospital "+str(h))
        if pref<start_from[d]:
            print("Already done with hospital "+str(h))
            continue #if you have already evaluated this hospital, you won't need to come here again
        start_from[d] = pref+1
        if d not in h_list[h][0]: #d is not acceptable for hospital h
            print("Doctor "+str(d)+" is not accepted by hospital"+str(h)+".")
            continue
        else:
            print("Doctor " + str(d) + " IS accepted by hospital" + str(h) + ".")
            if len(h_docs_assigned_heaps[h])==h_l_u[h][0]: #all places are filled
                print("But all the places have been filled at hospital "+str(h)+".")
                print("Doctors at hospital "+str(h)+" are : "+str(h_docs_assigned_heaps[h])+".")
                min_doc_removed_pref = heapq.heappop(h_docs_assigned_heaps[h]) #the worst ranked doc's ranking
                min_doc_removed = h_list[h][1][min_doc_removed_pref]
                print("Lowest ranked doctor in hospital "+str(h)+" right now is "+str(min_doc_removed)+" with preference "+str(min_doc_removed_pref)+".")
                if min_doc_removed_pref>h_list[h][0][d]: #if d has a better rank than the worst ranked doc's rank
                    print("But the preference of present doctor "+str(d)+" is "+str(h_list[h][0][d])+", which is better.")
                    #add d to assigned and add d to h_docs_assigned_heaps[h][0]
                    # print("assigned was: "+str(assigned))
                    assigned.add(d)
                    # print("assigned is "+str(assigned))
                    # print("unassigned was: " + str(unassigned))
                    unassigned.remove(d)
                    # print("unassigned is: " + str(unassigned))
                    heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])

                    # print("assigned was: " + str(assigned))
                    assigned.remove(min_doc_removed)
                    # print("assigned is " + str(assigned))
                    # print("unassigned was: " + str(unassigned))
                    unassigned.add(min_doc_removed)
                    # print("unassigned is: " + str(unassigned))
                    print("So removing "+str(min_doc_removed)+" and adding "+str(d)+" to hospital "+str(h)+".")
                    break
                else: #cannot replace anyone
                    print("But the preference of present doctor " + str(d) + " is " + str(h_list[h][0][
                        d]) + ", which is NOT better.")
                    heapq.heappush(h_docs_assigned_heaps[h],min_doc_removed_pref)
                    continue
            else: #some space is still left
                print("And, there is space!")
                heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])
                print("Assigned doctor "+str(d)+" to hospital "+str(h)+".")
                assigned.add(d)
                # print("unassigned-")
                # print(unassigned)
                unassigned.remove(d)
                # print("unassigned-")
                # print(unassigned)
                break
    if start_from[d]>= len(d_list[d][0]): #no more hospitals left to start
        print("All hospitals for doctor "+str(d)+" have been checked already.")
        if d in unassigned:
            unassigned.remove(d)
            cant_assign.add(d)
            if d in assigned:
                print("Wtf")
# print("assigned -")
# print(assigned)
# print("unassigned -")
# print(unassigned)
# print("can't assign -")
# print(cant_assign)
# print("h is "+str(h))
for i in range(1,hd[0]+1):
    print("hospital "+str(i)+" has the following doctors")
    for pref in h_docs_assigned_heaps[i]:
        print(h_list[i][1][pref])