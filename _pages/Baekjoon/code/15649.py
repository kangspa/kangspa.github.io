import sys
input = sys.stdin.readline
# 순열 뽑아주는 라이브러리
from itertools import permutations

if __name__ == '__main__':
    N, M = map(int, input().split())
    # 1부터 N까지 = range(1, N+1) / M개 뽑는다는 permutations
    # 해당 라이브러리 자체가 iter 니까 그대로 for 문에 써줘도 된다.
    for p in permutations(range(1, N+1), M):
        # 여러 원소가 하나씩 출력되도록 앞에 * 하나 붙여준다.
        print(*p)