import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    # 모든 값을 우선 무한대로 초기화
    answer = [[float('inf')] * (n+1) for _ in range(n+1)]
    # a에서 b로 가는 값을 c로 저장
    for _ in range(m):
        a,b,c = map(int, input().split())
        answer[a][b] = min(answer[a][b], c)
    # 자기자신에게 돌아오는 값은 0으로 초기화
    for i in range(1, n+1): answer[i][i] = 0
    # 시작지점 s에서 경유지 i를 거치고 f까지 가는 거리 계산
    for i in range(1, n+1):
        for s in range(1, n+1):
            for f in range(1, n+1):
                answer[s][f] = min(answer[s][f], answer[s][i]+answer[i][f])
    # 출력
    for ans in answer[1:]:
        for a in ans[1:]:
            if a==float('inf'): print(0, end=' ')
            else: print(a, end=' ')
        print()