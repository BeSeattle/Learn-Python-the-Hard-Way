# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import exit
from random import randint
#Scene				
class Scene(object):
	"""docstring for Scene"""
	def enter(self):
		print ("This is not yet configured. Subclass it and implement enter()")
		exit(1)
class Death(Scene):
	"""docstring for Death"""
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would proud...if she were smarter.",
		"Such a loser.",
		"I have a small puppy that's better at this."	
		]
	def enter(self):
		print (Death.quips[randint(0,len(Death.quips)-1)])#?????????
		exit(1)

class CentralCorridor(Scene):
	"""docstring for CentralCorridor"""
	def enter(self):
		for x in range(1,4):	
			print ("""----------------	
The Alien have invaded your ship and destroyed your entire crew.
You are the last surviving member and your last mission is to get 
the neutron bomb from the Weapons Armory,put it in the bridge,and
blow the ship up after getting into an escape pod.
You're running down the Central Corridor to the Weapons Armory when
a Alien out,red scale skin,dark grimy teeth,and evil clown costume
flowing around this hate filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you.
\nNow,you have two option:
	1.shoot
	2.tell a joke
		""")
			action = input("> ")
			if action == "shoot":
				return Death().enter()
			elif action == 'tell a joke':
				print ("DOSE NOT COMPUTE!")
				return 'laser_weapon_armory'
		print ("Too much mistake options!!!")
		return 'death'

class LaserWeaponArmory(Scene):
	"""docstring for LaserWeaponArmory"""
	def enter(self):
		print ("Now you need the code to get the bomb out.")
		print ("The code is 3 digits.")
		code = "%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
		guess = input("[keypad]>")
		guesses = 6

		while code != guess:
			print ("Wrong code,BZZZZEDDD!")
			guesses = guesses - 1
			if guess == "hint":
				print ("Give you a hint.The code is %s"%(code))
				guess = input("[keypad]> ")
				if code == guess:
					return 'escape_pod'
			elif guesses == 0:
				return 'death'
			print ("Only %d times can try!!!"%(guesses))
			guess = input("[keypad]>")
		
		else:
			return 'escape_pod'
	
class TheBridge(Scene):
	"""docstring for TheBridge"""
	def enter(self):
		pass

class EscapePod(Scene):
	"""docstring for EscapePod"""
	def enter(self):
		print ("There is 5 pods,which one do you take?")
		good_pod = str(randint(1,5))
		guess = input("[pod #]> ")	
		while guess != good_pod:

			if guess == "hint":
				print ("Give you a hint.The code is %s"%(good_pod))
				guess = input("[pod #]> ")
				if guess == good_pod:	
					print ("You won,my hero!!!")
					exit()
			else:
				return 'death'