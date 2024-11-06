import unittest
import runner

class RunnerTest(unittest.TestCase):
	is_frozen = False
	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_walk(self):
		obj_runner = runner.Runner("ASt")
		for i in range(10):
			obj_runner.walk()
		self.assertEqual(obj_runner.distance,50)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_run(self):
		obj_runner2 = runner.Runner("ASt2")
		for i in range(10):
			obj_runner2.run()
		self.assertEqual(obj_runner2.distance,100)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_challenge(self):
		obj_runner3 = runner.Runner("ASt3")
		obj_runner4 = runner.Runner("ASt4")
		for i in range(10):
			obj_runner3.run()
			obj_runner4.walk()
		self.assertNotEqual(obj_runner3.distance, obj_runner4.distance)





#test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
# Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции
# должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.