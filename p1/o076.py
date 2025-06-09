#2025-06-01
def main():
    n=input()
    buildings=(map(int,input().split()))
    b=0
    c=0
    l=0
    for i in buildings:
        if i<l:
            c+=1
            l=i
            if c>b:
                b=c
        else:
            l=i
            c=1
    print(b)
main()
