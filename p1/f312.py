#2025-01-04
a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
n=int(input())
m=-100000
for i in range(n+1):
    at=(a*i*i+b*i+c)+(d*(n-i)*(n-i)+e*(n-i)+f)
    if at>m:
        m=at
print(m)
