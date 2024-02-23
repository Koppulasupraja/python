a=float(input("enter first no"))
b=float(input("enter second no"))
c=float(input("enter third no"))
d=float(input("enter fouth no"))
if(a>b and a>c and a>d):
    print("the greatest no is:",a)
elif(b>c and b>d):
    print("the gretest no is:",b)
elif(c>d):
   print("the greatest no is:",c)
elif(d>c):
    print("the greatest no is:",d)
else:
    print("either any two values or all the four values are equal")