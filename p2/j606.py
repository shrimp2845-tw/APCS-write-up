#2024-11-08
old=[]
new=[]
al=[]
k,q,r=map(int,input().split())
s=input()
for i in s:
    old.append(i)
for i in range(k):
    new.append("")
for i in range(q):
    order=list(map(int,input().split()))
    x=0
    for j in order:
        new[j-1]=str(old[x])
        x+=1
    for j in range(k):
        old[j]=str(new[j])
    al.append(list(old))
    for j in range(k):
        new[j]=''
for i in range(r):
    for j in range(q):
        print(al[j][i],end='')
    print('')
