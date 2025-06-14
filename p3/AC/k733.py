#2025-06-14
#累死人題目
def main():
    m=input()
    def solve(m):
        m=list(m.split('T'))
        m=m[1:]
        total=0
        if "k" in m[0]:
            last_i=int(list(m[0].split("k"))[0])
        else:
            last_i=int(m[0])
        for i in range(len(m)):
            if "k" in m[i]:
                x=list(map(int,m[i].split("k")))
                total+=abs(x[0]-last_i)
                total+=x[1]
                last_i=None
            else:
                if last_i==None:
                    last_i=int(m[i])
                total+=abs(last_i-int(m[i]))
                last_i = int(m[i])
        return total
    def solve_loop(m):
        for i in range(m.count("E")):
            loop=m[m.rindex("L"):]
            loop=loop[:loop.index("E")+1]
            times=int(loop[1])
            fuck=list(loop.split("T"))
            if "k" in fuck[1]:
                f1,_=fuck[1].split("k")
                f1=int(f1)
            else:
                f1=int(fuck[1].strip("E"))
            if "k" in fuck[-1]:
                f2,_=fuck[-1].split("k")
                f2=int(f2)
            else:
                f2=int(fuck[-1].strip("E"))
            diff=abs(f1-f2)
            length=solve(loop[2:-1])
            length=length*times+diff*(times-1)
            m=m.replace(loop,f'T{f1}k{length}T{f2}',1)
        return m
    print(solve(solve_loop(m)))
main()
