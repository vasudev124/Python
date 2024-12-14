n=int(input())
l=list(map(int,input().split()))
pol=0
unsol=0
for i in l:
    if i==-1:
        if pol>0:
            pol=pol-1
        else:
            unsol=unsol+1
    else:
        pol=pol+i
print(unsol)

    
        
