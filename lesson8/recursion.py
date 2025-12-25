def factorial(n):
    if(n==0 or n==1):
        return 1
    return(n*factorial(n-1))

a=int(input("enter a number for factorial"))
b=factorial(a)
print("the factorial is ",b)
