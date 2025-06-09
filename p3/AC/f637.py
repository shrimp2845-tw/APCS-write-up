#2025-05-21
#dfs,並用遞迴層數計算格數
def solve(s,n):
    summarise=0
    idx=0
    def sx(layer):
        nonlocal idx,summarise
        for i in range(4):
            if s[idx]=="1":
                summarise+=(n*n)//(4**layer)
                idx+=1
            elif s[idx]=="0":
                idx+=1
            else:
                idx+=1
                sx(layer+1)
    if s[0]=='2':
        idx+=1
        sx(1)
        return summarise
    elif s[0]=='1':
        return n*n
    else:
        return 0
def main():
    s=input()
    n=int(input())
    print(solve(s,n))
main()
