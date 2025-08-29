import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        for _ in range(M):
            a, b = map(int, input().split())
        # 그냥 모든 국가를 연결할 수 있는 최소 선의 갯수 (N-1)
        print(N-1)