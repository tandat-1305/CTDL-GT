import random

ar = []
for x in range(15):
    a = random.randint(-100,100)
    ar.append(a)

def phan_vung(ar, low, high):
    i = (low-1)         
    pivot = ar[high]     
    for j in range(low, high):
        if ar[j] <= pivot:

            i = i+1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i+1], ar[high] = ar[high], ar[i+1]
    return (i+1)
  
def quickSort(ar, low, high):
    if len(ar) == 1:
        return ar
    if low < high:
        pi = phan_vung(ar, low, high)
        quickSort(ar, low, pi-1)
        quickSort(ar, pi+1, high)

print("array: ", arr)
n = len(ar)
quickSort(ar, 0, n-1)
print("Sorted aray is:")

for i in range(n):
    print("%d" % ar[i])