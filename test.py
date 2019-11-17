import simulation
import networkx as nx

G = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)


test_node = simulation.Simulation(G)
print(test_node.pick_random_node())

E = nx.path_graph([0,1,2])
test_bfs = simulation.Simulation(E)


near_sources = set()

while len(near_sources) != 3:
	node = test_bfs.pick_random_node()
	print('Source node is: ', node)
	if node in near_sources:
		print('Node already picked before!\n')
	else:
		near_sources.add(node)
		test_bfs.add_weight(node, 'near')
		print('Weight edge 0-1 : ', E[0][1]['weight'])
		print('Weight edge 1-2: ', E[1][2]['weight'])
		print('\n')

far_sources = set()

while len(far_sources) != 3:
	node = test_bfs.pick_random_node()
	print('Source node is: ', node)
	if node in far_sources:
		print('Node already picked before!\n')
	else:
		far_sources.add(node)
		test_bfs.add_weight(node, 'far')
		print('Weight edge 0-1 : ', E[0][1]['weight'])
		print('Weight edge 1-2: ', E[1][2]['weight'])
		print('\n')

print(test_bfs.calculate_threshold(0))
print(test_bfs.calculate_threshold(1))
print(test_bfs.calculate_threshold(2))

