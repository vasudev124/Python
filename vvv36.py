num=int(input())
n=list(map(int,input().split()))
tot=0
c=0
for i in n:
    tot=tot+i
    if tot==0:
        c=c+1
print(c)
    
        
