import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):
    def test1(self):
      actual = Triangle.classify(3, 3, 3)
      expected = Triangle.Type.EQUILATERAL
      self.assertEqual(actual, expected)
    
    def test2(self):
      actual = Triangle.classify(3, 4, 5)
      expected = Triangle.Type.SCALENE
      self.assertEqual(actual, expected)
    
    def test3(self):
      actual = Triangle.classify(2, 2, 3)
      expected = Triangle.Type.ISOSCELES
      self.assertEqual(actual, expected)

    def test4(self):
      actual = Triangle.classify(3, 2, 2)
      expected = Triangle.Type.ISOSCELES
      self.assertEqual(actual, expected)
    
    def test5(self):
      actual = Triangle.classify(2, 3, 2)
      expected = Triangle.Type.ISOSCELES
      self.assertEqual(actual, expected)
    
    def test6(self):
      actual = Triangle.classify(1, 2, 3)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)
    
    def test7(self):
      actual = Triangle.classify(0, 0, 0)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)

    def test8(self):
      actual = Triangle.classify(2, 2, 8)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)
    
    def test9(self):
      actual = Triangle.classify(5, 3, 9)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)
    
    def test10(self):
      actual = Triangle.classify(3, 4, 8)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)

    def test11(self):
      actual = Triangle.classify(-1, 4, 5)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(3, 4, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    # def test13(self):
    #     actual = Triangle.classify(11, 12, 13)
    #     expected = Triangle.Type.SCALENE
    #     self.assertEqual(actual, expected)
    # def test10(self):
    #   actual = Triangle.classify(1, 2, 3)
    #   expected = Triangle.Type.INVALID
    #   self.assertEqual(actual, expected)
if __name__ == '__main__':
  unittest.main()
