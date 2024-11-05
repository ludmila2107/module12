import unittest
from runner_and_tournament import Runner, Tournament
class TournamentTest(unittest.TestCase):
	all_results = {}

	@classmethod
	def setUpClass(cls):
		cls.all_results = {}

	def setUp(self):
		self.runner1 = Runner("Usain", 10)
		self.runner2 = Runner("Andrey", 9)
		self.runner3 = Runner("Nik", 3)

	@classmethod
	def tearDownClass(cls):
		for place, runner in sorted(cls.all_results.items()):
			print(f"Place {place}: {runner}")

	def test_race_usain_nik(self):
		tournament = Tournament(90, self.runner1, self.runner3)
		results = tournament.start()
		self.all_results.update(results)
		self.assertTrue(self.all_results[max(self.all_results)] == "Nik")

	def test_race_andrey_nik(self):
		tournament = Tournament(90, self.runner2, self.runner3)
		results = tournament.start()
		self.all_results.update(results)
		self.assertTrue(self.all_results[max(self.all_results)] == "Nik")

	def test_race_usain_andrey_nik(self):
		tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
		results = tournament.start()
		self.all_results.update(results)
		self.assertTrue(self.all_results[max(self.all_results)] == "Nik")



if __name__ == "__main__":
	unittest.main()
