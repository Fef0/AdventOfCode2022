max = 0
subset = []
subsets_sums = []
with open("input.txt", "r") as f:
	lines = f.readlines()
	for l in lines:
		if l == "\n":
			s = sum(subset)
			if s > max:
				# challenge 1
				max = s
			# challenge 2
			subsets_sums.append(s)
			subset = []
		else:
			subset.append(int(l.strip()))
	
	subsets_sums.sort()
	print("challenge 1:", max)
	print("challenge 2:", sum(subsets_sums[-3:]))
