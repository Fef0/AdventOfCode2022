# A,X = Rock, B,Y = Paper, C,Z = Scissors
win_rules_LUT = {
	"A": "Z", # rock defeats scissors 
	"B": "X", # paper defeats rock
	"C": "Y"  # scissors defeats paper
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
		opponent, me = list(map((lambda x: x.strip()), l.split(" ")))
		# Defeat, 0 points
		if me == win_rules_LUT[opponent]:
			# Update with shape points only
			score += points_LUT[me]
		# Draw, 3 points
		elif me == identity(opponent):
			score += points_LUT[me] + 3
		# Win, 6 points
		else:
			score += points_LUT[me] + 6
print("Score:", score)
