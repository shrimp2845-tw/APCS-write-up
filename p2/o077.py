#2025-05-01
def sd(x,y,d,h,w):
    ps=[]
    for i in range(y-d,y+d+1):
        if i>=0 and i<h:
            for j in range(x-d,x+d+1):
                if j>=0 and j<w:
                    ps.append([i,j])
    def f(l):
        if abs(l[0]-y)+abs(l[1]-x)<=d:
            return True
        return False
    ps=filter(f,ps)    
    return ps
h,w,n=map(int,input().split())
m=[[0 for i in range(w)] for j in range(h)]
for i in range(n):
    r,c,t,x=map(int,input().split())
    for j in sd(c,r,t,h,w):
        m[j[0]][j[1]]+=x
for i in m:
    print(' '.join(list(map(str,i))))
