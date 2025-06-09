#2025-05-27
'''
80%TLE
主要問題在每一個新的探員都要重製一次DSU，
copy一個長度m的字典
解決方法：因為探員最多只有二十對pairs，
記錄下更改的parent並回朔會快很多
'''
def main():
    class DSU:
        def __init__(self):
            self.parent = {}
        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
            elif self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, x, y):
            self.parent[self.find(y)] = self.find(x)
        def copy(self):
            new_dsu = DSU()
            new_dsu.parent = self.parent.copy()
            return new_dsu
    def makedsu(pairs):
        dsu=DSU()
        for a,b in pairs:
            dsu.union(a+1,-b-1)
            dsu.union(b+1,-a-1)
        return dsu
    n,m=map(int,input().split())
    pairs=list(map(int,input().split()))
    pairs=([a,b] for a,b in zip(pairs[::2],pairs[1::2]))
    ds=makedsu(pairs)
    p,k=map(int,input().split())
    for i in range(p):
        dsu=ds.copy()
        pairs=list(map(int, input().split()))
        pairs=([a,b] for a,b in zip(pairs[::2],pairs[1::2]))
        for a,b in pairs:
            if dsu.find(a+1)==dsu.find(b+1):
                print(i+1)
                break
            else:
                dsu.union(a+1,-b-1)
                dsu.union(b+1,-a-1)


main()
