import unittest
import day2

class TestDay2(unittest.TestCase):
    def test_parseInput_with_valid_input(self):
        self.assertEqual(day2.parseInput("2x3x4"), 58)

if __name__ == "__main__":
    unittest.main()