#2024-11-09
x,n=map(int,input().split())
l=list(map(int,input().split()))
left=0
right=0
rl=[]
ll=[]
for i in l:
    if i>x:
        right+=1
        rl.append(i)
    elif i<x:
        left+=1
        ll.append(i)
if right>left:
    print(right,end=" ")
    print(max(rl))
else:
    print(left,end=" ")
    print(min(ll))
