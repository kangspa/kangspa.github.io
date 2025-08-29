import sys
input = sys.stdin.readline

def findInList(a, A, N):
    # 가장 작은 값, 가장 큰 값
    s, b = 0, N-1
    # 이분 탐색 알고리즘
    while s <= b:
        n = (s+b)//2
        # a를 찾으면 1 반환
        if A[n]==a: return 1
        # 현재 값이 a보다 크면, 큰 값을 현재 값의 -1
        elif A[n] > a: b = n-1
        # 현재 값이 a보다 작으면, 작은 값을 현재 값의 +1
        elif A[n] < a: s = n+1
    # 못 찾으면 0 반환
    return 0

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    a = list(map(int, input().split()))
    # 이진 탐색을 위해 A를 sort
    A.sort()
    # a 안의 각 값에 대해 이진 탐색 후 출력
    for i in a:
        print(findInList(i, A, N))

'''
if __name__ == '__main__':
    N = int(input())
    NA = list(map(int, input().split()))
    M = int(input())
    MA = list(map(int, input().split()))
    # 해시를 이용하기 위해 dict 형태로 변환
    A = {v:1 for v in NA}
    # try except 구문을 활용해 간단히 풀이
    for a in MA:
        try:
            if A[a]: print(1)
        except: print(0)
'''