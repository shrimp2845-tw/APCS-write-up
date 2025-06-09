#2025-06-03
'''
將樹的結構改成無向圖，從任一點
找最遠點，再從這個點找最遠點得
到的距離及是答案（使用bfs找最遠距離）
'''
def main():
    import sys
    class Tree:
        def __init__(self):
            self.partner={}
        def add_partner(self,a,b):
            self.partner.setdefault(a,set())
            self.partner.setdefault(b,set())
            self.partner[a].add(b)
            self.partner[b].add(a)
        def find_furthest(self,node):
            roots=[(node,None)]
            length=0
            while 1:
                croots=[]
                for a,b in roots:
                    for i in self.partner[a]:
                        if i!=b:
                            croots.append((i,a))
                if len(croots)==0:
                    return roots[0][0],length
                else:
                    length+=1
                    roots=croots[:]
    n=int(input())
    data=(i.strip('\n').split() for i in (sys.stdin.readlines()))
    mytree=Tree()
    for a,b in data:
        mytree.add_partner(int(a),int(b))
    n1,l1=mytree.find_furthest(0)
    n2,l2=mytree.find_furthest(n1)
    print(l2)
main()
