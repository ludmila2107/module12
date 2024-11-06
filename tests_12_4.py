import logging
import unittest
from rt_with_exceptions import Runner, Tournament

logging.basicConfig(
	level=logging.INFO,
	filename='runner_tests.log',
	filemode='w',
	encoding='utf-8',
	format='%(levelname)s:%(message)s'
)

class RunnerTest(unittest.TestCase):
	is_frozen = False
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_walk(self):
		try:
			obj_runner = Runner("ASt", speed=-5)
			for i in range(10):
				obj_runner.walk()
			self.assertEqual(obj_runner.distance, 50)
			logging.info('"test_walk" выполнен успешно')
		except ValueError:
			logging.warning("Неверная скорость для Runner")
			raise ValueError


	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_run(self):
		try:
			obj_runner2 = Runner("ASt2")
			for i in range(10):
				obj_runner2.run()
			self.assertEqual(obj_runner2.distance,100)
			logging.info('"test_run" выполнен успешно')
		except TypeError:
			logging.warning("Неверный тип данных для объекта Runner")
			raise TypeError

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_challenge(self):
		obj_runner3 = Runner("ASt3")
		obj_runner4 = Runner("ASt4")
		for i in range(10):
			obj_runner3.run()
			obj_runner4.walk()
		self.assertNotEqual(obj_runner3.distance, obj_runner4.distance)
