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

    def test13(self):
      invalid = Triangle.classify(-3, -2, -4)
      scalene = Triangle.classify(3, 4, 5)
      equilateral = Triangle.classify(3, 3, 3)
      isosceles = Triangle.classify(3, 3, 4)
      self.assertEqual(invalid.value, 0)
      self.assertEqual(scalene.value, 1)
      self.assertEqual(equilateral.value, 2)
      self.assertEqual(isosceles.value, 3)

    def test14(self):
      actual = Triangle.classify(1, 1, 1)
      expected = Triangle.Type.EQUILATERAL
      self.assertEqual(actual, expected)

    def test15(self):
      actual1 = Triangle.classify(2, 2, 4)
      actual2 = Triangle.classify(4, 2, 2)
      actual3 = Triangle.classify(2, 4, 2)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual1, expected)
      self.assertEqual(actual2, expected)
      self.assertEqual(actual3, expected)

    def test16(self):
      actual = Triangle.classify(5, 5, 0)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual, expected)
    
    def test17(self):
      actual1 = Triangle.classify(5, 3, 2)
      actual2 = Triangle.classify(3, 5, 2)
      expected = Triangle.Type.INVALID
      self.assertEqual(actual1, expected)
      self.assertEqual(actual2, expected)
if __name__ == '__main__':
  unittest.main()
