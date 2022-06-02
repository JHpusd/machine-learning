def find_connected(node_num, edge_list):
    return [edge for edge in edge_list if edge[0]==node_num]

def repeat(in_list):
    return list(set(in_list)) != in_list

def check_for_cycle(edge_list):
    cycle = False
    for edge in edge_list:
        current_edges = [edge]
        visited_nodes = [edge[0], edge[1]]
        while True:
            connected = []
            for e in current_edges:
                connected += find_connected(e[1], edge_list)
            if connected == []:
                break
            for c_edge in connected:
                visited_nodes.append(c_edge[1])
            current_edges = connected
            if repeat(visited_nodes):
                cycle = True
                break
    return cycle

edges = [(1,2),(2,5),(5,6)]
print(check_for_cycle(edges))

edges = [(1,2),(2,3),(3,4),(4,1),(2,5),(5,6)]
print(check_for_cycle(edges))