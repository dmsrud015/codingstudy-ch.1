from collections import deque

def search(N):

    visited = [0] * 100001
    Q = deque()
    Q.append(N) #출발 지점 N을 큐에 추가하고, visited[N]을 0으로 초기화합니다.

    while Q: #큐가 빌 때까지 다음 과정을 반복합니다.
        position = Q.popleft() #큐에서 위치를 하나 꺼내고, 해당 위치를 현재 위치로 설정합니다.
        if position == K: #현재 위치가 도착 지점 K와 같은지 확인합니다. 같다면, visited[K] 값을 반환하고 종료합니다.
            return visited[position]

        for next_position in (position + 1, position - 1, position * 2) :

            if 0 <= next_position < 100001:     #next_position이 범위(0 이상 100000 이하) 안에 있는지 확인하고, 
                if visited[next_position] == 0:  # visited[next_position]이 0인지 확인합니다. visited[next_position]이 0이라면, 아직 방문하지 않은 위치이므로, 다음과 같은 과정을 수행합니다
                    if next_position == position * 2 and next_position != 0:
                        visited[next_position] = visited[position]
                        Q.appendleft(next_position)
                    else:
                        visited[next_position] = visited[position] + 1
                        Q.append(next_position)


N, K = map(int, input().split())
answer = search(N)
print(answer)


#######################################################################################
from collections import deque

def search(N, K):
    visited = [-1] * 100001 #처음수를 -1로 초기화
    q = deque()
    q.append(N)    #큐에 N추가
    visited[N] = 0  #초기솨

    while q:
        s = q.popleft() # 큐에서 하나씩 빼서 실행

        if s == K:
            return visited[s]

        if s*2 <= 100000 and visited[s*2] == -1: #-1이니까 무조건 실행/10000보다 적으면 실행
            visited[s*2] = visited[s]
            q.appendleft(s*2)
            
        if s+1 <= 100000 and visited[s+1] == -1:
            visited[s+1] = visited[s] + 1
            q.append(s+1)

        if s-1 >= 0 and visited[s-1] == -1:
            visited[s-1] = visited[s] + 1
            q.append(s-1)

N, K = map(int, input().split())
answer = search(N, K)
print(answer)

