'''
TO PRINT THE NAMES AS (PLAYER NAME,SCORE). PRINT ACCORDING TO SCORE.IF SCORE OF PLAYERS IS SAME THEN ASCEND ACCORDING TO ALPHABETICAL NAME ORDER.
'''
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
