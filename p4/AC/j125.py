#2025/6/12
'''
bfs檢查一個最小最大值有沒有可能大於target
二分搜尋最大側資範圍（0~1000000）
O(n²×log(max_diff))
(好欸開心
'''
import sys
import collections
def main():
    n=int(input())
    inputs=[list(map(int,i.strip('\n').split())) for i in (sys.stdin.readlines())]
    move=((1,0),(-1,0),(0,1),(0,-1))
    lower,upper=0,1000000
    def check(target):
        nonlocal inputs,n,move
        visited=[[0 for i in range(n)] for i in range(n)]
        visited[0][0]=1
        dp=collections.deque([(0,0,0)])
        while dp:
            y,x,s=dp.popleft()
            if y==n-1 and x==n-1:
                return s
            p1=inputs[y][x]
            for a,b in move:
                if 0<=y+a<n and 0<=x+b<n and visited[y+a][x+b]==0 and abs(inputs[y+a][x+b]-p1)<=target:
                    dp.append((y+a,x+b,s+1))
                    visited[y+a][x+b]=1
        return False
    while upper-lower>1:
        idx=(upper+lower)//2
        if check(idx):
            upper=idx
        else:
            lower=idx
    print(upper)
    print(check(upper))
main()
