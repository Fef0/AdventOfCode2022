import copy

def c(lines):
	# Get stacks_c1 dimensions
	dim = len([lines[0][i:i+4].strip() for i in range(0, len(lines[0]), 4)])
	stacks_c1 = [[] for i in range(dim)]
	# Load stacks_c1
	for cont, l in enumerate(lines):
		if l == "\n":
			break
		chunks = [l[i:i+4].strip() for i in range(0, len(l), 4)]
		for i in range(dim):
			if chunks[i] != "":
				stacks_c1[i].append(chunks[i])
	# Clean stack from last element (numbers)
	# I'm pretty sure there's a more clever way to do this
	stacks_c1 = [s[:-1] for s in stacks_c1]
	stacks_c2 = copy.deepcopy(stacks_c1)
	# Exec moves
	for l in lines[cont+1:]:
		_, j, _, src, _, dst = l.strip().split(" ")
		for i in range(int(j)):
			stacks_c1[int(dst)-1].insert(0, stacks_c1[int(src)-1].pop(0))
			stacks_c2[int(dst)-1].insert(0, stacks_c2[int(src)-1].pop(int(j)-i-1))
			
	
	print("challenge 1:", "".join([s[0][1:2] for s in stacks_c1]))
	print("challenge 2:", "".join([s[0][1:2] for s in stacks_c2]))

with open("input.txt", "r") as f:
	lines = f.readlines()
	c(lines)
