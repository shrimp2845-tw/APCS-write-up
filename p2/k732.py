#2024-11-05
n,m=map(int,input().split())
a=[]
b=[]
def mdis(a,b,c,d):
    m=abs(a-c)+abs(b-d)
    return m
for i in range(n):
    r=list(map(int,input().split()))
    a.append(r)
for i in range(n):
    for j in range(m):
        c=0
        for k in range(i-a[i][j],i+a[i][j]+1):
                for l in range(j-a[i][j],j+a[i][j]+1):
                    try:
                        if a[i][j]>=mdis(i,j,k,l) and l>-1 and k>-1 :
                            c+=a[k][l]
                    except:
                        pass
        
        if c%10==a[i][j]:
            b.append([i,j])
print (len(b))
for i in range(len(b)):
    print(str(b[i][0]),str(b[i][1]))
