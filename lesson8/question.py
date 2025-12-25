def greatest(a,b,c):
    if(a>b and a>c):
        print("the greatest number is ",a)
    elif(b>c and b>a):
        print("the greatest number is ",b)
    else:
        print("the greatest number is ",c)    

greatest(1,32,6)

def sum(n):

    if(n==1):
        return 1
    else:
        return(n+sum(n-1))

n=int(input("enter a number for finding the sum "))
p=sum(n)
print(p)         