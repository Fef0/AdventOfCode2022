# A,X = Rock, B,Y = Paper, C,Z = Scissors
opponent_win_rules_LUT = {
	"A": "Z", # rock defeats scissors 
	"B": "X", # paper defeats rock
	"C": "Y"  # scissors defeats paper
}

my_win_rules_LUT = {
	"A": "Y", # rock gets defeated by paper 
	"B": "Z", # paper gets defeated by scissors
	"C": "X"  # scissors gets defeated by rock
}

points_LUT = {
	"X": 1, # rock
	"Y": 2, # paper
	"Z": 3  # scissors
}

def identity(opponent):
	# Use ASCII decimal distance
	return chr(ord(opponent)+23)

score = 0
with open("input.txt", "r") as f:
	lines = f.readlines()
	for l in lines:
		# Apply strip() to each line splitting element	
		opponent, outcome = list(map((lambda x: x.strip()), l.split(" ")))
		print(opponent, outcome)
		# Defeat (opponent wins), 0 points
		if outcome == "X":
			score += points_LUT[opponent_win_rules_LUT[opponent]]
		# Draw, 3 points
		elif outcome == "Y":
			# Update with opponent shape points + 3
			score += points_LUT[identity(opponent)] + 3
		# Win (I win), 6 points
		else:
			# Retrieve winning move points from win rules and add 6
			score += points_LUT[my_win_rules_LUT[opponent]] + 6

print("Score:", score)
