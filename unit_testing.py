import unittest
import next_clock


class TestClockProblem(unittest.TestCase):

    def test_next_clock(self):
        self.assertEqual(next_clock.next_clock('00:00'), '00:00')
        self.assertEqual(next_clock.next_clock('23:59'), '22:21')


if __name__ == "__main__":
    unittest.main()
