sol1)deque를 사용한 풀이

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(int(input())):   
    m, n, k = map(int,input().split())      #가로, 세로, 배추의 개수
    s = [[0]*m for i in range(n)]
    visit = [[0]*m for i in range(n)]       #방문한s표시
    deq = deque()
    for i in range(k):
        a, b = map(int, input().split())
        s[b][a]=1                           #a, b가 아닌 b, a로 하는 이유는 x, y로 인수를 받는데 s는 s[세로][가로]로 표현하였으므로 b, a로 해야함
        deq.append((b, a))                  #deque에 배추의 위치 append
    while deq:                      #s를 조작하여 인접한 배추 제거하고 방문한 위치는 visit로 체크
        x, y = deq.pop()
        visit[x][y]=1
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m:
                if s[a][b]==1 and visit[a][b]==0:
                    visit[a][b]=1
                    s[a][b]=0
                    deq.append((a, b))
    p=0
    for i in s:             #s의 합
        p+=sum(i)
    print(p)

    
    
    
 
sol 2) 메모리 초과    
    
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

def dfs(i, j):
  s[i][j]=0
  for a in range(4):
    if i<0 or i>=n or j<0 or j>=m:
      return
    x = dx[a] + i
    y = dy[a] + j
    if i<0 or i>=n or j<0 or j>=m:
      return
    dfs(x, y)


for _ in range(int(input())):
  m, n, k = map(int, input().split())     #가로, 세로, 배추의 개수
  s = [[0]*(m) for i in range(n)]
  for i in range(k):
    b, a = map(int, input().split())
    s[a][b]=1
  cnt=0
  for i in range(n):                      #방문한 위치에 있는 배추 + 인접한 배추 모두 제거하고, 제거한 횟수를 셈으로써 cnt+=1해줌
    for j in range(m):
      if s[i][j]==1:                      #i:세로, j:가로
        dfs(i, j)
        cnt+=1
  print(cnt)
