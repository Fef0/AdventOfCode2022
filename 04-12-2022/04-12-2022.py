def c1(lines):
	tot = 0
	for l in lines:
		tmp = l.split(",")
		pair1 = list(map(lambda x: int(x), tmp[0].split("-")))
		pair2 = list(map(lambda x: int(x.strip()), tmp[1].split("-")))
		if (pair1[0] <= pair2[0] and pair2[1] <= pair1[1]) or (pair2[0] <= pair1[0] and pair1[1] <= pair2[1]):
			tot+=1
	print("challenge 1:",tot)
			

def c2(lines):
	tot = 0
	for l in lines:
		tmp = l.split(",")
		pair1 = list(map(lambda x: int(x), tmp[0].split("-")))
		pair2 = list(map(lambda x: int(x.strip()), tmp[1].split("-")))
		if (pair2[0] <= pair1[0] <= pair2[1] or pair2[0] <= pair1[1] <= pair2[1] or pair1[0] <= pair2[0] <= pair1[1] or pair1[0] <= pair2[1] <= pair1[1]):
			tot += 1 
	print("challenge 2:", tot)
	
with open("input.txt", "r") as f:
	lines = f.readlines()
	c1(lines)
	c2(lines)

