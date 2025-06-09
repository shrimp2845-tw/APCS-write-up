#2024-11-09
def rotate(ol):#old list
    nl=[]#new list
    for i in range(len(ol[0])):
        sp=[]
        for j in range(len(ol)):
            sp.append(ol[len(ol)-1-j][i])
        nl.append(sp)
    return nl
def spin(ol):
    nl=[]
    for i in range(len(ol)):        
            nl.append(ol[len(ol)-1-i])
    return nl
l=[]
r,c,m=map(int,input().split())
for i in range(r):
    l.append(list(map(int,input().split())))
step=list(map(int,input().split()))
for i in range(len(step)):
    if step[len(step)-1-i]==0:
        l=list(rotate(rotate(rotate(l))))
    else:
        l=list(spin(l))
print(str(len(l))+" "+str(len(l[0])))    
for i in l:
    for j in range(len(i)):
        print(i[j],end="")
        if j+1!=len(i):
            print(" ",end="")
    print("")
