l1 = [line.rstrip('\n') for line in open(r'D:\compare1.txt', 'r')]
l2 = [line.rstrip('\n') for line in open(r'D:\compare2.txt', 'r')]
equal =[]
unequal = []
n1 = len(l1)
n2 = len(l2)
min_len = min(n1,n2)

for i in range(min_len):
    if l1[i] == l2[i]:
        equal.append("The line " + str(i) +" in file 1 is " + l1[i] +" and The line "+ str(i) + " in file 2 is " + l2[i])
    else: 
        unequal.append("The line " + str(i) +" in file 1 is " + l1[i] +" and The line " + str(i) +" in file 2 is " + l2[i])
        
if min_len == n1:
    for i in range(min_len,n2):
        unequal.append("No line in file 1 and The line " + str(i) +" in file 2 is " + l2[i])
else:
    for i in range(min_len,n1):
        unequal.append("The line " + str(i) +" in file 1 is " + l1[i] +" and No line in file 2")

with open(r'D:\equal_text.txt', 'w') as f:
    for i in equal:
        f.write("%s\n" %i)
        
with open(r'D:\unequal_text.txt', 'w') as f:
    for i in unequal:
        f.write("%s\n" %i)