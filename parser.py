import os
import sys
import re

# PDF reader and writer
from PyPDF2 import PdfReader as pfr

# color for terminal
from colorama import init
init()

from colorama import Fore, Back, Style
# Fore.GREEN Back.YELLOW Style.BRIGHT
# Style.RESET_ALL

# цвет текста
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

# цвет фона
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

# яркость текста и общий сброс
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


my_text = input("nima izlaysiz: ").lower()

dir_name = 'pdf'

# get paths all pdf files
paths = os.listdir(dir_name)

print(*paths, sep="\n")

for path in paths:
	print("="*70)
	print("file name: ", path)
	print("="*70)
	
	# open pdf
	with open(dir_name+"/"+path, "rb") as file:
		pf = pfr(file)
		
		for num in range(len(pf.pages)):
			# get page
			page = pf.pages[num]
			
			# get text
			txt = page.extract_text()
			
			# find my text in the page
			if my_text in txt:
				print("+"*70)
				txt = txt.replace(my_text, Back.YELLOW+my_text+Style.RESET_ALL)
				print(txt)
				print("-"*70)
				print("path:", dir_name+"/"+path)
				print("page num:", num)
				input("enter:")
			
		print("pages: ", len(pf.pages))
		
	print()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	