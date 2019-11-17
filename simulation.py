import networkx as nx
import random
from collections import defaultdict, deque


class Simulation:

	def __init__(self, G):
		self.G = G


	def pick_random_node(self):
		total_nodes = nx.number_of_nodes(self.G)
		random_node = random.randint(0, total_nodes - 1)
		return random_node

	def assign_weight(self, source, audience_type):
		if audience_type == 'near':
			weight = 2 ** 7 #hard coded to be the longest shortest path of the FB graph
		else:
			weight = 1

		neighbors = self.G.neighbors
		visited = set([source])
		queue = deque([(source, neighbors(source), weight)])
		
		while queue:
			parent, children, curr_weight = queue[0]
			try:
				child = next(children)
				if child not in visited:
					self.G[parent][child]['weight'] = curr_weight
					if audience_type == 'near':
						curr_weight = curr_weight // 2
					else:
						curr_weight = curr_weight * 2 
					visited.add(child)
					queue.append((child, neighbors(child), curr_weight))
			except StopIteration:
				queue.popleft()

	def calculate_threshold(self, source):
		num_neighbors = self.G.neighbors(source)
		return len(list(num_neighbors)) * 10

	def assign_probabilities(self, source, starting_probability, step):
		probability = starting_probability
		neighbors = self.G.neighbors
		visited = set([source])
		queue = deque([(source, neighbors(source), probability)])
		
		while queue:
			parent, children, curr_probability = queue[0]
			try:
				child = next(children)
				if child not in visited:
					self.G.nodes[child]['probability'] = curr_probability
					new_probability = curr_probability + step
					visited.add(child)
					queue.append((child, neighbors(child), new_probability))
			except StopIteration:
				queue.popleft()