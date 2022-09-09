import copy
answer = 0

def solution(info, edges):     
    global answer
    
    graph = [[] for _ in range(len(info))]
    visited = [False for _ in range(len(info))]
    for i, j in edges:
        graph[i].append(j)
        
    dfs(0, visited, graph, info, [], 0, 0)
    return answer

def dfs(node, visited, graph, info, stack, wc, sc):
    visited[node] = True
    if info[node] == 1:
        wc += 1 
        if wc >= sc:
            return 
    else:
        sc += 1
        global answer
        answer = max(answer, sc)

    for i in graph[node]:
        stack.append(i)
    for i in stack:
        if not visited[i]:
            dfs(i, visited, graph, info, copy.copy(stack), wc, sc)
            visited[i] = False