import sys
input = sys.stdin.readline

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    # pow 함수가 분할정복을 통한 거듭제곱 함수이다.
    # 제곱하고자하는 값, 거듭제곱 횟수, 모듈러 연산할 값
    print(pow(A, B, C))
    '''
    # 글 참고하고 진행해보았으나, 파이썬 연산자체가 느린지 아래 방식으로 통과 안됨
    # 분할정복 관련 글 : https://deepdata.tistory.com/369
    answer = 1
    while B:
        if B&1: answer *= A
        A *= A
        B >> 1
        if answer > 2147483647: answer %= C
    print(answer)
    '''