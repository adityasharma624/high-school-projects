'''
def oddprime(n):
    L=[]
    for num in range (2, n):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i)==0:  
                    break  
            else:
                L.append(num)
    return L


def goldbach():
    c=0
    while (c==0):
        N=int(input("Enter the number: "))
        if N<4 or N%2!=0:
            print("Enter a valid number")
        else:
            od=oddprime(N)
            L=[]
            for i in od:
                for j in od:
                    if i+j==N:
                        if (j,i) not in L:
                            L.append((i,j))
                            
            c=1
            for i in L:
                print(i)

def goldbachv2():
    c=0
    while (c==0):
        N=int(input("Enter the number: "))
        if N<4 or N%2!=0:
            print("Enter a valid number")
        else:
            for num in range (3, N):  
                    for i in range(3,num):  
                        if (num % i)==0 and num > 1:  
                            break  
                    else:
                        for j in range (2, N):  
                                for b in range(2,j):  
                                    if (j % b)==0 and j > 1:  
                                        break  
                                else:
                                    if num<N//2 and num+j==N:
                                        print(num,j)
            c+=1                            
                
    
    
    
goldbachv2()
'''

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def goldbachv3():
    c=0
    while (c==0):
        n=int(input("Enter number: "))
        if n<4 or n%2!=0:
            print("Input A Valid Number")
        else:
            i=0
            while i<n//2:
                if isprime(i):
                    diff=n-i
                    if isprime(diff):
                        print(i,diff)
                        
                i+=1
            c+=1
                        
                        
goldbachv3()

