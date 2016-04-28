import unittest

import cheque

class TestCheque(unittest.TestCase):
	def test_1(self):
		self.assertEqual(cheque.ler_cheque('um real'), 1)

	def test_2(self):
		self.assertEqual(cheque.ler_cheque('dois reais'), 2)

	def test_13(self):
		self.assertEqual(cheque.ler_cheque('treze reais'), 13)

	def test_15(self):
		self.assertEqual(cheque.ler_cheque('quinze reais'), 15)
		
	def test_21(self):
		self.assertEqual(cheque.ler_cheque('vinte e um reais'), 21)

	# ['vinte', 'e', 'um']
	
	#def test_1_1(self):
	#	self.assertEqual(cheque.ler_cheque('um real e um centavo'), 1.1)
