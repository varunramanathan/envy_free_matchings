import heapq
'''
input starts with number of hospitals and number of doctors space separated
For each hospital, there are two lines of input
the first line contains "l u" (without the quotes) which are the lower and upper quotas
the second line contains a list of space seperated values, the ith of which denotes the preference given to the
ith doctor. if the ith value is -1, then the doctor is unacceptable

For each doctor, there is a single line of input
The line contains a list of space seperated values, the ith of which denotes the preference given to the
ith hospital. if the ith value is -1, then the hospital is unacceptable
'''

h,d = list(map(int,input().rstrip().split(" ")))
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
    h_list[i] = ({ar[j]:j for j in range(len(ar)) if ar[j]!=-1},{j:ar[j] for j in range(len(ar)) if ar[j]!=-1})
for i in range(d):
    ar = list(map(int, input().rstrip().split(" ")))
    d_list[i] = ({ar[j]:j for j in range(len(ar)) if ar[j]!=-1},{j:ar[j] for j in range(len(ar)) if ar[j]!=-1})

unassigned = set([i for i in range(d)])
assigned = set()
cant_assign = set()
start_from = [0 for i in range(d)]
h_docs_assigned_heaps = [[] for i in range(h)]
while(unassigned):
    d = unassigned.pop()
    for h in d_list[d][2]:
        if h<start_from[d]: continue
        start_from[d] = h+1
        if d not in h_list[h][0]:
            continue
        else:
            if len(h_docs_assigned_heaps[h])==h_l_u[h][0]: #all places are filled
                if h_docs_assigned_heaps[h][0]>h_list[h][0][d]: #if d can replace someone
                    #add d to assigned and add d to h_docs_assigned_heaps[h][0]
                    assigned.add(d)
                    unassigned.remove(d)
                    heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])
                     #remove the lowest preferred doc who had been assigned earlier
                    min_doc_removed_pref = heapq.heappop(h_docs_assigned_heaps[h])
                    min_doc_removed = h_list[h][1][min_doc_removed_pref]
                    assigned.remove(min_doc_removed)
                    unassigned.add(min_doc_removed)
                else:
                    continue
            else:
                heapq.heappush(h_docs_assigned_heaps[h],h_list[h][0][d])
                assigned.add(d)
                unassigned.remove(d)
    if start_from[d]>h:
        if d in unassigned: unassigned.remove(d)
        else: cant_assign.add(d)

for i in range(h):
    print("Doctors in "+h+" are "+str([h_list[i][1][pref] for pref in h_docs_assigned_heaps[i]]))