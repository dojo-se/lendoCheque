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

	def test_22(self):
		self.assertEqual(cheque.ler_cheque('vinte e dois reais'), 22)

	def test_23(self):
		self.assertEqual(cheque.ler_cheque('vinte e tres reais'), 23)

	def test_24(self):
		self.assertEqual(cheque.ler_cheque('vinte e quatro reais'), 24)

	def test_120(self):
		self.assertEqual(cheque.ler_cheque('cento e vinte reais'), 120)

	def test_100(self):
		self.assertEqual(cheque.ler_cheque('cem reais'), 100)

	def test_125(self):
		self.assertEqual(cheque.ler_cheque('cento e vinte e cinco reais'), 125)		

	# ['vinte', 'e', 'um']

	#def test_1_1(self):
	#	self.assertEqual(cheque.ler_cheque('um real e um centavo'), 1.1)
