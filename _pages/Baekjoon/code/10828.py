import sys
input = sys.stdin.readline
# 큐나 스택 구현에는 deque가 최고
from collections import deque
        
if __name__ == '__main__':
    N = int(input())
    # 스택 변수를 만들어둔다.
    Stack = deque()
    # 입력받은 N만큼 명령을 처리할 예정
    for _ in range(N):
        # push일 경우 띄어쓰기로 정수 X도 입력받아야하므로, 통일성을 위해 리스트로 입력 받는다.
        order = list(input().rstrip().split())
        # 0번째 원소를 비교
        match order[0]:
            # push 명령일 때, 1번 인덱스(정수 X)를 입력해준다.
            case "push":
                # 따로 연산할 것도 아니라서 정수 변환 별도로 안해줌.
                Stack.append(order[1])
            # pop 명령일 때, try except 구문으로 예외처리 해줌
            case "pop":
                try:
                    print(Stack.pop())
                except:
                    print(-1)
            # size 명령일 때, 그냥 len 씌워줌
            case "size":
                print(len(Stack))
            # empty 명령일 때, 스택 길이가 0이 아니면 0을 출력, 아니면 1 출력
            case "empty":
                if len(Stack): print(0)
                else: print(1)
            # top 명령일 때, pop과 동일하게 try except 구문으로 예외처리 함
            case "top":
                try:
                    print(Stack[-1])
                except:
                    print(-1)