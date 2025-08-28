import sys
input = sys.stdin.readline

from collections import deque

if __name__ == '__main__':
    # 입력받는 부분
    N, R, Q = map(int, input().split())
    # 연결된 간선들 저장
    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        U, V = map(int, input().split())
        edges[U].append(V)
        edges[V].append(U)
    # R을 토대로 각 정점의 부모 노드를 작성해둔다.
    parents = [False]*(N+1)
    parents[R] = True # 루트 노드는 True을 넣어둔다.
    # 각 노드들의 깊이를 저장할 배열
    depth = [False]*(N+1)
    depth[R] = 0 # 루트 노드는 0을 넣어둔다.
    # BFS 형식으로 부모 노드 찾아두기
    queue = deque()
    queue.append(R)
    while queue:
        # 트리의 각 깊이에 해당하는 노드들이 들어오고 체크하게 될 예정
        n = queue.popleft()
        d = depth[n]+1 # n의 자녀노드를 체크할거니까 깊이는 +1
        # 현재 노드와 연결된 정점들 중
        for v in edges[n]:
            # 아직 부모 노드가 연결되지 않은 정점은
            if not parents[v]:
                parents[v] = n # n을 부모노드로 설정해주고,
                queue.append(v) # 다음 탐색을 위해 큐에 넣어준다.
                depth[v] = d # 자녀 노드의 깊이를 작성해준다.
    
    # 각 노드의 서브트리 정점의 수를 저장할 배열
    numSub = [1]*(N+1)
    # 깊이, 부모, 해당정점 넘버를 깊이순으로 탐색하며 numSub에 저장해주자
    # 첫번째 0 인덱스는 제외해주고, sorted 하면 루트노드가 마지막에 오므로 루트노드의 p는 없으니 제외해준다.
    for d,p,i in sorted(tuple(zip(depth, parents, range(N+1)))[1:], reverse=True)[:-1]:
        numSub[p] += numSub[i]
        
    # 쿼리를 입력받을 때마다, 바로바로 연산 후 결과 출력한다.
    for _ in range(Q):
        q = int(input())
        print(numSub[q])