import unittest
from suma import sumar
from resta import restar
from multi import multiply
from div import division

class TestSumar(unittest.TestCase):
 def test_operator(self):
    self.assertEqual(sumar(4, 2), 6)
    self.assertEqual(sumar(-1, 1), 0)
    self.assertEqual(sumar(-1, -1), -2)
    self.assertEqual(sumar(-1, 0), -1)

class TestRestar(unittest.TestCase):
 def test_operator(self):
    self.assertEqual(restar(4, 2), 2)
    self.assertEqual(restar(-1, 1), -2)
    self.assertEqual(restar(-1, -1), 0)
    self.assertEqual(restar(-1, 0), -1)
    self.assertEqual(restar(3, 3), 0)

class TestMultiply(unittest.TestCase):
 def test_operator(self):
    self.assertEqual(multiply(4, 2), 8)
    self.assertEqual(multiply(-1, 3), -3)
    self.assertEqual(multiply(-1, -1), 1)
    self.assertEqual(multiply(-1, 0), 0)

class TestDiv(unittest.TestCase):
 def test_operator(self):
    self.assertEqual(division(4, 2), 2)
    self.assertEqual(division(-1, 3), -1/3)
    self.assertEqual(division(-1, -1), 1)
    self.assertEqual(division(2, 0), None)

if __name__ == '__main__':
 unittest.main()