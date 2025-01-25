class Rim:
    
    def __init__(self, ERD = None, num_spokes = None, num_crosses = None):
        self.ERD = ERD
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses

    def __repr__(self):
        
        return f"Wheel({self.ERD}, {self.num_crosses}, {self.num_crosses})"