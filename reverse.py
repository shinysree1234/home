n=int(input("enter a number"))
r=0
while n>0:
    rem=int(n%10)
    r=(r*10)+rem
    n=int(n/10)
print (r)