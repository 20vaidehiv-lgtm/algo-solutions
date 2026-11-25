# Problem: Course Schedule
# Source: https://leetcode.com/problems/course-schedule/
# Topic: Graph, Topological Sort

def can_finish(numCourses, prerequisites):
    # build adjacency list
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[b].append(a)

    # 0 = unvisited, 1 = visiting (in stack), 2 = done
    state = [0] * numCourses

    def has_cycle(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    for i in range(numCourses):
        if has_cycle(i):
            return False
    return True
