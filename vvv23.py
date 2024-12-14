l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
l1.sort()
l1.reverse()
l2.sort()
l1.extend(l2)
print(l1)
