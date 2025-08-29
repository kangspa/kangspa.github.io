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

'''
min, index 이용해서 가장 일찍 끝나는 강의실 기준 체크
if __name__ == '__main__':
    # N과 S, T 를 입력받는다.
    N = int(input())
    ST = [list(map(int, input().split())) for _ in range(N)]
    
    # 강의실 넣어줄 answer 배열
    answer = [-1]
    
    # 모든 강의를 체크 시작 (Si 기준으로 정렬 돼있다 가정)
    for st in ST:
        # 현재 사용 강의실 중 가장 빨리 끝나는 곳 시간
        m = min(answer)
        # 해당 강의실이 현재 사용가능하면,
        if st[0] >= m:
            # 해당 강의실은 현재 강의의 끝나는 시간을 기록
            answer[answer.index(m)] = st[1]
        # 현재 사용 불가라면
        else:
            # 새로운 강의실을 할당
            answer.append(st[1])
    
    # 모든 강의 체크가 끝났다면, 사용한 강의실 수를 출력
    print(len(answer))
'''
'''
# dict 이용해서 강의실 하나하나 체크하는 방법
if __name__ == '__main__':
    # N과 S, T 를 입력받는다.
    N = int(input())
    ST = [list(map(int, input().split())) for _ in range(N)]
    
    # 강의실 넣어줄 answer dict
    answer = {0:-1}
    
    # 모든 강의를 체크 시작 (Si 기준으로 정렬 돼있다 가정)
    for st in ST:
        # False 면 현재 빈 강의실이 없다!
        chk = False
        # answer의 강의실 중 비는 강의실이 있는지 체크
        for i in range(len(answer)):
            # 현재 강의 시작 시 비는 강의실 이 있다면,
            if st[0] >= answer[i]:
                # 해당 강의의 끝나는 시간을 강의실에 기록하고
                answer[i] = st[1]
                # 빈 강의실 있다고 체크해주자
                chk = True
                break
        # 만약 빈 강의실이 없다면, 새로운 강의실 넣기
        if not chk: answer[i+1] = st[1]
    
    # 모든 강의 체크가 끝났다면, 사용한 강의실 수를 출력
    print(len(answer))
'''