import sys
input = sys.stdin.readline

from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    # 9876543210 배열에서 나올 수 있는 자릿수는 1~10자리임
    for n in range(1, 11):
        # join 함수로 모든 경우의 수를 튜플에서 문자열로 바꿔주고, 작은 수부터 차례로 커지도록 정렬한다.
        lst = sorted(list(map(''.join, combinations('9876543210', n))))
        # 아직 N번째가 안됐으면, 체크한 감소하는 수 갯수만큼 N의 값을 줄여준다.
        if N >= len(lst): N -= len(lst)
        # 현재 리스트 안에 N번째 감소하는 수가 있으면,
        else:
            # 출력해주고, for 문 밖의 조건문에 안 걸리도록 빼준다.
            print(lst[N])
            N -= len(lst)
            break
    # 만약 for문 다 돌았는데 N이 0보다 크거나 같다면, -1을 출력 (감소하는 수가 없음)
    if N >= 0: print(-1)