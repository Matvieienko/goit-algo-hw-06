import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графу, транспортної мережі
G = nx.Graph()

# Додавання вершин 
nodes = ["Home", "Trakt", "LS", "OR", "AK", "DG", "OB", "Work"]
G.add_nodes_from(nodes)

# Додавання ребер з вагами
edges = [
    ("Home", "Trakt", 4),
    ("Home", "LS", 4),
    ("Trakt", "OR", 2),
    ("LS", "AK", 3),
    ("LS", "OR", 2),
    ("OR", "DG", 3),
    ("AK", "DG", 3),
    ("AK", "OB", 6),
    ("OB", "Work", 2),
    ("DG", "Work", 4)
]
G.add_weighted_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Мережа міста з вагами")
plt.show()

# Реалізація алгоритму Дейкстри

def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0
    pq = [(0, start)]  # Пріоритетна черга (відстань, вершина)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Якщо поточна відстань більша, ніж вже відома, пропускаємо
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

# Обчислення найкоротших шляхів від "Home"
shortest_paths_from_home = dijkstra(G, "Home")

# Виведення результатів
print("Найкоротші шляхи від 'Home':")
for target, distance in shortest_paths_from_home.items():
    print(f"  До {target}: відстань {distance}")