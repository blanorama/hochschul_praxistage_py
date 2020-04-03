import unittest
from converter import convert


class RomanConverterTest(unittest.TestCase):

    def test_convert1(self):
        self.assertEqual('I', convert(1))

    def test_convert2(self):
        self.assertEqual('II', convert(2))

    def test_convert3(self):
        self.assertEqual('III', convert(3))

    def test_convert4(self):
        self.assertEqual('IV', convert(4))

    def test_convert5(self):
        self.assertEqual('V', convert(5))

    def test_convert8(self):
        self.assertEqual('VIII', convert(8))

    def test_convert9(self):
        self.assertEqual('IX', convert(9))

    def test_convert10(self):
        self.assertEqual('X', convert(10))

    def test_convert42(self):
        self.assertEqual('XLII', convert(42))

    # def test_convert2k18(self):
    #     self.assertEqual('MMXVIII', convert(2018), "The number 2018 should be converted to MMXVIII")


if __name__ == "__main__":
    unittest.main()
