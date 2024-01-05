from itertools import permutations


k=0
for x in permutations('iiiiirrrrrrsssssss', r=18):
    w = ''.join(x)
    print(w)
    k+=1
print(k)