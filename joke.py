import random as r
import os

jokes = ('1', '2', '3',)
joke = r.choice(jokes)

if joke == "1":
	execfile('joke1.py')
elif joke == "2":
	execfile('joke2.py')
elif joke == "3":
	execfile('joke3.py')

