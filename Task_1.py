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
plt.title("Транспортна мережа міста")
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