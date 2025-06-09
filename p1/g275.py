#2024-11-01(曾經兩年沒寫code之後寫出來的詭異東東www
def a(a,b):
    if a[2]!=a[6] and a[2]==a[10] and b[2]!=b[6] and b[2]==b[10]:
        return 1
    return 0
def b(a,b):
    if a[12]=='1' and b[12]=='0':
        return 1
    return 0
def c(a,b):
    if a[2]!=b[2] and a[6]!=b[6] and a[10]!=b[10]:
        return 1
    return 0
n=int(input())
for i in range(n):
    x=0
    u=input()
    d=input()
    if a(u,d)==0:
        print("A",end="")
        x+=1
    if b(u,d)==0:
        print("B",end="")
        x+=1
    if c(u,d)==0:
        print("C",end="")
        x+=1
    if x!= 0:
        print("")
    if x==0:
        print("None")
