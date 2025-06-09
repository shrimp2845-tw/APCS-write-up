#2025-05-19
#簡單到像p1 ：P
n,m,k=map(int,input().split())
m-=1
l=list(range(n))
sp=0
for i in range(k):
    sp+=m
    sp%=n
    del l[sp]
    n-=1
sp%=n
print(l[sp]+1)
