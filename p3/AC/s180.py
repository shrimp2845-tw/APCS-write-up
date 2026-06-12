#2026-06-12
#differance array + prefix sum + index compress

def main():
    ml = {}
    n, m = map(int, input().split())
    tl = list(map(int, input().split()))
    dl = [map(int, input().split()) for i in range(m)]
    sp = set()
    for i, j in dl:
        if not ml.get(i): ml[i]=0
        if not ml.get(j+1): ml[j+1]=0
        ml[i]+=1
        ml[j+1]-=1
        sp.add(i)
        sp.add(j+1)
    sp.add(0)    
    ml[0] = 0
    sl = sorted(list(sp))
    c = 0
    for i in sl:
        ml[i]+=c
        c = ml[i]
    total = 0
    for i in tl:
        u, d = len(sl), 0
        ans = None
        while u-d > 1:     
            idx = (u+d)//2
            if sl[idx]>i:
                u = idx
            elif sl[idx]<i:
                d = idx
            else:
                ans = idx
                break
        if ans is None:
            total+=ml[sl[d]]
            continue
        total+=ml[sl[ans]]
    print(total)
main()
