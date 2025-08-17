# 순열
from itertools import permutations
# 조합
from itertools import combinations
# list 내 같은 원소의 수 반환하는 함수
from collections import Counter

N = int(input())

A = input().split()
for i in range(N):
    A[i] = int(A[i])

sum, min, mul, dev = map(int, input().split())

# 갯수로 입력받은 연산자를 배열 안에 하나씩 넣어준다.
arr = []
for i in range(sum):
    arr.append('+')
for i in range(min):
    arr.append('-')
for i in range(mul):
    arr.append('*')
for i in range(dev):
    arr.append('/')

# 연산자 순열을 중복없게 모든 경우의 수를 구한다.
arr = list(set(permutations(arr)))

# 연산해주는 함수를 별도로 만든다.
def cal(op, x, y):
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y

# 최대 최소값 저장할 변수
M = -1000000000
m = 1000000000

# 모든 경우의 수를 돌면서 연산시작
for op in arr:
    S = A[0]
    for i in range(1, len(A)):
        S = int(cal(op[i-1], S, A[i]))
    # 최대값 최소값 배정
    if (S > M):
        M = S
    if (S < m):
        m = S

# 출력
print(M)
print(m)
