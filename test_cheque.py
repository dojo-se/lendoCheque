import unittest

import cheque

class TestCheque(unittest.TestCase):
	def test_1(self):
		self.assertEqual(cheque.ler_cheque('um'), 1)
