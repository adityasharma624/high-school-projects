from matplotlib 
n=int(input("Input the number: "))
maxa=0
steps=0
while n!=1:
    if n%2==0:
        n=int(n/2)
        print(n)
        if n>maxa:
            maxa=n
        steps+=1
    else:
        n=3*n+1
        print(n)
        if n>maxa:
            maxa=n
        steps+=1
print(maxa,"is the highest point")
print("No. of steps taken to reach 1:",steps)