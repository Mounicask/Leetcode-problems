#Question:
#If first person kills second and so one, who will survive atlast.
#Answer : 73

l = []
for i in range(1,101):
    l.append(i)
print(l)

def programmer_thinks(l):
    inter = []
    for i in range(0,len(l)):
        if i % 2 !=0:
            inter.append(l[i])
    if len(l) %2 !=0:
        l.remove(l[0])
    l = [i for i in l if i not in inter] 
    if len(l)!=1:
        return programmer_thinks(l)
    else:
        return l
    
val = programmer_thinks(l)
print(val)

