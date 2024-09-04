# 문제: n번째 피보나치 수를 구하는 문제
# 입력: 10 , 출력: 55
# 제약조건: 0 <= n <= 20


# 내 풀이
n = int(input())

def fibo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1 
	return fibo(n-1) + fibo(n-2)

print("내 풀이 :", fibo(n))
print()

# 문제 풀이
# 1. 반복문을 이용한 피보나치 구하기
# 시간복잡도 O(n) = 20번
# f(n) = f(n-1) + f(n-2)
arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

for i in range(2, n+1):
	arr[i] = arr[i-1] + arr[i-2]

print("1. 반복문을 이용한 피보나치 구하기 :", arr[n])
print()

# 2-1. 재귀함수를 이용한 피보나치 구하기 - 메모이제이션 사용 X 
# 시간복잡도 O(2^n) = 2^20 = (2^10)*(2^10) = 1000 * 1000 = 100
# fibo(x) = fibo(x-1) + fibo(x-2)
def fibo(x):
	global cnt
	cnt += 1

	if x == 0:
		return 0
	if x == 1:
		return 1
	return fibo(x - 1) + fibo(x - 2)
cnt = 0
print("2-1. 재귀함수를 이용한 피보나치 구하기(메모이제이션 사용 X):", fibo(n))
print("cnt=",cnt)
print()

# 2-2. 재귀함수를 이용한 피보나치 구하기 - 메모이제이션 사용 O
# 메모이제이션 기법이란 이미 계산한 값을 저장해 둠으로써 불필요한 중복 계산을 막는 방법이다.
# 시간복잡도 O(n)
def fibo(x):
	global gArr
	global cnt2
	cnt2+=1
	if gArr[x] != -1:
		return gArr[x]

	gArr[x] = fibo(x - 1) + fibo(x - 2)
	return gArr[x]
cnt2 = 0
gArr = [-1] * (n + 2)
gArr[0] = 0
gArr[1] = 1

print("2-2. 재귀함수를 이용한 피보나치 구하기(메모이제이션 사용 O):",fibo(n))
print("cnt2=", cnt2)


