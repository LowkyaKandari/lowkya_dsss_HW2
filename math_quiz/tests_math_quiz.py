import unittest
from math_quiz import random_integer, random_operator, problem_solution


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        operators = {'+', '-', '*'}
        rand_operator = random_operator()
        self.assertIn(rand_operator, operators)

    def test_problem_solution(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8,5, '-', '8 - 5', 3),
                (2,3, '*', '2 * 3', 6),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = problem_solution(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
