997. Find the Town Judge

trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
trust = []
if len(trust) == 0:
    print("-1")
if N == 1:
    return -1
else:
    count = 0
    first = list(set([i[0] for i in trust]))
    second= list(set([i[1] for i in trust]))
    for i in first:
        if i in second:
            second.remove(i)
    if len(second) == 1:
        for i in first:
            if [i,second[0]] in trust:
                count = count + 1
    else:
        return ("-1")
    if count == len(first):
        return (second[0])
    else:
         return ("-1")
