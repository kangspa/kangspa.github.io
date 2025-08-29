import sys
input = sys.stdin.readline
import heapq

if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())
    Edges = [[] for _ in range(V+1)]
    # 간선에 대해 입력받고 Edges에 (가중치, 연결 노드) 순으로 저장
    for _ in range(E):
        u, v, w = map(int, input().split())
        Edges[u].append((w, v))
    # K에서 각 정점까지 거리 저장 배열
    answer = [float('inf')] * (V+1)
    answer[K] = 0
    
    # deque 쓰면 시간초과 나옴 > heapq 사용!
    HQ = []
    heapq.heappush(HQ, (0, K))
    while HQ:
        cnt, now = heapq.heappop(HQ)
        # 누적합이 최소 가중치보다 크면 체크 안함
        if answer[now] < cnt: continue
        # 현재 연결된 모든 정점들 체크
        for w, v in Edges[now]:
            new_w = cnt+w
            # 연결된 정점의 최소 가중치가 갱신가능할 때만 이동
            if new_w < answer[v]:
                answer[v] = new_w
                heapq.heappush(HQ, (new_w, v))
    # 정답 출력
    for ans in answer[1:]:
        if ans==float('inf'): print('INF')
        else: print(ans)