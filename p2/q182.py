#2025-01-21
al=["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def s0(w):
    nw=''
    for i in range(len(w)//2):
        nw+=w[(i*2)+1]
        nw+=w[i*2]
    return nw
        

def s1(w):
    nw=''
    for i in range(len(w)//2):
        if al.index(w[i*2])>al.index(w[(i*2)+1]):
            nw+=w[(i*2)+1]
            nw+=w[i*2]
        else:
            nw+=w[i*2]
            nw+=w[(i*2)+1]
    return nw
def s2(w):
    w1=''
    w2=''
    nw=''
    for i in range(len(w)):
        if i<len(w)//2:
            w1+=w[i]
        else:
            w2+=w[i]
    for i in range(len(w)//2):
        nw+=w1[i]
        nw+=w2[i]
    return nw
     
       
w=input()
n=int(input())
for i in range(n):
    a=int(input())
    if a==0:
        w=s0(w)
    elif a==1:
        w=s1(w)
    else:
        w=s2(w)
print(w)
