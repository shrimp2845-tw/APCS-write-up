#2025-04-22
t=int(input())
results=[]
from itertools import chain
for i in range(t):
    a,b=map(int,input().split())
    if a!=b:
       results.append((a,b))
results.sort()
merged=[]
for i in results:
    if not merged or merged[-1] [1]< i[0]:
        merged.append(list(i))
    elif merged[-1][1]<i[1]:
        merged[-1][1]=i[1]
length=sum((b-a) for a,b in merged)
print(length)
