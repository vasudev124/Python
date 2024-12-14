n,x=map(int,input().split())
if n<=x:
    print("1")
elif n%x==0:
    print(n//x)
else:
    dig=(n//x)
    val=n%x
    print(dig+val)
    
