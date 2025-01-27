import networkx as nx
import matplotlib.pyplot as plt

# Створення графу, що моделює схему доріг від дому до роботи
G = nx.Graph()

# Додавання вершин 
nodes = ["Home", "Trakt", "LS", "OR", "AK", "DG", "OB", "Work"]
G.add_nodes_from(nodes)

# Додавання ребер 
edges = [
    ("Home", "Trakt"),
    ("Home", "LS"),
    ("Trakt", "OR"),
    ("LS", "AK"),
    ("LS", "OR"),
    ("OR", "DG"),
    ("AK", "DG"),
    ("AK", "OB"),
    ("OB", "Work"),
    ("DG", "Work")
]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Мережа міста")
plt.show()

# Аналіз графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_info = dict(G.degree())

print(f"Кількість вершин (районів): {num_nodes}")
print(f"Кількість ребер (маршрутів): {num_edges}")
print("Ступінь вершин (кількість маршрутів для кожного району):")
for node, degree in degree_info.items():
    print(f"  {node}: {degree}")

# Функція для пошуку шляху за допомогою DFS
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Функція для пошуку шляху за допомогою BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    paths.append(path + [neighbor])
                else:
                    queue.append((neighbor, path + [neighbor]))
    return paths

# Пошук шляхів між "Home" і "Work" за допомогою DFS і BFS
dfs_result = dfs_paths(G, "Home", "Work")
bfs_result = bfs_paths(G, "Home", "Work")

print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_result:
    print(" -> ".join(path))

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_result:
    print(" -> ".join(path))

# Пояснення різниці між DFS і BFS
print("\nПояснення:")
print("DFS (глибина першим) шукає шляхи, заглиблюючись у граф якомога далі, перш ніж повернутися.")
print("BFS (ширина першим) досліджує всі сусідні вершини на кожному рівні, що дозволяє знайти найкоротші шляхи.")