#2025-06-05
'''
不直接拼接字串，而是將字串拆分成a+b+a的形式，
然後檢查集合裡是否有字串b
'''
def main():
    import sys
    n=int(input())
    inputs={i.strip("\n") for i in (sys.stdin.readlines())}
    p=0
    for i in inputs:
        li=len(i)
        for j in range(li-1):
            if i[:j+1]==i[li-1-j:]:
                if i[j+1:li-1-j] in inputs:
                    p+=1
    print(p)
main()
    
