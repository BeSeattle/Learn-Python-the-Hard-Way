# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Scene import *
#Map
class Map(object):
	"""docstring for Map"""
	Scene = {
	'central_corridor':CentralCorridor(),
	'death':Death(),
	'laser_weapon_armory':LaserWeaponArmory(),
	'the_bridge':TheBridge(),
	'escape_pod':EscapePod()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self,scene_name):
		return Map.Scene.get(scene_name)			

	def opening_scene(self):
		return self.next_scene(self.start_scene)