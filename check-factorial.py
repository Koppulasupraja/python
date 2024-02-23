a=int(input("enter a number"))
factorial=1
if a<0:
    print("sorry,factorial number does not exits for negative numbers ")
elif(a==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
        print("the factorialof",a,"i",factorial)