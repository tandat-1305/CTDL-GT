import networkx as nx
import matplotlib.pyplot as plt


g = nx.DiGraph()
g.add_nodes_from([1,3,5,7,9])
g.add_edge(1,3)
g.add_edge(5,7)
g.add_edge(3,9)
g.add_edge(1,7)
g.add_edge(3,5)
g.add_edge(9,3)
g.add_edge(5,1)

nx.draw(g,with_labels=True, arrows=False)
plt.draw()
plt.show()