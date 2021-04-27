def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    print("The factorial of {0} is {1}".format(n,p))

n=int(input("Enter a number"))
fact(n)


