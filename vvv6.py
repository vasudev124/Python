n=int(input())
numb=n
num=0
mul=1
while (n!=0):
    num=n%10
    mul*=num
    n=n//10
print(mul)
