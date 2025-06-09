#2025-01-21
a,b=map(int,input().split())
n=input()
c=list(map(int,input().split()))
t=0
for i in c:
    if i%(a+b)>=a:
        t+=b-(i%(a+b)-a)
print(t)
