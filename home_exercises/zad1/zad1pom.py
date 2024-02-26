def palindrom_np(s, i, j):
    if len(s) % 2 == 1:
        ni, nj = i, j
        while ni <= nj:
            if s[ni] != s[nj]:
                return False
            ni+=1
            nj-=1
        return True
    else:
        return False


def ceasar( s ):
    n = len(s)
    ml = 0
    i = 0
    j = n-1
    r = n-1
    while j<n:
        if palindrom_np(s,i,j):
            ml = j - i
            break
        j+=1
        i+=1
        if j==n:
            r-=1
            i = 0
            j = r
    return ml

def maks(a,b):
    if a>b:
        return a
    return b

def new(s):
    n = len(s) #len s
    ml = 1 #odp
    le = 1 # dlugosc aktualnie sprawdzana
    i=1 #srodek prawdopodobnego palindromu
    while i<n-ml:
        l = i-1
        r = i+1
        while l>=0 and r<n:
            if s[l] != s[r]:
                ml = maks(le, ml)
                break
            else:
                le += 2
            l-=1
            r+=1
        ml = maks(le, ml)
        i+=1
        le = 1
    return ml

print(new("akontnoknonabcddcba"))


