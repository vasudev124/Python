def nat(n):
    if(n==0):
        return 1
    else:
        return n*nat(n-1)
num=int(input())
print(nat(num))
