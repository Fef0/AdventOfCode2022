def c1(text):
	for i in range(len(text)):
		if len(set(text[i:i+4])) == 4:
			print("challenge 1:", i+4)
			return

def c2(text):
	for i in range(len(text)):
		if len(set(text[i:i+14])) == 14:
			print("challenge 2:", i+14)
			return
			
with open("input.txt", "r") as f:
	text = f.read()
	c1(text)
	c2(text)
