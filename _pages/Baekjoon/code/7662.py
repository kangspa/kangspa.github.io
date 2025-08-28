import sys
input = sys.stdin.readline

import heapq

if __name__ == '__main__':
    T = int(input())
    # 각 테스트 케이스마다 따로 입력 받기
    for _ in range(T):
        # 연산 갯수 먼저 입력받고
        k = int(input())
        # 최대값 우선순위 큐, 최소값 우선순위 큐를 각각 만든다.
        maxQ, minQ = [], []
        # 우선순위 큐 한쪽에서만 제거되면 다른 쪽에서는 모르는만큼,
        # 현재 큐 내에 특정값이 몇개 있는지 체크해줄 딕셔너리를 선언
        chkQ = dict()
        # 연산 입력 시작
        for _ in range(k):
            # 입력받아주고나서, n은 정수형 변환해줌
            op, n = input().strip().split()
            n = int(n)
            # I 연산이라면,
            if op=='I':
                # 최대값 우선순위 큐는 역순정렬되어야 하므로,
                # -를 곱해서 튜플형태로 바꿔주고, 1인덱스에 원본값 보존
                heapq.heappush(maxQ, (-n, n))
                # 최소값 우선순위 큐에는 그냥 넣어주면 된다.
                heapq.heappush(minQ, n)
                # 딕셔너리에 해당 정수값 +1 해주는데, 없다면 새로 만들어준다.
                try: chkQ[n] += 1
                except: chkQ[n] = 1
            else:
                # D 연산일 때, 만약 heappop이 안되면 그냥 pass 해준다.
                try:
                    # 최대값을 제거해야한다면,
                    if n==1:
                        # 튜플로 뽑히니깐 1인덱스 값이 구하는 값이다!
                        c = heapq.heappop(maxQ)[1]
                        # 만약 뽑은 값이 이미 없는 값이라면,
                        if not chkQ[c]:
                            # 있는 값이 될 때까지 뽑고,
                            while True:
                                c = heapq.heappop(maxQ)[1]
                                # 만약 큐 안에 존재하는 값이면, -1하고 반복문 탈출
                                if chkQ[c]:
                                    chkQ[c] -= 1
                                    break
                        # 이미 있는 값이면 그냥 -1 해주면 된다.
                        else: chkQ[c] -= 1
                    # 최소값 제거는 평범하게 제거하고 체크해주면 된다.
                    else:
                        c = heapq.heappop(minQ)
                        if not chkQ[c]:
                            while True:
                                c = heapq.heappop(minQ)
                                if chkQ[c]:
                                    chkQ[c] -= 1
                                    break
                        else: chkQ[c] -= 1
                except: pass
        # 모든 연산이 끝났는데, chkQ의 값(모든 정수값)이 전부 0이라 큐에 값이 없다면 EMPTY
        if all(v==0 for v in chkQ.values()): print('EMPTY')
        else:
            # 아니면 M, m 에 큐 안의 최대 최소값을 넣어주고, 출력해준다.
            while True:
                M = heapq.heappop(maxQ)[1]
                if chkQ[M]: break
            while True:
                m = heapq.heappop(minQ)
                if chkQ[m]: break
            print(M, m)