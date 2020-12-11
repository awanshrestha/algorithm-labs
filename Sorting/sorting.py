def insertionSort(data):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while(i >= 0 and data[i] > key):
            data[i + 1] = data[i]
            i -= 1

        data[i + 1] = key

def mergeSort(data, p , r ):
    if p < r:
        midValue = (p + r) // 2
        mergeSort(data, p, midValue)
        mergeSort(data, midValue + 1, r)
        merge(data, p, midValue, r)

def merge(data, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * (n1)
    R = [None] * (n2)
 
    for i in range(0, n1):
        L[i] = data[p + i]
 
    for j in range(0, n2):
        R[j] = data[q + 1 + j]
 
    i = 0
    j = 0
    k = p
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i = i + 1
        else:
            data[k] = R[j]
            j = j + 1
        k = k + 1
 
    while i < n1:
        data[k] = L[i]
        i = i + 1
        k = k + 1
 
    while j < n2:
        data[k] = R[j]
        j = j + 1
        k = k + 1
