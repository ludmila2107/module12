import unittest
from module_12_1 import RunnerTest
from tests_12_2 import TournamentTest

# Создаем объект TestSuite и добавляем туда тесты
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

if __name__ == "__main__":
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(test_suite)