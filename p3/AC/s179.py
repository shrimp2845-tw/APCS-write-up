#2026-06-12
#其實這題就是fancy一點的二分搜，應該算送分？

from itertools import accumulate

def get_sec(ll, l, r):
    if l > r:
        return 0
    return ll[r]-ll[l-1]

def main():
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    il = [map(int, input().split()) for i in range(m)]
    nl = [0] + list(accumulate(nl))
    for l, r, a, b in il:
        t = a/(a+b)
        u, d = r, l-1
        while u-d > 1:
            idx = (u+d)//2
            nt = get_sec(nl, l, idx) / get_sec(nl, l, r)
            if nt >= t:
                u = idx
            elif nt < t:
                d = idx
        print(u)
main()
