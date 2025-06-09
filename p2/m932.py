#2025-06-06
def main():
    #x,y
    ex={0:(0,-1),
        1:(1,0),
        2:(1,1),
        3:(0,1),
        4:(-1,0),
        5:(-1,-1)
    }
    m,n,k=map(int,input().split())
    world=[list(input()) for i in range(m)]
    steps=list(map(int,input().split()))
    done=set()
    path=''
    x,y=0,m-1
    for i in steps:
        px=x+ex[i][0]
        py=y+ex[i][1]
        if not px in (-1,n) and not py in (-1,m):
            x,y=px,py
        idx=world[y][x]
        path+=idx
        done.add(idx)
    print(path)
    print(len(done))
main()
