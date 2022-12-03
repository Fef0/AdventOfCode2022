def c1(lines):
	common_char_priorities = []
	for l in lines:
		half1 = l[:int(len(l)/2)]
		half2 = l[int(len(l)/2):]
		for c in half1:
			if c in half2:
				# ord(a) = 97 -> priority(a) = 97-96 = 1
				# ord(A) = 65 -> priority(A) = 65-38 = 27
				common_char_priorities.append(ord(c)-96 if ord(c) > 96 else ord(c)-38)
				break
	print("challenge1:", sum(common_char_priorities))

def c2(lines):
	common_badge_priorities = []
	for i in range(0, len(lines), 3):
		for c in lines[i]:
			if c in lines[i+1] and c in lines[i+2]:
				common_badge_priorities.append(ord(c)-96 if ord(c) > 96 else ord(c)-38) 
				break
	
	print("challenge2:", sum(common_badge_priorities))
	
with open("input.txt", "r") as f:
	lines = f.readlines()
	c1(lines)
	c2(lines)

