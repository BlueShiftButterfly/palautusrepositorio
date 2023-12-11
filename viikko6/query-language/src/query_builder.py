from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, query=All()) -> None:
        self.query_matcher = query
    
    def playsIn(self, team):
        return QueryBuilder(And(self.query_matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_matcher, HasFewerThan(value, attr)))

    def oneOf(self):
        pass

    def build(self):
        return self.query_matcher