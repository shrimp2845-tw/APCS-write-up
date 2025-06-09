#2025-05-28
#差分陣列紀錄權重，貪心法填入機器
import sys,itertools
def main():
    n,m=map(int,input().split())
    inputs=[list(map(int,i.strip('\n').split())) for i in (sys.stdin.readlines())]
    machine=inputs.pop()
    machine.sort()
    darray=[0 for i in range(n+1)]
    for i in inputs:
        l,r,w=i
        darray[l-1]+=w
        darray[r]-=w
    posinfo=list(itertools.accumulate(darray))
    posinfo.pop()
    posinfo.sort(reverse=True)
    totalt=0
    for a,b in zip(machine,posinfo):
        if b!=0:
            totalt+=a*b
        else:
            break
    print(totalt)
main()
