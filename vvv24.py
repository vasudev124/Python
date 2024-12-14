l=list(map(int,input().split()))
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
    else:
        l1.insert(0,i)
print(l1)
