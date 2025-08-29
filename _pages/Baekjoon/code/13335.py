import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    # n = 트럭 수 / w = 다리 길이 / L = 다리 하중
    n, w, L = map(int, input().split())
    truck = deque(map(int, input().split()))
    # 다리 위 각 (트럭의 무게, 현재 위치)
    bridge = deque()
    # 첫번째 트럭은 우선 다리 위에 올려준다.
    t = truck.popleft()
    bridge.append([t, 0])
    # 시간은 1부터 시작, 현재 다리 위의 무게
    answer, now = 1, t
    
    # 남은 트럭이 있거나, 다리 위에 트럭이 있다면,
    while truck or bridge:
        # 일단 시간을 +1 해주고, 현상 확인
        answer += 1
        for i in range(len(bridge)): bridge[i][1] += 1
        # 트럭이 다리 밖으로 나간다면, bridge에서 제거
        if bridge[0][1]==w:
            t, p = bridge.popleft()
            now -= t
        
        # 다음 트럭이 다리 위에 올라갈 수 있는 상태라면
        if truck and ((now+truck[0]) <= L):
            # 다리 위에 트럭 올려준다.
            t = truck.popleft()
            bridge.append([t, 0])
            now += t
    # 최종적으로 걸린 시간 출력
    print(answer)