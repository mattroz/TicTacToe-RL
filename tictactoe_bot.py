import numpy as np

class RLAgent:

	def __init__(self, marker, field_size=3, learning_rate=0.3):
		self._observation = []
		self._qvalues = {}
		self._learning_rate = learning_rate
		self._discount_factor = 0.5
		self._number_of_actions = field_size**2
		self.marker = marker
		self._current_state = None
		self._previous_state = None
		self._previous_action = None
		self._last_action = None
		self._action_to_coordinates_map = {}
		# Fill a2c map:
		act_idx = 0
		for i in range(0, field_size):
			for j in range(0, field_size):
				self._action_to_coordinates_map.update({act_idx: [i,j]})
				act_idx += 1

	
	def act(self):
		# Determine the most profitable action to execute
		# from the current state
		value = self.maxQ(self._current_state)
		action = self._qvalues[self._current_state].index(value)
		self._last_action = action
		print('action: ', action)
		return self._action_to_coordinates_map[action]
	
	
	def maxQ(self, state):
		max_q_value = max(self._qvalues[state])
		return max_q_value	
		

#	def action_to_coordinates(self, action):
#		return self._action_to_coordinates_map[action]


	def observe(self, state):
		# check if the given state is already a known state
		if state not in self._qvalues.keys():
			# if it is not, add the new state to the Q values table and init values with 0s 
			self._qvalues.update({state: [np.random.rand() for x in range(0, self._number_of_actions)]})	
			#self._qvalues.update({state: [0 for x in range(0, self._number_of_actions)]})	
			
		self._previous_state, self._current_state = self._current_state, state
	
	
	def learn(self, reward):
		'''
		Q(s,a) = Q(s,a) + learning_rate * (reward + discount*maxQ(s',a) - Q(s,a))
		'''
		curr_state = self._current_state
		prev_state = self._previous_state
		last_action = self._last_action
		self._qvalues[prev_state][last_action] += self._learning_rate * (reward + self._discount_factor * self.maxQ(curr_state) - self._qvalues[prev_state][last_action])
			
