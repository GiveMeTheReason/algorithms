'''
Dijkstra's algorithm
'''

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in passed_set:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def print_way(parents):
    cur_node = "fin"
    way = cur_node
    while not cur_node == "start":
        way = parents[cur_node] + ", " + way
        cur_node = parents[cur_node]
    return way

graph = {}
graph["start"] = {}
graph["start"]["1"] = 2
graph["start"]["2"] = 2

graph["1"] = {}
graph["1"]["3"] = 2
graph["1"]["fin"] = 2

graph["2"] = {}
graph["2"]["1"] = 2

graph["3"] = {}
graph["3"]["2"] = -1
graph["3"]["fin"] = 2

graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["1"] = 2
costs["2"] = 2
costs["3"] = infinity
costs["fin"] = infinity

parents = {}
parents["1"] = "start"
parents["2"] = "start"
parents["3"] = None
parents["fin"] = None

passed_set = set()

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    passed_set.add(node)
    node = find_lowest_cost_node(costs)

print(costs["fin"])  # 4
print(print_way(parents))  # start, 1, fin
