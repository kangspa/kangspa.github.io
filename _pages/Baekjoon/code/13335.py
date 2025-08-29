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

'''
if __name__ == '__main__':
    # n = 트럭 수 / w = 다리 길이 / L = 다리 하중
    n, w, L = map(int, input().split())
    a = list(map(int, input().split()))
    answer = 0
    # 현재 다리 위의 무게, 트럭 교체가 일어난 횟수
    now, cnt = 0, 0
    # 다리 위 각 (트럭의 무게, 현재 위치)
    Q = deque()
    for i in a:
        # 현재 트럭이 다리 위에 올라갈 수 있는 상태라면
        if (now+i) <= L:
            # 다리 위 트럭의 위치를 +1 해주고, 현재 트럭을 올려준다.
            for j in range(len(Q)): Q[j][1] += 1
            Q.append([i,0])
            now += i
            # 트럭 올라갈 때마다 시간+1
            answer += 1
        # 현재 트럭이 못 올라가는 상태라면
        else:
            # i 트럭이 올라갈 수 있을 때까지 빼준다.
            while ((now+i) > L):
                t, p = Q.popleft()
                now -= t
                # 트럭이 빠져나오기 까지 걸린 시간=w-p
                k = (w-p)
                answer += k
                # 남은 트럭들 위치도 k만큼 이동시켜준다.
                for j in range(len(Q)): Q[j][1] += k
            # 현재 트럭을 다리에 올려주고, 현재 하중을 더해준다.
            Q.append([i,0])
            now += i
    # 마지막 트럭이 나오는데 걸릴 시간(w)를 더해준다.
    print(answer+w)
'''