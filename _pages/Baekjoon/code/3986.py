import sys
input = sys.stdin.readline

from collections import deque

def isGoodWord(word):
    Stack = deque()
    for ab in word:
        # 만약 Stack이 비어있으면, 글자 추가해주고 다음으로 넘김
        if not len(Stack):
            Stack.append(ab)
            continue
        # 최근 글자 꺼내주고
        now = Stack.pop()
        # 현재 글자랑 다르면 다시 넣어준다. (순서가 중요!)
        if now!=ab:
            Stack.append(now)
            Stack.append(ab)
    # 모두 체크했는데, Stack에 남아있으면 False
    if len(Stack): return False
    else: return True

if __name__ == '__main__':
    N = int(input())
    answer = 0
    for _ in range(N):
        word = input().rstrip()
        if isGoodWord(word): answer += 1
    print(answer)