import heapq

print("pushing 5, 1, 4, 2 onto heapq")
heapQ = []
heapq.heappush(heapQ, 5)
print(heapQ)
heapq.heappush(heapQ, 1)
print(heapQ)
heapq.heappush(heapQ, 4)
print(heapQ)
heapq.heappush(heapQ, 2)
print(heapQ)
num = heapq.heappop(heapQ)
print(f"Num: {num}, heap: {heapQ}")
heapq.heappush(heapQ, 3)
print(heapQ)
