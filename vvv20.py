l=list(map(int,input().split()))
num=0
e=0
l2=[]
for i in range(1,4):
    num=min(l)
    l2.append(num)
    l.remove(num)
print(sum(l2))
    

    
    
    
    
