import heapq


def a_star(graph, start, goal, heuristic):
    # Priority queue to store (cost, current_node, path)
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # (f(n), current node, path)
    visited = set()  # Keep track of visited nodes

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        # Goal check
        if current == goal:
            return path, cost

        # Explore neighbors
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                g_cost = cost + weight
                f_cost = g_cost + heuristic(neighbor)
                heapq.heappush(pq, (f_cost, neighbor, path + [neighbor]))

    return None, float('inf')  # If no path is found

# Input Graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 1},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'G': 3},
    'F': {'C': 1, 'G': 2},
    'G': {'E': 3, 'F': 2}
}

# Heuristic Function (Example)
heuristic = lambda node: {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 0}[node]

# Execution
start_node = 'A'
goal_node = 'G'
path, cost = a_star(graph, start_node, goal_node, heuristic)
print(f"Shortest path: {path}")
print(f"Cost: {cost}")



print("------------------------- A* Memory Bound State ------------------")
import heapq

def memory_bounded_a_star(graph, start, goal, heuristic, memory_limit):
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # (f(n), current node, path)
    visited = set()
    memory = 0

    while pq:
        if memory > memory_limit:
            # Prune the least promising node
            pq.sort(key=lambda x: x[0])  # Sort by cost
            pq = pq[:memory_limit]
            memory = len(pq)

        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, cost

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                g_cost = cost + weight
                f_cost = g_cost + heuristic(neighbor)
                heapq.heappush(pq, (f_cost, neighbor, path + [neighbor]))
                memory += 1

    return None, float('inf')

# Input Graph and Execution (Same as above)
memory_limit = 5  # Example memory limit
path, cost = memory_bounded_a_star(graph, start_node, goal_node, heuristic, memory_limit)
print(f"Memory-Bounded Shortest path: {path}")
print(f"Cost: {cost}")

