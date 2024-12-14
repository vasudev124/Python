l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(len(l)):
    if i%2==0:
        l1.append(l[i])
for i in l1:
    if i%2!=0:
        l2.append(i)
print(sum(l2))
