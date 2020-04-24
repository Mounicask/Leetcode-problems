name='BANANA'
lis=['A','E','I','O','U']
list1=[]
length=len(name)
vowcount,conscount=0,0
for i in range(0,length):
    if(name[i] in lis):
       vowcount=vowcount+(length-i)
    else:
        conscount=conscount+(length-i)
if(vowcount>conscount):
    print("kevin",vowcount)
elif(vowcount==conscount):
    print("Draw")
else:
    print("Stuart",conscount)