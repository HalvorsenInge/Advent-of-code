import unittest
import day1

class TestParser(unittest.TestCase):

    def test_down(self):
        self.assertEqual(day1.parseInput(")"), -1)


if __name__ == "__main__":
    unittest.main()
