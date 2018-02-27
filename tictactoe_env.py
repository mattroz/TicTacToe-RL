class TicTacToeEnv:

	def __init__(self, field_size):
		self.__reward = 10;
		self.__last_played = None
		self.__field_size = field_size		
		self.__delta = {'x': 1, 'o': 100, '-': 0}
		self.amount_to_win = 3
		self.__h_score = [0 for x in range(0, self.__field_size)] 
		self.__v_score = [0 for x in range(0, self.__field_size)] 
		self.__d_score = [0,0]


		# Fill game field
		self.__field = [['-' for i in range(0, self.__field_size)] 
							for j in range(0, self.__field_size)]
		self.__occupied_positions = [[0 for x in range(0, self.__field_size)] 
							for j in range(0, self.__field_size)]

	def render_field(self):
		for i in range(0, self.__field_size):
			for j in range(0, self.__field_size):
				print(self.__field[i][j], end=" ")
			print()

	
	def recalculate_field_score(self, player_move):
		# For calculating winning combination there are 3 variables:
		# h_score - horizaontal lines score, one value for each row in the field,
		# v_score - vertical lines score,
		# d_score - diagonal lines score.
		# After every move this scores are recalculated according to the following rules:
		# +1 for 'x', +2 for 'o', and therefore if there is 3 or 6 detected in the score
		# variables mentioned above, we have a winner ('x'-player or 'o'-player respectively).
		i = player_move[0]
		j = player_move[1]
		x_win_score = self.amount_to_win * self.__delta['x']
		o_win_score = self.amount_to_win * self.__delta['o']
		
		delta = self.__delta[self.__field[i][j]]

		if (i == j) and (i + j == self.__field_size-1):
		# If the current element is in the middle point, recalculate both d_scores
			self.__d_score[0] += delta
			self.__d_score[1] += delta
		elif (i == j):
		# If the current element is on the primary diagonal line, recalculate d_score[0]
			self.__d_score[0] += delta
		elif (i + j) == (self.__field_size-1):
		# If the current element is one the secondary diagonal line, recalculate d_score[1]
			self.__d_score[1] += delta
		
		self.__h_score[i] += delta
		self.__v_score[j] += delta
		
		# Detect if there is a winning combination
		for i in range(0, len(self.__h_score)):
			if( (self.__h_score[i] == x_win_score) or 
				(self.__h_score[i] == o_win_score) or 
				(self.__v_score[i] == x_win_score) or 
				(self.__v_score[i] == o_win_score) ):
				print('Winner!')
				return 1

		for i in range(0,2):
			if(self.__d_score[i] == x_win_score) or (self.__d_score[i] == o_win_score):
				print('Winner!')
				return 1
	

	def state(self):
		return self.__field


	def reward(self):
		return self.__reward

	
	def step(self, player_mark, player_move):
		# player_move is the coordinates list [x, y] where to place 'x' or 'o'
		# player_mark is 'o' or 'x'
		row, column = player_move[0], player_move[1]
		if(self.__occupied_positions[row][column] == 0):
			self.__field[row][column] = player_mark
			self.__occupied_positions[row][column] = 1
		else:
			print("This position is already occupuied!")
			return
		self.render_field()
		return self.recalculate_field_score(player_move)
				

	def start_game(self, player_1, player_2):
		if player_1 == 0 or player_2 == 0:
			is_human = 1
		

