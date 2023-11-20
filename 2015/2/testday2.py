import unittest
import day2

class TestDay2(unittest.TestCase):
    def test_parseInput_with_valid_input(self):
        self.assertEqual(day2.calculatePaper(['2', '3', '4']), 58)

    def test_ribbon_length(self):
        self.assertEqual(day2.calculateRibbon(['4','2','3']), 34)

if __name__ == "__main__":
    unittest.main()