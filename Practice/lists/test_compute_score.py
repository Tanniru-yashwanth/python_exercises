from unittest import TestCase
from compute_score import compute_score


class TestCompute(TestCase):
    def test_score(self):
        total_score = compute_score(["5", "2", "C", "D", "+"])
        self.assertEqual(total_score, 30)

    def test_second(self):
        total = compute_score(["5", "-2", "4", "C", "D", "9", "+", "+"])
        self.assertEqual(total, 27)

    def test_third(self):
        total_third = compute_score(["1"])
        self.assertEqual(total_third, 1)

