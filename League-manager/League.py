from Player import Player

class League:
    def __init__(self, name):
        self.name = name
        self.players = []

    def new_player(self, player: Player):
        for i in self.players:
            if i.name == player.name:
                print(f"This player : {player.name}, already exists.")
                return
        self.players.append(player)
        print(f"{player.name} added succesfully.")

    def search_player(self, name):
        for i in self.players:
            if i.name == name:
                return i
        return None
    
    def ranking(self):
        return sorted(self.players, key=lambda player: player.average(), reverse=True)
    
    def finalists(self):
        finalistes=[]
        for i in self.players:
            if i.statut() == "Finaliste":
                finalistes.append(i)
        return finalistes
    
    def __len__(self):
        return len(self.players)
    
    def __str__(self):
        return f"League {self.name} - {len(self)} players"