import unittest
def add(a,b):
    return a+b


class testadd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEquals(add(3,5),8)
    def test_add_negative_numbers(self):
        self.assertEquals(add(-7,-3),-10)
    def test_add_zero(self):
        self.assertEquals(add(0,5),5)

if __name__== '__main__':
    unittest.main()