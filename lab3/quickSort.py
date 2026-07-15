def quickSort(A,low,high):
    if low<high :
        p=partition(A,low,high)
        quickSort(A,low,p-1)
        quickSort(A,p+1,high)


def partition(A,low,high):
    pivot = A[low]
    x=low+1
    y=high
    while x<=y:
        while x<=high and A[x]<=pivot:
            x=x+1
        while y>=low+1 and A[y] >= pivot:
            y=y-1

        if x<y:
            A[x],A[y]=A[y],A[x]
    
    A[low],A[y] = A[y],A[low]
    return y

A=[44,22,33,77,11,55,66]
print("Original Array : ",A)
quickSort(A,0,len(A)-1)
print("Sorted Array : ",A) 


