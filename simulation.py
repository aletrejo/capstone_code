import networkx as nx
import random
from collections import defaultdict, deque

class Post:

	def __init__(self, G, starting_probability, threshold_percentage):
		self.G = G
		self.starting_probability = starting_probability
		self.threshold_percentage = threshold_percentage
		self.threshold = 0
		self.interest = 0
		self.tu = 0

	def run(self, audience, step):
		# Add weight and probabilities
		source = self.pick_random_node()
		print('Source node is: ', source)
		self.assign_weight(source, audience, step)
		self.assign_probabilities(source, step)
		# Establish threshold value
		self.threshold = self.calculate_threshold(source)
		print('Threshold value is: ', self.threshold)
		while True:
			self.interest = 0
			self.activate_nodes(source)
			self.tu+= 1
			if not self.remains_online():
				break
		print('Total runs: ', self.tu)

	def pick_random_node(self):
		total_nodes = nx.number_of_nodes(self.G)
		random_node = random.randint(0, total_nodes - 1)
		return random_node


	def assign_weight(self, source, audience_type, step):
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
						curr_weight = curr_weight * step
					else:
						curr_weight = curr_weight * (1 + step) 
					visited.add(child)
					queue.append((child, neighbors(child), curr_weight))
			except StopIteration:
				queue.popleft()


	def assign_probabilities(self, source, step):
		probability = self.starting_probability
		neighbors = self.G.neighbors
		visited = set([source])
		queue = deque([(source, neighbors(source), probability)])
		
		while queue:
			parent, children, curr_probability = queue[0]
			try:
				child = next(children)
				if child not in visited:
					self.G.nodes[child]['probability'] = curr_probability
					new_probability = curr_probability * step
					visited.add(child)
					queue.append((child, neighbors(child), new_probability))
			except StopIteration:
				queue.popleft()


	def activate_nodes(self, source):
		neighbors = self.G.neighbors
		visited = set([source])
		queue = deque([(source, neighbors(source))])
		
		while queue:
			parent, children = queue[0]
			try:
				child = next(children)
				if child not in visited:
					probability = self.G.nodes[child]['probability'] * 100
					num_picked = random.randint(1, 100)
					if num_picked <= probability:
						self.interest += self.G[parent][child]['weight']
					visited.add(child)
					queue.append((child, neighbors(child)))
			except StopIteration:
				queue.popleft()


	def calculate_threshold(self, source):
		threshold_value = 0
		neighbors = self.G.neighbors(source)
		for neighbor in neighbors:
			threshold_value += self.G[source][neighbor]['weight']
		return threshold_value * self.threshold_percentage


	def remains_online(self):
		return True if self.interest >= self.threshold else False