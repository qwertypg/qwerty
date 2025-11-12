import heapq

chars=['a','b','c','d','e','f']
freq=[5,9,12,13,16,45]

heap=[[f,[ch,""]] for ch , f in zip(chars,freq)]
heapq.heapify(heap)

while len(heap)>1:
    low1=heapq.heappop(heap)
    low2=heapq.heappop(heap)

    for pair in low1[1:]: pair[1]="0" + pair[1]

    for pair in low2[1:]: pair[1]="1" + pair[1]

    heapq.heappush(heap, [low1[0]+low2[0]]+low1[1:]+low2[1:])

for ch,code in sorted(heap[0][1:], key=lambda x: x[0]):
    print(ch,"->",code)