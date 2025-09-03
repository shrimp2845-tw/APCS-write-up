#2025-09-03
'''
不知道為什麼用heap一起傳遞路徑長度算出來
的路徑長度會有偏差，所以乾脆用最小高度差
再bfs一次算長度，比binary search+bfs
快四倍左右
'''
import heapq
import math


def main():
    n = int(input())
    world = [list(map(int, input().split())) for i in range(n)]
    move = ((0, 1), (1, 0), (-1, 0), (0, -1))
    weight = [[math.inf for j in range(n)] for i in range(n)]
    weight[0][0] = 0
    # max_step, y, x
    heap = [(0, 0, 0)]
    ans1 = None
    while heap:
        max_step, y, x = heapq.heappop(heap)
        if max_step > weight[y][x]:
            continue
        if y == n-1 and x == n-1:
            ans1 = max_step
            break
        ch = world[y][x]
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and max(max_step, abs(world[ny][nx] - ch)) < weight[ny][nx]:
                heapq.heappush(heap, (max(max_step, abs(world[ny][nx] - ch)), ny, nx,))
                weight[ny][nx] = max(max_step, abs(world[ny][nx] - ch))
    print(ans1)
    visited=[[0 for i in range(n)] for i in range(n)]
    visited[0][0] = 1
    queue = [(0, 0)]
    length = 0
    while queue:
        nq = []
        for y, x in queue:
            if y==n-1 and x==n-1:
                print(length)
                return
            for dy, dx in move:
                ny, nx = y+dy, x+dx
                if not (0<=ny<n and 0<=nx<n and visited[ny][nx]==0):
                    continue
                if abs(world[ny][nx]-world[y][x]) <= ans1:
                    nq.append((ny, nx))
                    visited[ny][nx] = 1
        length += 1
        queue = nq
main()
