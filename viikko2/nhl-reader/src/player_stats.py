from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, player_reader : PlayerReader) -> None:
        self._players = player_reader.players.copy()
    
    def _by_player_score(self, player): 
        return player.points

    def top_scorers_by_nationality(self, nationality):
        tsn = []
        for player in self._players:
            if player.nationality == nationality:
                tsn.append(player)
        tsn.sort(key=self._by_player_score, reverse=True)
        return tsn    