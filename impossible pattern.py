n=int(input("Enter the number of lines: "))
h=0
d=n//2+1
for r in range(0, n):
    s=''
    for c in range(1, n+1):
        if r<d:
            h=r*2
        elif r==d:
            h=d
        else:
            h=int(d/3)
        s+=str(h*n+c) + ' '
    print(s)
