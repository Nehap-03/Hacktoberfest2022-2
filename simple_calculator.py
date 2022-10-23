a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
c=int(input("Enter slno. of operation to be done"))
if c==1:
    sum=a+b
    print("The result is - ",sum)
    
if c==2:
    diff=a-b
    print("The result is - ",diff)
    
if c==3:
    pro=a*b
    print("The result is - ",pro)

if c==4:
    div=a/b
    print("The result is - ",div)
