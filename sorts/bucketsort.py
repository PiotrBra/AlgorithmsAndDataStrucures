
def insertion_sort(t):
    for i in range(1 ,len(t)):
        key = t[i]
        j = i - 1
        while j >= 0 and t[j] > key:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key
    return t

def bucket_sort(t):
    n = len(t)
    max_value = max(t)
    size = max_value / n
    buckets = []
    for i in range(n):
        buckets.append([])

    for i in range(n):
        j = int(t[i] / size)

        if j != n:
            buckets[j].append(t[i])
        else:
            buckets[n - 1].append(t[i])

    for i in range(n):
        insertion_sort(buckets[i])

    output = []
    for i in range(n):
        output = output + buckets[i]

    return output

