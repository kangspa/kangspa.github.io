import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    # 현재 회사에 남아있는 사람
    now = set() # 리스트로 입력받으면 시간 초과됨!
    for _ in range(N):
        name, order = input().rstrip().split()
        # 출퇴근(order)에 따라서 나뉘게 match로 구현
        match order:
            case "enter":
                now.add(name)
            case "leave":
                now.remove(name)
    # 배열을 반환해주도록, sorted를 사용, 역순정렬
    answer = sorted(list(now), reverse=True)
    print(*answer)