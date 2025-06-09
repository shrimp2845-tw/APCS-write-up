#2024-11-04
n=0
for i in range(2):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(str(sum(a))+':'+str(sum(b)))
    if sum(a)>sum(b):
        n+=1
    elif sum(a)<sum(b):
        n-=1
if n>0:
    print('Win')
elif n==0:
    print('Tie')
else:
    print('Lose')
