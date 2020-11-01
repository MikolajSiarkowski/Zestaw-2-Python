L1 = ['a','b','c','d','f']
L2 = ['a','f','d','g','a']
L3 = []
for i in range(len(L1)):
    for j in range(len(L2)):
      if L1[i] == L2[j]:
             L3 += L1[i]
L3 = set(L3)
print(L3)         
