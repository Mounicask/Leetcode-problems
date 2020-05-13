#TWO PAIR SUM

#Using two list

ar = [1, 4, 45, 6, 10, -8 ]
tar = 16
ar2 = ar
for i in ar:
    if tar-i in ar2:
        print(i,tar-i)
        ar2.remove(tar-i)
        
        
#Using two pointer approach
        
ar = [ 1, 4, 45, 6, 10, 8]
tar = 16
left = 0
right = len(ar) - 1
ar.sort()
print(ar)
while left<right:
    if ar[left] + ar[right] > tar:
        right = right-1
    elif ar[left] + ar[right] < tar:
        left =left +1
    else:
        print(ar[left],ar[right])
        left = left+1
        right = right -1
        