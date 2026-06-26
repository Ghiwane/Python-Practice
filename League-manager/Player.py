class Player:
    def __init__(self, name, scores, rank="bronze"):
        self.name=name
        self.scores=scores
        self.rank=rank
    
    def average(self):
        if self.scores:
            return float(sum(self.scores)/len(self.scores))
        return 0.0
    
    def statut(self):
        average_player=self.average()
        if average_player<60.0 : 
            return "Éliminé"
        elif 60.0 <= average_player <75.0:
            return "Qualifié"
        elif 75.0 <= average_player < 90.0:
            return "Demi-finaliste"
        else:
            return "Finaliste"
        
    def __str__(self):
        return f"{self.name} ({self.rank}) - average : {self.average():.1f} - {self.statut()}"