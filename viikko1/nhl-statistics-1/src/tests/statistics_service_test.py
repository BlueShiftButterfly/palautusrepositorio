import unittest
from statistics_service import StatisticsService
from player import Player

class TestPlayerList:
    playerlist = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class PlayerReaderStub:
    def get_players(self):
        return TestPlayerList().playerlist

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing(self):
        target_name = "Semenko"
        player = self.stats.search(target_name)
        self.assertEqual(target_name, player.name)

    def test_search_nonexisting(self):
        target_name = "Johnson"
        player = self.stats.search(target_name)
        self.assertEqual(None, player)

    def test_get_players_by_team(self):
        team_name = "EDM"
        target_player_list = [TestPlayerList().playerlist[0], TestPlayerList().playerlist[2], TestPlayerList().playerlist[4]]
        self.assertEqual(target_player_list, self.stats.team(team_name))

    def test_get_players_by_nonexistent_team(self):
        team_name = "VAN"
        self.assertEqual([], self.stats.team(team_name))

    def test_get_top_players(self):
        # Palautettu määrä on yhden enemmän kuin odotettu?
        player_list = self.stats.top(1)
        target_player_list = [TestPlayerList().playerlist[4], TestPlayerList().playerlist[1]]
        self.assertEqual(target_player_list, player_list)
