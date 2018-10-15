#!/usr/local/bin/python3.7
# -*- coding: cp1252 -*-
# Module de teste
from unittest import TestCase
# Module a tester
import mowers

# Teste de la classe field
class TestField(TestCase):
	# Teste de l'initialisation des attributs d une nouvelle instance field
	def test_init_field(self):
		self.terrain = mowers.field([2,3])
		self.assertEqual([ self.terrain.min_x , 
							self.terrain.min_y , 
							self.terrain.max_x , 
							self.terrain.max_y ] , 
							[ 0 , 0 , 2 , 3 ])

# Teste de la classe mower
class TestMower(TestCase):
	# Initialisation des variables necessaires aux tests
	def setUp(self):
		self.terrain = mowers.field([5,5])
		self.num = 0
		# Instanciation d une tondeuse
		self.tondeuse = mowers.mower(self.terrain, self.num, ['1','2','N'])

	# Teste de l'initialisation des attributs d une nouvelle instance mower
	def test_init_mower(self):
		self.assertEqual([ self.tondeuse.num , 
							self.tondeuse.posX , 
							self.tondeuse.posY , 
							self.tondeuse.posA ] , 
							[ 0 , 1 , 2 , 'N' ])

	# Teste de la fonction de mouvement 
	def test_move_mower(self):
		# Initialisation de la variable contenant les donnees de mouvement
		strControl ='GAGAGAGAA'
		# Lecture du string d instructions de mouvements de la tondeuse
		for ch in strControl:
			# Instruction de mouvement
			self.tondeuse.moveMower(ch)
		# Teste de la position finale
		self.assertEqual([ self.tondeuse.num , 
							self.tondeuse.posX , 
							self.tondeuse.posY , 
							self.tondeuse.posA ] , 
							[ 0 , 1 , 3 , 'N' ])
