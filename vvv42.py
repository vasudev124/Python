s=input()
n=len(s)
res=[]
for i in range(n):
    if res and s[i]==res[-1]:
        stack.pop()
    else:
        stack.append(s[i])
print("".join(stack)
