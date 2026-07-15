def seqSearch(a,target):
    for i in range (len(a)):
        if a[i] == target:
            return i
    return -1

A=[1,2,3,4,5,6,7,8,9]
target=7

if (seqSearch(A,target) == -1):
    print(f"{target} Not Found")
else:
    print(f"{target} found at {seqSearch(A,target)} index")

