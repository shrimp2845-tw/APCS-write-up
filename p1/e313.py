#2025-05-21
n=int(input())
l=[input() for i in range(n)]
l.sort(reverse=True)
s=[set(list(i)) for i in l]
ml=1001
ans=""
c=0
for i in s:
    if len(i)<=ml:
        ml=len(i)
        ans=l[c]
    c+=1
print(ans)
