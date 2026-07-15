def gcd(a,b):
    if a == 0 and b== 0:
        return "Undefined"
    if b==0:
        return a
    if a==0:
        return b
    while b!= 0:
        a,b=b,a%b
    return a 


# def gcd(a,b):
#     if a==0 and b==0:
#         return "Undefined"
#     if b==0:
#         return a
#     if a==0:
#         return b
    
#     return gcd(b,a%b)


print ("GCD = ",gcd(33,55))




