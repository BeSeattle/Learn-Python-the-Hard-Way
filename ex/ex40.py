# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self,lyrics):
		for line in lyrics:
			print line
		for line in self.lyrics:
			print line
happy_bday = song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
						"With pockets full of shells"])
#happy_bday.sing_me_a_song()
#bulls_on_parade.sing_me_a_song()
song('qwe').sing_me_a_song('31231')