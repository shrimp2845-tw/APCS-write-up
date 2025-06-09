#2025-04-25
#90%TLE,時間複雜度O(n^l*m),簡直災難
#可能要整個打掉重練QAQ
def check(a,l,b):
    idxs=[0 for i in range(l)]
    def s(layer):
        nonlocal idxs
        if layer+1!=l:
            for i in a:
                idxs[layer]=i
                layer+=1
                ifs=s(layer)
                if ifs:
                    return ifs
                layer-=1
            return 0
        else:
            for i in a:
                idxs[-1]=i
                if not ''.join(idxs) in b:
                    return  ''.join(idxs)
            return 0    
    print(s(0))  
def main():
    a=list(set(input()))
    a.sort()
    l=int(input())
    b=input()
    check(a,l,b)
main()
