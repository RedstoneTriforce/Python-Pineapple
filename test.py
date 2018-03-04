import os

input = str.lower(raw_input(u"\u001b[31mUser:\n\u001b[0m"))
inp = input.split()
h1 = ("hi")
h2 = ("hello")
hay1 = ("how")
hay2 = ("are")
j = ("joke")
s = ("stop")
l = ("list")

if h1 in inp or h2 in inp:
	print("Hi")
	os.system('mpg321 1.mp3')
	execfile('test.py')
elif hay1 and hay2 in inp:
	print("Good and u?")
	execfile('good.py')
elif l in inp:
	print(u"\u001b[34mList:\u001b[31m\nHello\nHow are u?\nstop\u001b[34m\n==========\u001b[0m")
	execfile('test.py')
elif j in inp:
	execfile('joke.py')
elif s in inp:
	print("Bye-bye")
else:
	print("That isn't in my Database!")
	execfile('test.py')
