#2025-05-29
'''
概念：
1.用上一層每個點的最大搜集點數和當前這一層
  的點數求出當前這一層的每一點最大搜集點數在
  去算下一層直到到底
2.單一點的最大必是：
  1.從正上方下來
  2.從左邊的某點下來再走過來
  3.從右邊的某點下來再走過來
'''
import sys
def main():
    m,n=map(int,input().split())
    inputs=[list(map(int,i.strip("\n").split())) for i in (sys.stdin.readlines())]
    def dp(lastrow,currentrow):
        maxpoint=[]
        down=[a+b for a,b in zip(lastrow,currentrow)]
        maxv=down[0]
        maxpoint.append(maxv)
        for a,b in zip(down[1:],currentrow[1:]):
            maxv=max(a,b+maxv)
            maxpoint.append(maxv)
        leftrow=currentrow[::-1]
        leftdown=down[::-1]
        lmaxv=leftdown[0]
        maxpoint[-1]=max(lmaxv,maxpoint[-1])
        c=1
        for a,b in zip(leftdown[1:],leftrow[1:]):
            c+=1
            lmaxv=max(a,b+lmaxv)
            maxpoint[-c]=max(lmaxv,maxpoint[-c])
        return maxpoint
    lastr=[0 for i in range(n)]
    for i in inputs:
        lastr=dp(lastr,i)
    print(max(lastr))
main()
