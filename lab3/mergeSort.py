def merge(A, l, mid, r):

    #calculating number of left,right subarrays
    n1 = mid - l + 1
    n2 = r - mid
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
    # Copy left subarray to L
    for i in range(n1):
        L[i] = A[l + i]
    # Copy right subarray to R
    for j in range(n2):
        R[j] = A[mid + 1 + j]

    i = 0 # pointer for left subarray
    j = 0 # pointer for right subarray
    k = l # pointer for initial array

    # Merge the temporary arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[]
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[]
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2

        mergeSort(A, l, mid)
        mergeSort(A, mid + 1, r)
        merge(A, l, mid, r)



A = [38, 27, 43, 3, 9, 82, 10,44,61,0,2]
print("Original Array:", A)
mergeSort(A, 0, len(A) - 1)
print("Sorted Array:", A)


