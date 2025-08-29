# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

q = int(input())
h = []
d = set()

for _ in range(q):
    x = input().split()
    if x[0] == '1':
        v = int(x[1])
        heapq.heappush(h, v)
        d.add(v)
    elif x[0] == '2':
        v = int(x[1])
        d.remove(v)
    else:
        while h[0] not in d:
            heapq.heappop(h)
        print(h[0])