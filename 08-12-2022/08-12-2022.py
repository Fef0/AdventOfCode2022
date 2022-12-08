def c1(lines):
	visible = 2 * (len(lines[0]) + len(lines) - 2)
	inner_grid = []
	# consider the inner grid only
	for l_i, l in enumerate(lines[1:-1], start=1):
		inner_grid.append([])
		# check nth-line of trees in inner grid
		for t, c in enumerate(l[1:-1], start=1):
			inner_grid[l_i-1].insert(t-1, 0)
			tree_h = int(c)
			
			# check top->bottom (not efficient but whatever)
			# If all the trees in front of current tree are shorter
			if all(tree_h > int(lines[x][t]) for x in range(l_i)):
				inner_grid[l_i-1][t-1] += 1
			# check bottom->top
			elif all(tree_h > int(lines[x+l_i+1][t]) for x in range(len(lines[l_i+1:]))[::-1]):
				inner_grid[l_i-1][t-1] += 1
			# check left->right
			elif all(tree_h > int(lines[l_i][x]) for x in range(t)):
				inner_grid[l_i-1][t-1] += 1
			# check right->left
			elif all(tree_h > int(lines[l_i][x+t+1]) for x in range(len(l[t+1:]))):
				inner_grid[l_i-1][t-1] += 1
			
	# update visible trees total num	
	for line in inner_grid:
		for tree_status in line:
			visible += tree_status
	
	print("Challenge 1:", visible)
	
def c2(lines):
	pass

	
	print("Challenge 2:")

with open("input.txt", "r") as f:
	lines = list(map(lambda x: x.strip(), f.readlines()))
	c1(lines)
	c2(lines)
