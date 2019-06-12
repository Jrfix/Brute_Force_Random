#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
sys.setrecursionlimit(2147000000)
from os import system
from time import sleep
import time
import random as r

os.system("clear")

chars = ["0","1","2","3","4","5","6","7","8","9",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","Q","W"]
attempts = []


password = "PJUHVTXY4M36"


len_pass = len(password)
print("password lenght: " + str(len_pass) + "\n\n")
sleep(2)

def found():
	"SUCCESSED"
	raw_input("\nenter to exit..")
	quit()


def random():
	sleep(0.001)
	try:
	
		word = "" 
		for i in range(0,len_pass):
			random_char = (r.randint(0,len(chars)-1 ) ) 

			word += chars[random_char]
		
		if word in attempts:
			print("var: " + word)
			random()

		if password == word:
			print("password found: " + word)
			found()

		else:
			attempts.append(word)
			print(word)
			random()
	except Exception,e:
		print("\n\nERROR: " + str(e))
	
	




random()
