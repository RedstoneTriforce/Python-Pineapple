input = str.lower(raw_input(u"\u001b[34mUser:\n\u001b[0m"))
inp = input.split()
g = ("good")
b = ("bad")
w = ("why")
l = ("list")

if g in inp:
	print("That's Bad!")
	execfile('good.py')
elif b in inp:
	print("That's Good!")
	execfile('good.py')
elif w in inp:
	print("Cause I'm BATMAN!!!")
	execfile('test.py')
elif w in inp:
	print(u"\u001b[34mList:\u001b[31m\ngood\nbad\nwhy?\u001b[34m\n==========\u001b[0m")
	execfile('good.py')
else:
	print("Please repeat!")
	execfile('test.py')

