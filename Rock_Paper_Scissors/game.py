import pickle


class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.id = id
        self.move = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.move(p)