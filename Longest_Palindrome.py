a = "babad"
long_palindrome = ''
for i in range(0,len(a)+1):
    for j in range(0,len(a)+1):
        if i!=j and j>i:
            val = a[i:j]
            if val == val[::-1]:
                if len(long_palindrome)<len(val):
                    long_palindrome = val
print("long_palindrome is ",long_palindrome)