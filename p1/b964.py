#2025-05-01
n=int(input())
l=list(map(int,input().split()))
bc=100
wc=-100
for i in l:
    p=i-60
    if i>=60:
        if p<bc:
            bc=p
    else:
        if p>wc:
            wc=p
l.sort()
print(' '.join(list(map(str,l))))
if wc>=-60:
    print(60+wc)
else:
    print('best case')
if bc<=40:
    print(60+bc)
else:
    print('worst case')
