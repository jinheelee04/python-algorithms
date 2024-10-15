# BOJ 4779
# 칸토어 집합
# 문제: 칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 
# 구간 [0,1]에서 시작해서 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.
# 전체 집합이 유한이라고 가정하고, 다음과 같은 과정을 통해서 칸토어 집합의 근사를 만들어보자
# 1. -가 3^n개 있는 문자열에서 시작한다.
# 2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.
# 3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다.
# 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.
#
# 입력: 입력을 여러줄로 이루어져 있다. 각 줄에 N이 주어진다. 파일의 끝에서 입력을 멈춘다.
# 제약조건: 0 <= N <= 12 
# ex) 
# 0
# 1
# 3
# 2
# 출력: 입력으로 주어진 N에 대해서, 해당 칸토어 집합의 근사를 출력한다.
# ex)
# -
# - -
# - -   - -         - -   - -
# - -   - -

# 문제 풀이
# 1. bottom-up 방식
# 시간복잡도: O(3^N)
# 
# f(n) = f(n-1) + 공백이 3^(N-1) + f(n-1)
# ans[i]: 입력이 2일 때의 답(문자열)
# ans[i]: ans[i-1] + 공백이 3^(i-1) + ans[i-1]
ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1,13):
	ans[i] = ans[i-1] + (' ' *(3**(i-1))) + ans[i-1]

while True:
	try:
		N = int(input())
		print(ans[N])
	except:
		break


# 2. 재귀함수 이용
# def func(k):
# 	# base case
# 	if k == 0:
# 		print('-', end="")
# 		return
# 	#recursive case
# 	func(k-1)
# 	print(' ' * (3**(k-1)), end="")
# 	func(k-1)

# while True:
# 	try:
# 		N = int(input())
# 		func(N)
# 		print()
# 	except:
# 		break

# 입력이 k일 때 답을 (문자열로) 반환하는 함수 
def func(k):
	# base case
	if k == 0:
		return '-'
	# recursive case
	return func(k-1) + (' '*(3**(k-1))) + func(k-1)
while True:
	try:
		N = int(input())
		print(func(N))
	except:
		break