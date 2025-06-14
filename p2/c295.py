#2025-06-14
def main():
    n,m=map(int,input().split())
    ans=[]
    for i in range(n):
        l=list(map(int, input().split()))
        ans.append(max(l))
    sum_ans=sum(ans)
    print(sum_ans)
    ans2=[]
    for i in ans:
        if sum_ans%i==0:
            ans2.append(i)
    if ans2:
        print(" ".join(map(str,ans2)))
    else:
        print(-1)
main()
