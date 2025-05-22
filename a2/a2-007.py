num_tanks, num_targets = map(int, input().split())
tank_positions = [None] * (num_tanks + 1)
for idx in range(1, num_tanks + 1):
    left_x, right_x = map(int, input().split())
    tank_positions[idx] = (left_x, right_x)

parent = list(range(num_tanks + 1))
for i in range(1, num_tanks + 1):
    for j in range(i + 1, num_tanks + 1):
        if tank_positions[j][1] > tank_positions[i][1]:
            break
        parent[j] = i

children = [[] for _ in range(num_tanks + 1)]
for node in range(1, num_tanks + 1):
    if parent[node] != node:
        children[parent[node]].append(node)

has_target = [0] * (num_tanks + 1)
target_list = list(map(int, input().split()))
for t in target_list:
    has_target[t] = 1

depth = [0] * (num_tanks + 1)

stack = []
visited = [False] * (num_tanks + 1)

for root in range(1, num_tanks + 1):
    if parent[root] == root and not visited[root]:
        stack.append((root, 0)) 
        while stack:
            curr_node, state = stack.pop()
            if state == 0:
                visited[curr_node] = True
                stack.append((curr_node, 1))
                for child in children[curr_node]:
                    if not visited[child]:
                        depth[child] = depth[curr_node] + 1
                        stack.append((child, 0))
            else:
                for child in children[curr_node]:
                    has_target[curr_node] += has_target[child]

result = []
for root in range(1, num_tanks + 1):
    if parent[root] == root and has_target[root] > 0:
        max_depth = -1
        selected_node = -1
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if has_target[curr_node] == has_target[root]:
                if depth[curr_node] > max_depth:
                    max_depth = depth[curr_node]
                    selected_node = curr_node
                for child in children[curr_node]:
                    stack.append(child)
        if selected_node != -1:
            result.append(selected_node)

result.sort()
print(len(result))
print(*result)
