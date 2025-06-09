#2025-01-04
n,d=map(int,input().split())
money=0
c=0
for i in range(n):
    l=list(map(int,input().split()))
    m=max(l)
    s=min(l)
    if m-s>=d:
        money=money+(l[1]+l[2]+l[0])//3
        c+=1
print(c,money)
