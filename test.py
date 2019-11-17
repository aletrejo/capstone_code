import simulation
import networkx as nx

G = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)


test_fb_node = simulation.Simulation(G)
print(test_fb_node.pick_random_node())

E = nx.path_graph([0,1,2])
small_test = simulation.Simulation(E)


near_sources = set()

while len(near_sources) != 3:
	node = small_test.pick_random_node()
	print('Source node is: ', node)
	if node in near_sources:
		print('Node already picked before!\n')
	else:
		near_sources.add(node)
		small_test.assign_weight(node, 'near')
		print('Weight edge 0-1 : ', E[0][1]['weight'])
		print('Weight edge 1-2: ', E[1][2]['weight'])
		print('\n')

far_sources = set()

while len(far_sources) != 3:
	node = small_test.pick_random_node()
	print('Source node is: ', node)
	if node in far_sources:
		print('Node already picked before!\n')
	else:
		far_sources.add(node)
		small_test.assign_weight(node, 'far')
		print('Weight edge 0-1 : ', E[0][1]['weight'])
		print('Weight edge 1-2: ', E[1][2]['weight'])
		print('\n')

print(small_test.calculate_threshold(0))
print(small_test.calculate_threshold(1))
print(small_test.calculate_threshold(2))


small_test.assign_probabilities(0, 0.8, -0.1)
print(E.nodes[1]['probability'])
print(E.nodes[2]['probability'])

