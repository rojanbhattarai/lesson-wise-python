def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

a=int(input("enter the number to calculate the factorial"))
print("the factorial of the number is ",factorial(a))

   