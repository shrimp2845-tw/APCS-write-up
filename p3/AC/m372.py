#2025-9-2
'''
bfs,格子加入queue時就把那格水管抹掉
並且每次while queue都把queue長度加
到ans(是應該一個一個加，但我懶得改了）
然後遍歷整張地圖找到水管就bfs更新最大
長度
'''
import sys
def main():
    n, m = map(int, input().split())
    tubes = {
        'I': ((1, 0), (-1, 0)),
        'H': ((0, 1), (0, -1)),
        'X': ((1, 0), (-1, 0), (0, 1), (0, -1)),
        'L': ((0, 1), (-1, 0)),
        'J': ((0, -1), (-1, 0)),
        '7': ((1, 0), (0, -1)),
        'F': ((0, 1), (1, 0))}
    world = [list(i) for i in sys.stdin.read().splitlines()]
    def bfs(y, x):
        nonlocal  world, n, m
        length = 0
        queue = [(y, x, world[y][x])]
        world[y][x] = '0'
        while queue:
            nq = []
            length += len(queue)
            for qy, qx, tube in queue:
                inp = tubes[tube]
                for dy, dx in inp:
                    ny, nx = qy+dy, qx+dx
                    if not (0 <= ny < n and 0 <= nx < m):
                        continue
                    if world[ny][nx] == '0':
                        continue
                    out = tubes[world[ny][nx]]
                    if (-dy, -dx) in out:
                        nq.append((ny, nx, world[ny][nx]))
                        world[ny][nx] = '0'
            queue = nq
        return length
        
    ans = 0
    for y in range(n):
        for x in range(m):
            idx = world[y][x]
            if idx != '0':
                ans = max(bfs(y, x), ans)
    print(ans)
main()
