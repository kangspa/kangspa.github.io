import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    SN = []
    # 1번조건(길이)과 2번조건(숫자합)을 한번에 연산하기 위해 따로 입력받음
    for _ in range(N):
        sn = input().strip()
        # 시리얼번호 중 숫자는 전부 더해서 s에 저장한다.
        s = sum(int(c) for c in sn if c.isdigit())
        # 길이, 숫자합, 시리얼번호 순으로 SN에 저장.
        SN.append((len(sn), s, sn))
    # 그냥 sort 해주면 첫번째 인덱스부터 차례대로 비교해준다.
    SN.sort()
    # 출력은 마지막 원소인 시리얼번호만 해준다.
    for sn in SN: print(sn[2])