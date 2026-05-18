# 문제: 그룹 ID
# 날짜: 2026-05-18

from collections import deque

# 입력 받기
N, M = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# BFS 준비
visited = [False] * (N + 1)
maxSize = 0
ansID = 0

#1번부터 N번까지 돌면서
for i in range(1, N + 1):
    if not visited[i]:
        queue = deque() 
        queue.append(i)
        visited[i] = True
        size = 0     # 여기까지는 BFS 준비! while문 들어가기 전에 세팅하는 거임.

        while queue: # 큐가 빌 때까지 반복
            cur = queue.popleft() #가장 앞에 있는 노드 꺼내기
            size += 1   #그룹 크기 1 증가

            for next in graph[cur]: #cur과 연결된 노드들(next) 탐색
                if not visited[next]:
                    visited[next] = True
                    queue.append(next) # 큐에 새로운 노드 추가

            
        # 그룹 크기가 최대인 경우 업데이트
        if size > maxSize:
            maxSize = size
            ansID = i
# 결과 출력
print(ansID)

    