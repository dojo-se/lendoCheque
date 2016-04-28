import unittest

import cheque

class TestCheque(unittest.TestCase):
	def test_1(self):
		self.assertEqual(cheque.ler_cheque('um real'), 1)
	def test_2(self):
		self.assertEqual(cheque.ler_cheque('dois reais'), 2)
	#def test_1_1(self):
	#	self.assertEqual(cheque.ler_cheque('um real e um centavo'), 1.1)