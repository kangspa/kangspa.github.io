import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    answer = 0
    # 큰 동전부터 확인
    for i in range(N-1, -1, -1):
        if K >= A[i]:
            answer += (K//A[i])
            K %= A[i]
            if K==0: break
    print(answer)