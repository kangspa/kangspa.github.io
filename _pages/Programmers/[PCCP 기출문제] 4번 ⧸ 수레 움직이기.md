---
title: "[PCCP 기출문제] 4번 ⧸ 수레 움직이기"
tags:
    - C
    - C++
    - Java
    - JavaScript
    - Python3
date: "2025-08-17"
---

출처 : [[PCCP 기출문제] 4번 ⧸ 수레 움직이기](https://school.programmers.co.kr/learn/courses/30/lessons/250134)
<details>
<summary><b>Solution</b></summary>

<details>
<summary>Python</summary>

<pre><code class='language-python'>
from collections import deque

def check_move(n, m, y, x, log, maze):
    # maze 범위 벗어나는지 체크
    if not ((0 <= y < n) & (0 <= x < m)):
        return False
    # 이미 지나온 위치인지 체크
    if log[y][x]:
        return False
    # 진행 방향에 벽이 있는지 체크
    if (maze[y][x] == 5):
        return False
    # 모든 경우 다 되면 True
    return True

def move(n, m, y, x, log, maze):
    # 수레가 갈 수 있는 방향 / 상하좌우
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    # 이동 가능한 좌표 값은 리스트에 저장
    result = []
    # 4방향으로 수레를 이동시킬 수 있는지 체크
    for i in range(4):
        dy, dx = direction[i][0], direction[i][1]
        # check_move 함수를 통해 체크하고
        if check_move(n, m, y+dy, x+dx, log, maze):
            # 유효한 위치라면 result에 추가
            result.append((y+dy, x+dx))
    # result를 반환해준다.
    return result

def bfs(maze, ry, rx, by, bx, n, m):
    # 최단 횟수 저장할 변수
    answer = 0
    
    # 방문용 배열 만들기 (ry, rx, by, bx)
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # 최근 기록 배열 만들기
    log_red = [[False] * m for _ in range(n)]
    log_blue = [[False] * m for _ in range(n)]
    
    # 스타트 위치는 방문으로 표시해준다.
    log_red[ry][rx] = True
    log_blue[by][bx] = True
    
    # BFS 탐색으로 최단 횟수를 알기 위해, Queue 생성
    Q = deque()
    Q.append((ry, rx, by, bx, log_red, log_blue, 0))
    
    # BFS 탐색 시작
    while Q:
        # Q의 값을 꺼내온다.
        ry, rx, by, bx, rV, bV, cnt = Q.popleft()
        # 방문한 장소라면 패스
        if visited[ry][rx][by][bx]: continue
        # 아니라면 방문 체크
        visited[ry][rx][by][bx] = True
        
        # 빨간 수레, 파란 수레 도착지점 체크 변수
        chk_r, chk_b = False, False
        # 빨간 수레가 도착지점 도착 시 True
        if maze[ry][rx] == 3: chk_r = True
        # 파란 수레가 도착지점 도착 시 True
        if maze[by][bx] == 4: chk_b = True
        
        # 둘 다 도착지점 도착 완료했다면,
        if chk_r & chk_b:
            # answer에 현재까지 카운트 저장 후 탈출
            answer = cnt
            break
        # 빨간 수레, 파란 수레 둘 다 도착 못 함
        elif ((not chk_r) & (not chk_b)):
            # 빨간 수레 유효 좌표 체크
            nrs = move(n, m, ry, rx, rV, maze)
            # 파란 수레 유효 좌표 체크
            nbs = move(n, m, by, bx, bV, maze)
        # 빨간 수레 도착, 파란 수레 미도착
        elif (chk_r & (not chk_b)):
            # 파란 수레 유효 좌표 체크
            nbs = move(n, m, by, bx, bV, maze)
            # 빨간 수레는 현위치 고정!
            nrs = [(ry, rx)]
        # 빨간 수레 미도착, 파란 수레 도착
        elif ((not chk_r) & chk_b):
            # 빨간 수레 유효 좌표 체크
            nrs = move(n, m, ry, rx, rV, maze)
            # 파란 수레는 현위치 고정!
            nbs = [(by, bx)]
        
        # 빨간 수레 이동 가능 위치와 파란 수레 이동 가능 위치 탐색
        for nry, nrx in nrs:
            for nby, nbx in nbs:
                # 현재 이동한 위치의 두 수레가 겹치면 패스
                if ((nry == nby) & (nrx == nbx)): continue
                # 만약 서로 이동한 위치가 이전 위치를 바꾼거라면 패스(겹치는 이동)
                if (((nry==by)&(nrx==bx))and((nby==ry)&(nbx==rx))): continue
                
                # 걸리는 부분 없이 이동가능하다면, 해당 위치로 옮겨준다.
                cnt += 1
                # 해당 위치 방문 체크를 해준다.
                rV[nry][nrx], bV[nby][nbx] = True, True
                # Q 에 해당위치들을 넣어준다.
                Q.append((nry, nrx, nby, nbx, rV, bV, cnt))
                
                # for 문 내에서 다음 위치들 확인할 때 누적연산 되므로
                cnt -= 1
                rV[nry][nrx], bV[nby][nbx] = False, False
    # answer 그대로 return
    return answer

def solution(maze):
    n = len(maze) # 세로 길이
    m = len(maze[0]) # 가로 길이
    
    # 수레들 스타트 위치 찾기
    for y in range(n):
        for x in range(m):
            # 빨간 수레 위치 저장
            if maze[y][x] == 1:
                ry, rx = y, x
                # 해당 위치는 빈칸으로 초기화
                maze[y][x] = 0
            # 파란 수레 위치 저장
            elif maze[y][x] == 2:
                by, bx = y, x
                # 해당 위치는 빈칸으로 초기화
                maze[y][x] = 0
    
    # BFS 탐색 함수에 넣고, 최단 횟수를 answer에 저장
    answer = bfs(maze, ry, rx, by, bx, n, m)
    return answer
</code></pre>
</details>

</details>
<hr>

<h6 class="guide-section-title">문제 설명</h6>
<div class="markdown solarized-dark"><p><code>n</code> x <code>m</code> 크기 격자 모양의 퍼즐판이 주어집니다.</p>
<p>퍼즐판에는 빨간색 수레와 파란색 수레가 하나씩 존재합니다. 각 수레들은 자신의 시작 칸에서부터 자신의 도착 칸까지 이동해야 합니다.<br/>
모든 수레들을 각자의 도착 칸으로 이동시키면 퍼즐을 풀 수 있습니다.</p>
<p>당신은 각 턴마다 <strong>반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야 합니다.</strong> 단, 수레를 움직일 때는 아래와 같은 규칙이 있습니다.</p>
<ul>
<li>수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.</li>
<li>수레는 자신이 방문했던 칸으로 움직일 수 없습니다.</li>
<li>자신의 도착 칸에 위치한 수레는 <strong>움직이지 않습니다.</strong> 계속 해당 칸에 고정해 놓아야 합니다.</li>
<li>동시에 두 수레를 같은 칸으로 움직일 수 없습니다.</li>
<li>수레끼리 자리를 바꾸며 움직일 수 없습니다.</li>
</ul>
<p>예를 들어, 아래 그림처럼 <code>n</code> = 3, <code>m</code> = 2인 퍼즐판이 있습니다.</p>
<p><img alt="rb_horse1.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/2d21a258-144f-4d03-81c1-1a857a942efa/rb_horse1.jpg" title=""/></p>
<ul>
<li>속이 빨간색인 원은 빨간색 수레를 나타냅니다.</li>
<li>속이 파란색인 원은 파란색 수레를 나타냅니다.</li>
<li>테두리가 빨간색인 원은 빨간색 수레의 도착 칸을 나타냅니다.</li>
<li>테두리가 파란색인 원은 파란색 수레의 도착 칸을 나타냅니다.</li>
</ul>
<p>위 퍼즐판은 아래와 같은 순서로 3턴만에 풀 수 있습니다.</p>
<p><img alt="rb_horse2.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e1c81aa3-238b-4f0e-b21d-697903543b72/rb_horse2.jpg" title=""/></p>
<ul>
<li>빨간색 사선이 처진 칸은 빨간색 수레가 방문했던 칸을 나타냅니다. 규칙에 따라 빨간색 수레는 빨간색 사선이 처진 칸(방문했던 칸)으로는 이동할 수 없습니다.</li>
<li>파란색 사선이 처진 칸은 파란색 수레가 방문했던 칸을 나타냅니다. 규칙에 따라 파란색 수레는 파란색 사선이 처진 칸(방문했던 칸)으로는 이동할 수 없습니다.</li>
</ul>
<p><img alt="rb_horse3.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/2b78f38c-121a-441c-90f9-704eb0642e96/rb_horse3.jpg" title=""/></p>
<ul>
<li>위처럼 동시에 수레를 같은 칸으로 움직일 수는 없습니다.</li>
</ul>
<p>퍼즐판의 정보를 나타내는 2차원 정수 배열 <code>maze</code>가 매개변수로 주어집니다. 퍼즐을 푸는데 필요한 턴의 최솟값을 return 하도록 solution 함수를 완성해 주세요. 퍼즐을 풀 수 없는 경우 0을 return 해주세요.</p>
<hr/>
<h5>제한사항</h5>
<ul>
<li>1 ≤ <code>maze</code>의 길이 (= 세로 길이) ≤ 4

<ul>
<li>1 ≤ <code>maze[i]</code>의 길이 (= 가로 길이) ≤ 4</li>
<li><code>maze[i][j]</code>는 0,1,2,3,4,5 중 하나의 값을 갖습니다.</li>
</ul></li>
</ul>
<table class="table">
<thead><tr>
<th><code>maze[i][j]</code></th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td>0</td>
<td>빈칸</td>
</tr>
<tr>
<td>1</td>
<td>빨간 수레의 시작 칸</td>
</tr>
<tr>
<td>2</td>
<td>파란 수레의 시작 칸</td>
</tr>
<tr>
<td>3</td>
<td>빨간 수레의 도착 칸</td>
</tr>
<tr>
<td>4</td>
<td>파란 수레의 도착 칸</td>
</tr>
<tr>
<td>5</td>
<td>벽</td>
</tr>
</tbody>
</table>
<ul>
<li>빨간 수레의 시작 칸, 빨간 수레의 도착 칸, 파란 수레의 시작 칸, 파란 수레의 도착 칸은 퍼즐판에 1개씩 존재합니다.</li>
</ul>
<hr/>
<h5>입출력 예</h5>
<table class="table">
<thead><tr>
<th>maze</th>
<th>result</th>
</tr>
</thead>
<tbody><tr>
<td>[[1, 4], [0, 0], [2, 3]]</td>
<td>3</td>
</tr>
<tr>
<td>[[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]</td>
<td>7</td>
</tr>
<tr>
<td>[[1, 5], [2, 5], [4, 5], [3, 5]]</td>
<td>0</td>
</tr>
<tr>
<td>[[4, 1, 2, 3]]</td>
<td>0</td>
</tr>
</tbody>
</table>
<hr/>
<h5>입출력 예 설명</h5>
<p><strong>입출력 예 #1</strong></p>
<p>문제 예시와 같습니다.</p>
<p><strong>입출력 예 #2</strong></p>
<p><img alt="rb_horse4.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/54629429-3bec-4288-a7b4-6303c0929880/rb_horse4.jpg" title=""/></p>
<p>7턴만에 퍼즐을 풀 수 있습니다. 다른 방법으로도 퍼즐을 풀 수 있지만 7턴보다 빠르게 풀 수는 없습니다.</p>
<p><strong>입출력 예 #3</strong></p>
<p><img alt="rb_horse5.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/c6aed2ad-dbbf-477e-bac7-fd5cd44bad00/rb_horse5.jpg" title=""/></p>
<p>다음 턴에 파란색 수레가 파란색 수레의 도착 칸에 위치한 후 고정되어 빨간색 수레가 빨간색 수레의 도착 칸에 도착할 수 없게 됩니다.<br/>
퍼즐을 풀 수 없으므로 0을 return 해야 합니다.</p>
<p><strong>입출력 예 #4</strong></p>
<p><img alt="rb_horse6.jpg" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0ff7e955-77d6-4760-9e16-75cf2313fc0d/rb_horse6.jpg" title=""/></p>
<p>수레는 서로 위치를 바꾸면서 움직일 수 없으므로 퍼즐을 풀 수 없습니다. 따라서 0을 return 해야 합니다.</p>
</div>
