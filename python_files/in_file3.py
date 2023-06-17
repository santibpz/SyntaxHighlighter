import sys
import math

def bfs(n, edges, s):
    #initialize state, distance and parent for all the vertices
    state = [0 for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [-1 for i in range(n)]
    #initialize state, distance and parent for the source vertex
    state[s] = 1 
    distance[s] = 0 
    parent[s] = 'NIL'
    queue = []
    arr = []
    queue.append(s)
    #Start discovering the vertices starting from the source vertex
    while queue:
        x = queue.pop(0)
        arr.append(x)
        #Start discovering the vertices adjacent to x and store
        #information about their parent, distance and state
        for i in range(len(edges[x])):
            if state[edges[x][i]] == 0:
                state[edges[x][i]] = 1 
                distance[edges[x][i]] = distance[x] + 1
                parent[edges[x][i]] = x 
                queue.append(edges[x][i])
        state[x] = -1
 
    return arr 
 
def main():
   #input format is described below
    n, m, s = map(int, input().split())
    edges = {}
    for i in range(n):
        edges[i] = []
    for i in range(m):
        a, b = map(int, input().split())
        edges[a] += [b]
        edges[b] += [a]
    for i in range(n):
        edges[i].sort()
    arr = bfs(n, edges, s)
    print(*arr)
 
if __name__ == '__main__':
    main()