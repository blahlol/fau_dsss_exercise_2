import unittest
from math_quiz import generate_random_integer, perform_math_operation, random_math_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_math_operation(self):
        for _ in range(100):
            math_operation = random_math_operation()
            self.assertTrue(math_operation in ['+', '-', '*'])

    def test_perform_math_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, -1, '-', '2 - -1', 3),
                (10, 2, '*', '10 * 2', 20)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = perform_math_operation(num1, num2, operator)
                self.assertTrue(problem == expected_problem)
                self.assertTrue(answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
