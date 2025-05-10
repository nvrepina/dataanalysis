import networkx as nx

n = 17
p = 0.8

G = nx.erdos_renyi_graph(n, p)

a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(f'Cредняя степень вершины: {float(a) / len(G.nodes())}')

print(
    f'Cредняя степень вершины по представленной формуле: '
    f'{(n - 1) * p}')