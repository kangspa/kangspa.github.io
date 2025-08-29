import sys
input = sys.stdin.readline
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, input().split())
    house = []
    chicken = []
    for y in range(N):
        lst = list(map(int, input().split()))
        for x in range(N):
            if lst[x] == 1:
                house.append((y,x))
            elif lst[x] == 2:
                chicken.append((y,x))
    # [i][j] : i=chicken수 / j=house수
    c, h = len(chicken), len(house)
    chDir = [[0]*h for _ in range(c)]
    # 각 집과 치킨집 간의 "치킨 거리" 계산
    for i in range(c):
        for j in range(h):
            chDir[i][j] = abs(chicken[i][0]-house[j][0]) + abs(chicken[i][1]-house[j][1])
    # 최종 정답 변수
    answer = float('inf')
    # M개만큼 선택하는 치킨집 위치 사수
    for combi in combinations(range(c), M):
        # 현재 조합에서 최소가 되는 치킨 거리 저장
        ans = 0
        # 현재 집 위치 선택
        for k in range(h):
            # 현재 집에서 치킨집까지 위치 중 가장 짧은 거리
            now = float('inf')
            for chk in combi:
                now = min(now, chDir[chk][k])
            ans += now
        answer = min(answer, ans)
    print(answer)