#2025-06-19
#就是模擬
def main():
    m, n, k = map(int, input().split())
    wheels = [list(input()) for i in range(m)]
    points = 0
    for _ in range(k):
        steps = list(map(int, input().split()))
        new_wheels = []
        for i, wheel in zip(steps, wheels):
            i %= n
            wheel = wheel[-i:] + wheel[:-i] 
            new_wheels.append(wheel)
        wheels = new_wheels
        for alpha in zip(*wheels):
            points += max((alpha.count(j) for j in set(alpha)))
    print(points)
main()
