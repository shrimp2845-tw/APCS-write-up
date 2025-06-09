#2025-05-07
#dfs,並把底下的總長向上傳遞直到根
import sys
def ans(m):
    total=0
    idx=0
    def gm(m,p):
        nonlocal idx
        if m[idx]==0:
            idx+=1
            return (m,0)
        else:
            n=p-m[idx]
            return (m,n)
    def tree(m,p):
        nonlocal total,idx
        idx+=1
        for i in range((p%2)+2):
            m,n=gm(m,p)
            total+=abs(n)
            if n:
                m=tree(m,m[idx])[0]
        return (m,p)
    tree(m,m[idx])
    return total
def main():
    m=list(map(int,sys.stdin.readline().split()))
    print(ans(m))
main()
