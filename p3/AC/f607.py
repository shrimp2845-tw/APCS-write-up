#2025-05-28
#二分搜尋切割點、線段長
import sys
def main():
    n,L=map(int,input().split())
    l=[0,L]
    total=0
    inputs=[list(map(int,i.strip("\n").split())) for i in (sys.stdin.readlines())]
    inputs.sort(key=(lambda l:l[1]))
    def search(t):
        nonlocal l
        d,u=0,len(l)-1
        while u-d>1:
            idx=(u+d)//2
            if t>l[idx]:d=idx
            else:u=idx
        length=l[u]-l[d]
        l.insert(u,t)
        return length
    for i in inputs:
        total+=search(i[0])
    print(total)
main()
