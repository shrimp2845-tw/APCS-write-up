#2024-11-07
w=0#way point 
p=0#point
ems=0#ems
chart=[]
m,n,k,r,c=map(int,input().split())
for i in range(m):
    chart.append(list(map(int,input().split())))
while chart[r][c]!=0:
    p+=chart[r][c]
    chart[r][c]-=1
    ems+=1
    if p%k==0:
        w+=1
    
    while True:#infinite loop bug!!
        if w%4==0:#right
            if c+1<n:#limit
                if chart[r][c+1]!=-1:#wall
                    c+=1
                    break
            w+=1
        elif w%4==1:#down
            if r+1<m:
                if chart[r+1][c]!=-1:
                    r+=1
                    break
            w+=1
        elif w%4==2:#left
            if chart[r][c-1]!=-1 and c-1>-1:
                c-=1
                break
            w+=1    
        elif w%4==3:#up
            if chart[r-1][c]!=-1 and r-1>-1:
                r-=1
                break
            w+=1
print(ems)
