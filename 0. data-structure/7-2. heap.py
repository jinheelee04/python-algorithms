# 7. 힙: 완전 이진 트리의 일종으로, 우선 순위가 높은 원소를 빠르게 접근 가능한 자료구조
# 최대 힙 (Max Heap) : 값이 큰 것이 우선순위가 높음
from queue import PriorityQueue

# 우선순위 큐 선언
pq = PriorityQueue()

# 원소 삽입
#파이썬의 PriorityQueue()에서는 [a, b] 이런 형식으로 원소가 들어가게 되면
#두 원소의 우선순위를 비교할 때 첫 번째 인자 부분(a)를 먼저 비교하게 된다.
pq.put([-40, 40]) # (우선 순위, 값)을 의미
pq.put([-30, 30])
pq.put([-20, 20])
pq.put([-10, 10])

# 우선순위 큐 출력
print("우선순위 큐:", pq.queue)
print(pq.queue)
print()

# 최상위 원소 삭제 (우선순위가 가장 높은 원소를 삭제)
removed_element = pq.get()
print("삭제된 원소:", removed_element)
print("실제 쓸 값:", removed_element[1])
print("삭제 후 우선순위 큐:", pq.queue)

# (삭제하지 않고) 최상위 원소 확인
top_element = pq.queue[0]
print("최상위 원소:",top_element)
print("현재 우선순위 큐:", pq.queue)
print()

# 우선순위 큐의 크기 확인
print("우선 순위 큐의 크기:", len(pq.queue))
print()

# 우선순위 큐가 비어 있는지 확인
print("우선순위 큐가 비어 있는지 확인:", pq.empty())
print()

# 우선순위 큐 그냥 순회(우선순위 보장 안함)
for u in pq.queue:
	print(u[1], end=' ')
print()
print()

# 우선순위 큐 순회(우선순위 대로 순회)
while pq.queue: # not pq.empty()
	print(pq.get()[1], end=' ')