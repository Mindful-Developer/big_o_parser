import unittest
from optimization_tools.big_o import complexity


# test time complexity
class TestComplexity(unittest.TestCase):
    def setUp(self):
        @complexity
        def constant_algo_1(items):
            total = items[0] * items[0]
            return total

        @complexity
        def linear_algo_1(items):
            total = 0
            for item in items:
                total += item
            return total

        @complexity
        def linear_algo_2(items):
            total = 0
            for item in items:
                total += item
            for item in items:
                total += item
            return total

        @complexity
        def quadratic_algo_1(items):
            total = 0
            for item in items:
                for item2 in items:
                    total += item + item2
            return total

        @complexity
        def cubic_algo_1(items):
            total = 0
            for item in items:
                for item2 in items:
                    for item3 in items:
                        total += item + item2 + item3
            return total


        @complexity
        def exponential_algo_1(num):
            if (num <= 1):
                return num
            return exponential_algo_1(num - 2) + exponential_algo_1(num - 1)

        @complexity
        def logarithmic_algo_1(items):
            for index in range(0, len(items), 3):
                print(items[index])

        @complexity
        def logarithmic_algo_2(items, target):
            left = 0
            right = len(items) - 1
            while (left <= right):
                mid = (left + right) / 2
                if (items(mid) == target):
                    return mid
                elif (items(mid) < target):
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        @complexity
        def log_linear_algo_1(items):
            pass

        @complexity
        def factorial_algo_1(data, n):
            if n == 1:
                print(data)
                return

            for i in range(n):
                factorial_algo_1(data, n - 1)
                if n % 2 == 0:
                    data[i], data[n - 1] = data[n - 1], data[i]
                else:
                    data[0], data[n - 1] = data[n - 1], data[0]


        self.constant_1 = constant_algo_1
        self.linear_1 = linear_algo_1
        self.linear_2 = linear_algo_2
        self.quadratic_1 = quadratic_algo_1
        self.cubic_1 = cubic_algo_1
        self.exponential_1 = exponential_algo_1
        self.logarithmic_1 = logarithmic_algo_1
        self.logarithmic_2 = logarithmic_algo_2
        self.log_linear_1 = log_linear_algo_1
        self.factorial_1 = factorial_algo_1

        self.item_list = [4, 5, 6, 8]
        
    def test_constant_algo_1(self):
        self.assertEqual('O(1)', self.constant_1(self.item_list))

    def test_linear_algo_1(self):
        self.assertEqual('O(n)', self.linear_1(self.item_list))

    def test_linear_algo_2(self):
        self.assertEqual('O(n)', self.linear_2(self.item_list))

    def test_quadratic_algo_1(self):
        self.assertEqual('O(n^2)', self.quadratic_1(self.item_list))

    def test_cubic_algo_1(self):
        self.assertEqual('O(n^3)', self.cubic_1(self.item_list))

    def test_exponential_algo_1(self):
        self.assertEqual('O(2^n)', self.exponential_1(self.item_list[-1]))

    def test_logarithmic_algo_1(self):
        self.assertEqual('O(log(n))', self.logarithmic_1(self.item_list))

    def test_logarithmic_algo_2(self):
        self.assertEqual('O(log(n))', self.logarithmic_2(self.item_list, 8))

    def test_log_linear_algo_1(self):
        self.assertEqual('O(nlog(n))', self.log_linear_1(self.item_list))

    def test_factorial_algo_1(self):
        self.assertEqual('O(n!)', self.factorial_1(self.item_list, len(self.item_list)))

if __name__ == '__main__':
    unittest.main()
