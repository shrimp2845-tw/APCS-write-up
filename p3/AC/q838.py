#2025-06-16
import heapq
class simple_dll:
    def __init__(self,n):
        self.left=[-1]*n
        self.right=[-1]*n
        self.alive=[True]*n
        for i in range(n):
            if i>0:
                self.left[i]=i-1
            else:
                self.left[i]=-1
            if i<n-1:
                self.right[i]=i+1
            else:
                self.right[i]=-1
    def delete(self,i):
        if not self.alive[i]:
            return
        l,r=self.left[i], self.right[i]
        if r!=-1:
            self.left[r]=l
        if l!=-1:
            self.right[l]=r
        self.alive[i]=False

    def r(self,i):
        if self.alive[i]:
            return self.right[i]
        return -1

def main():
    n,t = map(int,input().split())
    game_map = list(map(int, input().split()))
    heap=[(game_map[i],i) for i in range(n)]
    heapq.heapify(heap)
    connection=simple_dll(n)
    total = 0
    while heap:
        amount,idx=heapq.heappop(heap)
        if not connection.alive[idx] or game_map[idx]!=amount:
            continue
        if amount > t:
            break
        right=connection.r(idx)
        total+=amount
        connection.delete(idx)
        if right!=-1 and connection.alive[right]:
            game_map[right]+=amount
            heapq.heappush(heap,(game_map[right],right))
    print(total)
main()
