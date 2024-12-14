s=input()
l=len(s)
c=0
if not l<=6 and l<=22:
    c=c+1
uc,lc,d,sc,p=1,1,1,1,0
spl_c=0
for i in range(l):
    if s[i].isupper():
        uc=0
    if s[i].islower():
        lc=0
    if s[i].isdigit():
        d=0
    if s[i] in "!@#$%^&*":
        spl_c+=1
    if i+1<l and s[i]==s[i+1]:
        p=p+1
if spl_c>=2:
    sc=0
c+=uc+lc+d+sc+p
print(c)


