#Perform String Shifts
#You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
#
#direction can be 0 (for left shift) or 1 (for right shift). 
#amount is the amount by which string s is to be shifted.
#A left shift by 1 means remove the first character of s and append it to the end.
#Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
#Return the final string after all operations.

s = "yisxjwry"
shift = [[1,8],[1,4],[1,3],[1,6],[0,6],[1,4],[0,2],[0,1]]
for i in shift:
    if i[0] == 0:
        new = s[:i[1]]
        s = s.replace(new,'',1)
        s = s + new
    else:
        pos = -1 * i[1]
        new = s[pos:]
        s = s[:pos]
        s = new + s
print(s)


