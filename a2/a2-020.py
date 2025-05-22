def find_cycle_length(start, mapping, visited):
    length = 0
    current_pos = start
    while True:
        if visited[current_pos]:
            break
        visited[current_pos] = True
        length += 1
        current_pos = mapping[current_pos]
        if current_pos == start:
            break
    return length

num_players = int(input())
transfer_map = [0] * (num_players + 1)
visited_nodes = [False] * (num_players + 1)

for player in range(1, num_players + 1):
    transfer_map[player] = int(input())

longest_cycle = 0
for player in range(1, num_players + 1):
    if not visited_nodes[player]:
        cycle_len = find_cycle_length(player, transfer_map, visited_nodes)
        if cycle_len > longest_cycle:
            longest_cycle = cycle_len

print(longest_cycle)
