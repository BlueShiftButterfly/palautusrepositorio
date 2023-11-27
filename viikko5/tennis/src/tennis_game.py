from player import Player

class TennisGame:
    def __init__(self, p1name, p2name):
        self.player1 = Player(p1name)
        self.player2 = Player(p2name)

        self._score_zero_name = "Love"
        self._score_one_name = "Fifteen"
        self._score_two_name = "Thirty"
        self._score_three_name = "Forty"

        self._score_tie_deuce_name = "Deuce"

        self._tie_subname = "All"

        self._minimum_win_score = 4
        self._minimum_win_score_offset = 2
        self._minimum_advantage_score = 3
        self._minimum_deuce_score = 3

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.add_score_point()
        else:
            self.player2.add_score_point()

    def _get_opponent(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def _get_players_score_difference(self):
        return abs(self.player1.score - self.player2.score)

    def _get_score_subname(self, score):
        if score == 0:
            return self._score_zero_name
        elif score == 1:
            return self._score_one_name
        elif score == 2:
            return self._score_two_name
        else:
            return self._score_three_name

    def _player_has_advantage(self, player):
        return player.score >= self._minimum_win_score and self._get_opponent(player).score < player.score and self._get_players_score_difference() == self._minimum_win_score_offset - 1

    def _has_player_won(self, player):
        return player.score >= self._minimum_win_score and self._get_opponent(player).score < player.score and self._get_players_score_difference() >= self._minimum_win_score_offset

    def get_score(self):
        if self._get_players_score_difference() == 0:
            score_message = self._get_score_subname(self.player1.score) + "-" + self._tie_subname
            if self.player1.score >= self._minimum_deuce_score:
                score_message = "" + self._score_tie_deuce_name
            return score_message

        for p in [self.player1, self.player2]:
            if self._has_player_won(p):
                return f"Win for {p.name}"
            elif self._player_has_advantage(p):
                return f"Advantage {p.name}"

        score_message = self._get_score_subname(self.player1.score) + "-" + self._get_score_subname(self.player2.score)                 

        return score_message
