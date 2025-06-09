#2025-05-21
n=int(input())
l=list(map(int,input().split()))
total=0
c=0
for i in l:
    if i!=0:
        pass
    elif c==0:
        total+=l[c+1]
    elif c==len(l)-1:
        total+=l[c-1]
    else:
        if l[c-1]>=l[c+1]:
            total+=l[c+1]
        else:
            total += l[c-1]
    c+=1
print(total)
