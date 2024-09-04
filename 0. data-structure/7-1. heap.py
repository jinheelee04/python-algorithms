# 7. 힙: 완전 이진 트리의 일종으로, 우선 순위가 높은 원소를 빠르게 접근 가능한 자료구조
# 최소 힙 (Min Heap) : 값이 작은 것이 우선 순위가 높음
from queue import PriorityQueue

# 우선순위 큐 선언
pq = PriorityQueue()

# 원소 삽입
pq.put(40)
pq.put(30)
pq.put(10) # 최소값 우선순위 가장 높음
pq.put(20)

# 우선순위 큐 출력
print("우선순위 큐:", pq.queue)
print(pq.queue)
print()

# 최상위 원소 삭제(우선순위가 가장 높은 원소를 삭제)
removed_element = pq.get()
print("삭제된 원소:", removed_element)
print("삭제 후 우선순위 큐:", pq.queue)
print()

# (삭제하지 않고) 최상위 원소 확인
top_element = pq.queue[0]
print("최상위 원쇠:", top_element)
print("현재 우선순위 큐", pq.queue)
print()

# 우선순위 큐의 크기 확인
print("우선순위 큐의 크기:", len(pq.queue))
print()

# 우선순위 큐가 비어 있는지 확인
print("우선순위 큐가 비어 있는지 확인:", pq.empty())
print()

# 우선순위 큐 그냥 순회(우선순위 보장 안함)
for u in pq.queue:
	print(u, end = ' ')
print()
print()

# 우선순위 큐 순회(우선순위 대로 조회)
while pq.queue: # not pq.empty()
	print(pq.get(), end = ' ')