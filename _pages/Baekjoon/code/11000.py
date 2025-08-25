import sys
input = sys.stdin.readline

# 해당 문제는 힙큐를 무조건 사용해야 한다.
import heapq

if __name__ == '__main__':
    # N과 S, T 를 입력받는다.
    N = int(input())
    ST = [list(map(int, input().split())) for _ in range(N)]
    
    # 우선 시작 시간 기준으로 정렬해준다.
    ST.sort()
    
    # 정답이 될 강의실 수
    answer = 1
    # 강의실 배정을 heap에 해주고,
    heap = []
    # 초기화를 위해 -1만 넣어준다.
    heapq.heappush(heap, -1)
    
    for st in ST:
        # 현재 강의실 중 가장 일찍 끝나는 곳
        m = heapq.heappop(heap)
        # 해당 강의실이 현재 사용가능하면,
        if st[0] >= m:
            # 해당 강의실은 현재 강의의 끝나는 시간을 기록
            heapq.heappush(heap, st[1])
        # 현재 사용 불가라면
        else:
            # 가장 일찍 끝나는 강의실도 heap 에 다시 넣어주고
            heapq.heappush(heap, m)
            # 강의실 하나 더 추가해준다.
            answer += 1
            heapq.heappush(heap, st[1])
    
    print(answer)