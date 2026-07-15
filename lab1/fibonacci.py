# def fibonacci_iterative(n):
#     if n== 1:
#         return 0
#     if n == 2:
#         return 1
#     a,b=0,1
#     for i in range(3,n+1):
#         a,b=b,a+b
#     return b


def fibonacci_recursive(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    return fibonacci_recursive(n-1)+ fibonacci_recursive(n-2)
    

print("Fibonacci =",fibonacci_recursive(9)) 