from collections import deque


def get_cords(cords):
    return cords[0] // 50, cords[1] // 50


def bfs(graph, start, goal):
    queque = deque([start])
    visited = {start: None}

    while queque:
        cur_node = queque.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queque.append(next_node)
                visited[next_node] = cur_node
    cur = goal
    a = [cur]
    while cur != start:
        cur = visited[cur]
        a.append(cur)
    return a


def generate_graph(file):
    not_zero = []
    lvl = open(file, 'r').readlines()
    lvl = [i.replace('\n', '') for i in lvl]
    matrix = [[int(i) for i in j] for j in lvl]
    cords = {(j, i): [] for i in range(len(matrix)) for j in range(len(matrix[0]))}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                cords[(j, i)] = None
                not_zero.append((j, i))
    for cord in cords:
        if cord not in not_zero:
            cords_ = []
            if cord[0] != 0 and cords[(cord[0] - 1, cord[1])] is not None:
                cords_.append((cord[0] - 1, cord[1]))
            if cord[0] != 15 and cords[(cord[0] + 1, cord[1])] is not None:
                cords_.append((cord[0] + 1, cord[1]))
            if cord[1] != 0 and cords[(cord[0], cord[1] - 1)] is not None:
                cords_.append((cord[0], cord[1] - 1))
            if cord[1] != 11 and cords[(cord[0], cord[1] + 1)] is not None:
                cords_.append((cord[0], cord[1] + 1))
            cords[cord] = cords_

    return cords


def get_direction(start, goal, file, direction):
    cord = bfs(generate_graph(file), start, goal)[0]
    print(cord)
    if start[0] < cord[0]:
        direction = 1
    elif start[0] > cord[0]:
        direction = 3
    elif start[1] < cord[1]:
        direction = 2
    elif start[1] > cord[1]:
        direction = 0
    return direction


