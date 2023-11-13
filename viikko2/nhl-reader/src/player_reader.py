import requests
from player import Player

class PlayerReader():
    def __init__(self, url : str) -> None:
        self.players : list = self._get_players(url)

    def _get_players(self, url : str):
        response = requests.get(url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players