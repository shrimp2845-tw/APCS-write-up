#2025-06-01
#95%,maximum recursion depth exceeded
#改bfs或手動stack代替遞迴
def main():
    import sys
    class Tree:
        def __init__(self):
            self.parent={}
            self.children={}
            self.total_height={}
        def add_parent(self,child,p):
            self.parent[child]=p
            self.children.setdefault(p,[])
            self.children[p].append(child)
        def find_root(self,idx):
            self.parent.setdefault(idx,idx)
            if self.parent[idx]==idx:
                return idx
            else:
                return self.find_root(self.parent[idx])
        def h(self,node):
            if not self.children.get(node):
                return 0
            else:
                mh=0
                for i in self.children[node]:
                    hi=self.h(i)
                    self.total_height[i]=hi
                    mh=max(mh,hi+1)
                self.total_height[node]=mh
                return mh
    n=int(input())
    nodes=(list(map(int,i.strip("\n").split())) for i in (sys.stdin.readlines()))
    c=1
    mytree=Tree()
    for i in nodes:
        for j in i[1:]:
            mytree.add_parent(j,c)
        c+=1
    root=mytree.find_root(1)
    print(root)
    mytree.h(root)
    print(sum(mytree.total_height.values()))
main()
