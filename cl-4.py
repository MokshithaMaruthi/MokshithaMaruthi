n=int(input("enter range: "))
a=[]
for i in range(0,n):
    x=int(input("enter: "))
    a.append(x)
print(a)
b=[]
for i in range(0,n):
    y=int(input("enter: "))
    b.append(y) 
print(b)
sum=0
for i in range(0,n):
    sum+=(a[i]*b[i])
print(sum)
    
