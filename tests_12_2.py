import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


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
