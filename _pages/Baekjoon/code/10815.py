import sys
input = sys.stdin.readline

if __name__ == '__main__':
    # 모두 차례차례 입력 받는다.
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    check = list(map(int, input().split()))
    
    # 정답 넣어둘 dict (배열로는 시간 초과 뜸)
    answer = dict(zip(check, [0]*len(check)))
    
    # cards 를 체크하면서 보유 중이면 1로 바꿈
    for chk in cards:
        # if 문 안 하면 새로운 키 값을 생성해버리니 주의!
        if chk in answer.keys():
            answer[chk] = 1
    
    print(*answer.values())