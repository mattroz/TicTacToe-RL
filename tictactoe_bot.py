import numpy as np

class RLAgent:

	def __init__(self, marker, field_size=3, learning_rate=0.3):
		self.observation = []
		self.qvalues = {}
		self.learning_rate = learning_rate
		self.number_of_actions = field_size**2
		self.marker = marker
		self.current_state = None
		self.previous_state = None
		self.previous_action = None
		self.action_to_coordinates_map = {}
		# Fill a2c map:
		act_idx = 0
		for i in range(0, field_size):
			for j in range(0, field_size):
				self.action_to_coordinates_map.update({act_idx: [i,j]})
				act_idx += 1

	
	def act(self):
		# Determine the most profitable action to execute
		# from the current state
		max_value = max(self.qvalues[self.current_state])
		action = self.qvalues[self.current_state].index(max_value)
		return self.action_to_coordinates(action)
	
	
	def action_to_coordinates(self, action):
		return self.action_to_coordinates_map[action]


	def observe(self, state):
		# check if the given state is already a known state
		if state not in self.qvalues.keys():
			# if it is not, add the new state to the Q values table and init values with 0s 
			self.qvalues.update({state: [np.random.rand() for x in range(0, self.number_of_actions)]})	
		self.previous_state, self.current_state = self.current_state, state
		
