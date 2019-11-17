import networkx as nx
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
import simulation
from collections import defaultdict, deque


G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
print(nx.info(G_fb))

# Print graph
# nx.spring_layout(G_fb)
# nx.draw_networkx(G_fb, pos=nx.spring_layout(G_fb), with_labels=False, node_size=10)
# plt.show()


# Assign weight
network = simulation.Simulation(G_fb)
node = network.pick_random_node()
network.assign_weight(node, 'near')

# Set Edge Color based on weight
# Taken from https://stackoverflow.com/questions/43644210/python-networkx-add-weights-to-edges-by-frequency-of-edge-occurance
num_edges = nx.number_of_edges(G_fb)
values = range(num_edges)
jet = cm = plt.get_cmap('YlOrRd')
cNorm  = matplotlib.colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = matplotlib.cm.ScalarMappable(norm=cNorm, cmap=jet)
colorList = []

for i in range(num_edges):
    colorVal = scalarMap.to_rgba(values[i])
    colorList.append(colorVal)


# Print graph with different weights
pos = nx.spring_layout(G_fb)
# betCent = nx.betweenness_centrality(G_fb, normalized=True, endpoints=True)
# node_color = [20000.0 * G_fb.degree(v) for v in G_fb]
# node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G_fb, pos=pos, with_labels=False,
                 node_size=5, edge_color= colorList)
plt.axis('off')
plt.show()
