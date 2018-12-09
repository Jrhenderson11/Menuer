import os
from collections import OrderedDict

class Menu():

	menu_items = {}
	asciiart = ""

	def __init__(self, asciiart, menu_items):
		if not isinstance(menu_items, OrderedDict):
			raise Exception("menu_items is not an OrderedDictionary")
		self.asciiart = asciiart
		self.menu_items = menu_items

	def printgreen(self, text):
		print('\033[92m' + text + '\033[0m')

	def printred(self, text):
		print('\033[31m' + text + '\033[0m')

	def print_intro(self):
		print(self.asciiart)
		
	def print_menu_items(self):
		for i, s in enumerate(list(self.menu_items.keys())):
			print(" [{}] {}".format(i+1, s))
		print("")

	def menu_loop(self):
		os.system("clear")
		print('\033[2J')
		print('\033[s')
		self.print_intro()
		print("\n"	)
		self.print_menu_items()
		num = int(input())
		while not (num>0 and num<len(self.menu_items)+1):
			print('\033[u')
			self.print_intro()
			print("	   \033[31m\033[1m  invalid input \033[0m\n")
			self.print_menu_items()
			num = int(input('\033[K'))
		num-=1
		list(self.menu_items.values())[num]()

