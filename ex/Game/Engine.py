# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Scene import *
from Map import *
class Engine(object):
	"""docstring for Engine"""
	def __init__(self, Scene_map):
		self.Scene_map = Scene_map
		#foo()
	def play(self):
		current_scene = self.Scene_map.opening_scene()
		while True:
			next_scene_name = current_scene.enter()
			current_scene = self.Scene_map.next_scene(next_scene_name)
start_map = Map('central_corridor')
start_game = Engine(start_map)
start_game.play()