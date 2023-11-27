class Player:
    def __init__(self, name : str) -> None:
        self._score : int = 0
        self._name = name
    
    def add_score_point(self):
        self._score += 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score