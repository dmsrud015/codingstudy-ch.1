from collections import deque

def bfs():
    q = deque()  #먼저 deque()를 이용해 큐를 초기화합니다
    q.append(n)  #시작점인 수빈이의 위치 n을 큐에 추가합니다
    while q:    #큐에서 노드를 하나씩 꺼내면서
        v = q.popleft() #큐에서 원소를 꺼내어(q.popleft())동생의 위치와 일치하는지 확인합니다. 
        if v == k  :#해당 노드와 목표 노드 k가 같은지 확인합니다
            print(visited[v])  #같으면 visted[v]출력
            ans = []      #일치한다면,visited 리스트에서 해당 위치의 값을 출력하고, 반복문을 종료합니다.     
 # path에 저장된 경로 값을 통해 거슬러올라가면서 ans에 저장.
            while v != n:     # 일치하지 않는 경우, 현재 위치에서 갈 수 있는 모든 경우의 수를 검사합니다
                ans.append(v)  #
                v = path[v]
            ans.append(n)
            ans.reverse()  # 역순으로 저장되어 있으므로 순서를 바꿈
            print(' '.join(map(str, ans)))
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not visited[next_step]: 
                #이때, 노드가 MAX보다 작거나 같은 범위 내에 있으며,이미 방문한 적이 없는 노드일 경우에만 큐에 삽입합니다.
                visited[next_step] = visited[v] + 1# visited 리스트에서 해당 위치의 값을 업데이트하고 큐에 추가합니다
                q.append(next_step)                #이때, q.append()를 사용하여 큐의 오른쪽에 추가합니다
                path[next_step] = v               # 최종 경로 출력 시 next_step 값을 통해 이전 위치를 알아낼 수 있도록 저장함

n, k = map(int, input().split())
MAX = 100001
visited = [0] * MAX
path = [0] * MAX
bfs()
