import matplotlib.pyplot as plt
import networkx as nx

def is_safe(graph, color, node, colors, node_names):
    for neighbor in graph[node]:
        if colors[node_names.index(neighbor)] == color:
            return False
    return True

def solve_csp(graph, m, colors, node=0, node_names=None):
    if node == len(graph):
        return True
    for color in range(1, m+1):
        if is_safe(graph, color, node_names[node], colors, node_names):
            colors[node] = color
            if solve_csp(graph, m, colors, node + 1, node_names):
                return True
            colors[node] = 0
    return False

def graph_coloring(graph, m):
    node_names = list(graph.keys())
    colors = [0] * len(graph)
    if solve_csp(graph, m, colors, 0, node_names):
        return dict(zip(node_names, colors))
    return None

def display_coloring(graph, coloring):
    if coloring is None:
        print("No valid coloring found.")
        return

    print("\nRegion Color Assignment:")
    for region, color in coloring.items():
        print(f"{region} → Color {color}")

    G = nx.Graph()
    for region in graph:
        for neighbor in graph[region]:
            G.add_edge(region, neighbor)

    color_map = ['gray', 'red', 'blue', 'green', 'orange', 'purple', 'cyan']
    node_colors = [color_map[coloring[region]] for region in G.nodes]

    pos = nx.spring_layout(G, seed=42)  # Consistent layout
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_color='white', font_weight='bold')
    plt.title("Australia Map Coloring")
    plt.show()

# Australia adjacency graph
australia_graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'QLD'],
    'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['QLD', 'SA', 'VIC'],
    'VIC': ['SA', 'NSW', 'TAS'],
    'TAS': ['VIC']
}

# Number of colors (minimum needed = 3 or 4)
m = 4

# Get and display result
coloring_result = graph_coloring(australia_graph, m)
display_coloring(australia_graph, coloring_result)
