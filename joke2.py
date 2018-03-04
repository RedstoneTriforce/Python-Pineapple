print("How do you get a pikachu on the Bus?")
poke = ("u poke em on", "u", "U")
inp = raw_input("HOW?\n")

if any(inp.find(s)>=0 for s in poke):
	print("How did u know?")
	execfile('test.py')
else:
        print("U poke em on!!!\nHAHAHA")
	execfile('test.py')
 
