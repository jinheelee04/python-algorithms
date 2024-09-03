# 5. 스택: 데이터를 후입선출(LIFO, Last-In-First-Out)의 원칙에 관리하는 선형 자료 구조
from collections import deque

# 스택 선언
st = deque()

# 맨 위(뒤)에 원소 추가
st.append(10)
st.append(20)
st.append(30)

# 스택 출력
print("스택:", st)
print()

# 맨 위(뒤)의 원소 제거
removed_element = st.pop()
print("삭제된 원소:", removed_element)
print("삭제 후 스택:", st)
print()

# 맨 위(뒤)의 원소 확인 
top_element = st[-1]
print("맨 위(뒤)의 원소:", top_element)
print("현재 스택:", st)
print()

# 스택의 크기 확인
print("스택의 크기:", len(st))
print()

# 스택이 비어 있는지 확인
print("스택이 비어있는지 확인", not st)
print()

# 스택 순회
while st:  # 스택이 비어 있지 않으면(원소가 있으면)
	print(st.pop(), end=' ') # 맨위에 원소를 빼면서 출력