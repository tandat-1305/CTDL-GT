ar = []
for x in range(15):
    a = random.randint(-100,100)
    ar.append(a)

def merge(ar, l, m, r):
#l : left index 
#r : right index
    x1 = m - l + 1
    x2 = r- m
  
    L = [0] * (x1)
    R = [0] * (x2)
  
    for i in range(0 , x1):
        L[i] = ar[l + i]
    for j in range(0 , x2):
        R[j] = ar[m + 1 + j]

    i = 0  
    j = 0     
    k = l    
  
    while i < x1:
        ar[k] = L[i]
        i += 1
        k += 1

    while i < x1 and j < x2 :
        if L[i] <= R[j]:
            ar[k] = L[i]
            i += 1
        else:
            ar[k] = R[j]
            j += 1
        k += 1


    while j < x2:
        ar[k] = R[j]
        j += 1
        k += 1

def mergeSort(ar,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(ar, l, m)
        mergeSort(ar, m+1, r)
        merge(ar, l, m, r)
  
print("array: ",ar)
n = len(ar)
print ("Sorted array :")
for i in range(n):
    print ("%d" %ar[i])
print ("Given array :")

for i in range(n):
    print ("%d" %ar[i]),
mergeSort(ar,0,n-1)