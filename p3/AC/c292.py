#2025-04-30
#我也不知道自己在寫啥XD會動就好www
import sys
n=int(input())
d=int(input())
m=list(sys.stdin.read().splitlines())
m=[list(i.split()) for i in m]
def solve(n,d,m):
    if d==1 or d==3:
        if d==1:
            d=3
        else:
            d=1
        
    y,x=n//2,n//2
    idx=''
    def move(dt,mv):
        nonlocal x,y,idx
        midx=[dt in (0,2),dt in (1,2)]#mx,my and positive,negetive
        if midx[0]:
            if midx[1]:
                for i in range(mv):
                    idx+=m[y][x]
                    x+=1 
            else:
                for i in range(mv):
                    idx+=m[y][x]
                    x-=1
        else:
            if midx[1]:
                for i in range(mv):
                    idx+=m[y][x]
                    y+=1 
            else:
                for i in range(mv):
                    idx+=m[y][x]
                    y-=1 
    for i in range(1,n):
        for j in range(2):
            move(d%4,i)
            d-=1
    move(d%4,n)
    
    return idx
print(solve(n,d,m))
