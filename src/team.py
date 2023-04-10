class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
    

        # def add_player(self, players_name, players_list):

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        else:
            return False

    def team_points(self):



