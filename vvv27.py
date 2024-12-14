l=list(map(int,input().split()))
count=0
max=0
for i in l:
    if i>max:
        max=i
        count=count+1
print(count)
        
        
