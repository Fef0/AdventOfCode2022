def get_path(raw_path):
	return "/".join(raw_path)

def c(lines):
	path = []
	dirs = {}
	for l in lines:
		chunks = l.split(" ")
		if chunks[0] != "$":
			if chunks[0].isdigit():
				# Update the whole path sizes backwards
				for i in range(len(path)):
					dirs[get_path(path[:i+1])] += int(chunks[0]) 
			continue
		
		# exclude ls
		if chunks[1] != "cd":
			continue
		
		# Visit dir
		if chunks[2] != "..":
			path.append(chunks[2])
			# init new path
			if get_path(path) not in dirs:
				dirs[get_path(path)] = 0
			continue
			
		# if .. then pop from current path
		path.pop()
	
	needed = 70000000 - 30000000
	print("Challenge 1:", sum(filter(lambda x: x <= 100000, list(dirs.values()))))
	print("Challenge 2:", min(filter(lambda x: dirs["/"] - x <= needed, list(dirs.values()))))
			
with open("input.txt", "r") as f:
	lines = list(map(lambda x: x.strip(), f.readlines()))
	c(lines)
