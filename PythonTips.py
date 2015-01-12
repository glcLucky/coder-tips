# -*- coding: utf-8 -*-

# 邻接坐标：
def get_neighbor(p, xlim, ylim, constraint):
    all_constraint = lambda p: 0 <= p[0] < xlim and 0 <= p[1] < ylim and constraint(*p)
    plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1]][1::2]
    # plist = [(p[0]+i, p[1]+j) for i in [-1,0,1] for j in [-1,0,1] if i or j]
    return filter(all_constraint, plist)
    
# 简单寻路1，判断是否相通：
from collections import deque

def is_accessible(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = set([]), deque([p1])
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    while to_search and p2 not in to_search:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        visited.add(cur_p)
        to_search += plist
    return p2 in to_search

# 简单寻路2，记录路径：
from collections import deque

def find_path(p1, p2, region):        
    xlim, ylim = len(region), len(region[0])
    visited, to_search = {p1: None}, deque([p1])
    constraint = lambda i,j: (region[i][j] in '.') and ((i,j) not in visited)
    while to_search and p2 not in to_search:
        cur_p = to_search.popleft()
        plist = get_neighbor(cur_p, xlim, ylim, constraint)
        for p in plist:
            visited[p] = cur_p
        to_search += plist
    
    if p2 not in to_search: return []
    
    trace = [cur_p, p2]
    while p1 not in trace:
        trace = [visited[trace[0]]] + trace
    return trace

# A*寻路算法，记录路径
# 需要定义距离函数h_score
def h_score(p1, p2):
    return 

def find_path_a_star(start, end, region):
    xlim, ylim = len(region), len(region[0])
    visited, to_search = {}, {start: (h_score(start, end), 0, None)}
    constraint = lambda i,j: (region[i][j] == 0) and ((i,j) not in visited)
    while to_search and (end not in to_search):
        cur_p = sorted(to_search.keys(), key = lambda x: x[0])[0]
        _, g, pre_p = to_search.pop(cur_p)
        visited[cur_p] = pre_p
        for p in get_neighbor(cur_p, xlim, ylim, constraint):
            h = h_score(p, end)
            if (p not in to_search) or (g + h + 1 < to_search[p][0]):
                to_search[p] = (g + h + 1, g + 1, cur_p)

    if end not in to_search: return []

    trace = [cur_p, end]
    while start not in trace:
        trace = [visited[trace[0]]] + trace
    return trace

# Dijkstra Algorithm
# 输入为距离矩阵，默认第一个为起始点，最后一个为结束点
def dijkstra(distance):
    S, T, D = set([0]), set(range(1,n)), distance[0][:]
    while n-1 not in S:
        p_move = min(T, key=lambda x: D[x])
        S.add(p_move)
        T.remove(p_move)
        for p_togo in T:
            D[p_togo] = min(D[p_togo], D[p_move] + distance[p_move][p_togo])
    return D[-1]
    
