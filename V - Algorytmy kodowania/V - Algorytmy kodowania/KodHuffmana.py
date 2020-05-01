import heapq
from collections import defaultdict


def code(frequency):
    stack = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(stack)
    while len(stack) > 1:
        low = heapq.heappop(stack)
        high = heapq.heappop(stack)
        for pair in low[1:]:
            pair[1] = "0" + pair[1]
        for pair in high[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(stack, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heapq.heappop(stack)[1:], key=lambda p: (len(p[-1]), p))


data = "exam ple lsa dfds aewr"
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1


huff = code(frequency)
print("Symbol".ljust(10) + "Weig".ljust(10) + "Huffman Kod")
for p in huff:
    print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])

