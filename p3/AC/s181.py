#2026-06-12
#dfs enumerate 
import sys
def main():
    n, m, r, k, t = map(int, input().split())
    inp = list(map(int, input().split()))
    cl = [inp[i*r: (i+1)*r] for i in range(m)]
    idx = 0
    def dfs(q, p, depth):
        nonlocal idx, cl, r, k, t 
        for i in range(r):
            if cl[depth][i] in p:
                continue
            np = p.copy()
            np.add(cl[depth][i])
            for j in list(range(i+1, r))+[None]:
                nnp = np.copy()
                if j is not None:
                    if cl[depth][j] in nnp:
                        continue
                    nnp.add(cl[depth][j])
                nq = []
                nq.append((r*depth)+i+1)
                if j is not None:
                    nq.append((r*depth)+j+1)
                nq = q+nq
                if len(nq) == k:
                    idx+=1
                    if idx == t:
                        print(' '.join(map(str, nq)))
                        sys.exit(0)
                if len(nq) >= k:
                    continue
                if depth+1 == len(cl): break
                dfs(nq, nnp, depth+1)
        if depth+1 == len(cl): return
        dfs(q, p, depth+1)
    dfs([], set(), 0)
main()
