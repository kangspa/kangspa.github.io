import sys
input = sys.stdin.readline

from collections import deque

def find_CC(graph, N):
    # 탐색완료한 정점 체크용 배열
    visited = [False]*N
    result = 0 # 찾은 연결 요소 수
    
    for i in range(N):
        # 만약 i가 체크 안된 정점이라면,
        if not visited[i]:
            # bfs 로 탐색하자
            Q = deque()
            # 체크 안된 정점을 Q에 넣고 방문 체크
            Q.append(i)
            visited[i] = True

            while Q:
                node = Q.popleft()
                # 연결되어 있는 정점을 전부 체크
                for v in graph[node]:
                    # 방문 안 한 곳이라면 Q에 추가 후 방문 체크
                    if not visited[v]:
                        Q.append(v)
                        visited[v] = True
            # 일련의 과정이 끝나면 연결 요소 1개 찾은 것
            result += 1
    return result

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    # 만들어지는 그래프를 인접 리스트 형태로 저장
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        # 입력받는 간선을 0 넘버링으로 바꿔준다.
        u, v = map(lambda x: int(x)-1, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 연결 요소 찾는 함수로 값을 찾아준다.
    print(find_CC(graph, N))