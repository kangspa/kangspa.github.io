import sys
input = sys.stdin.readline

# 일단 우선순위 큐로 구현
import heapq

if __name__ == '__main__':
    N = int(input())
    
    # 우선순위 큐로 쓰기 위한 리스트
    heap = []
    # N 번 반복하기 위해 for문으로 구현
    for _ in range(N):
        # N 번 입력받는다.
        x = int(input())
        # 0 이 아니라면 우선순위 큐 에 원소를 넣는 연산
        if x!=0:
            # 절댓값 기준 정렬이 되면서 출력값은 입력값이어야해서 튜플 통해서 입력
            # 공식문서 참고 시, heapq에는 튜플이 가능하며, 0 인덱스 값 기준으로 정렬됨을 알 수 있다.
            heapq.heappush(heap, (abs(x), x))
        else:
            # 만약 입력값이 0이라면,
            try:
                # heapq 에서 가장 절댓값이 작은 값을 뽑아내고, 튜플형태이기에 1 인덱스의 원본 값을 print 한다.
                print(heapq.heappop(heap)[1])
            # heapq 에 원소가 없다면 에러가 발생 (out of index)
            except:
                print(0)