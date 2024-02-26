def cs(a,k):
    n = len(a)
    c = [0]*k
    b = [0]*n
    for i in range(n):
        c[a[i]] +=1
    for i in range(1,k):
        c[i] = c[i]+c[i-1]
    for i in range(n-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    return b



a = [2,5,6,7,1,2,2,5]
print(cs(a,8))
