#Hackerrank Minion Game

S = 'BANANA'
lis=[]
A = 0
B = 0
for i in range(0,len(S)):
    for j in range(i,len(S)+1):
        if i!=j:
            lis.append(S[i:j])

vowels = ['A','E','I','O','U','a','e','i','o','u']
for i in lis:
    if i[0] in vowels:
        B = B +1
    else:
        A = A +1
if A>B:
    print('Stuart',A)
elif A == B:
    print('DRAW')
else:
    print('Kevin',B)