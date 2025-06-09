#2025-05-28
def main():
    ex={2:0,
        0:5,
        5:2}
    f=int(input())
    n=int(input())
    l=list(map(int,input().split()))
    op=''
    last=None
    c=1
    for i in l:
        op+=(str(f)+' ')
        if not i==f:
            if ex[f]==i:
                print(op+': '+'Lost at round',c)
                return 0
            else:
                print(op+': '+'Won at round',c)
                return 0
        else:
            if last!=i:
                last=i
                f=i
            else:
                f=ex[i]
        c+=1
    print(op+': '+'Drew at round',n)
main()
