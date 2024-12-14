def xor(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
l=int(input("LL"))
u=int(input("UL"))
a=xor(l-1)
b=xor(u)
c=a^b
print(c)
