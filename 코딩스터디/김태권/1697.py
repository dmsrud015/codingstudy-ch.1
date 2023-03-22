import sys
from collections import deque

def bfs(v):
    q = deque([v])                     #deque 모듈을 이용하여 큐를 생성합니다
    while q:                          #while문에서 큐가 빌 때까지 반복합니다.
        v = q.popleft()               #큐에서 노드를 하나씩 꺼내면서,
        if v == k:                   #해당 노드와 목표 노드 k가 같은지 확인합니다. 
            return array[v]         #같다면, 해당 노드의 거리를 반환합니다,그렇지 않다면, 해당 노드의 이웃한 노드들을 찾아서 큐에 삽입합니다.
        for next_v in (v-1, v+1, 2*v):     #이웃한 노드들은 v-1, v+1, 2*v로 찾아집니다
            if 0 <= next_v < MAX and not array[next_v]: #이때, 노드가 MAX보다 작거나 같은 범위 내에 있으며,이미 방문한 적이 없는 노드일 경우에만 큐에 삽입합니다.
                array[next_v] = array[v] + 1   #추가된 노드들은 array 배열에 현재 노드 v까지의 거리에 1을 더한 값으로 업데이트됩니다. 이후, 큐에서 다음 노드를 꺼내서 같은 과정을 반복합니다.
                q.append(next_v)


MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX
print(bfs(n))

#v = q.popleft()는 큐에서 가장 왼쪽에 있는 노드를 꺼내서 변수 v에 할당하는 것입니다. 큐는 선입선출(FIFO) 구조이기 때문에 가장 먼저 들어온 노드가 가장 왼쪽에 위치하게 됩니다.

#BFS 알고리즘에서는 가장 먼저 들어온 노드부터 탐색해야 하므로, q.popleft()를 이용하여 큐에서 가장 왼쪽에 있는 노드를 꺼내서 탐색합니다. 이때, 꺼낸 노드는 이후에는 큐에서 제거됩니다.
