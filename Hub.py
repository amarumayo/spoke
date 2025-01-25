class Hub:
    
    def __init__(
        self, LFO = None, RFO = None, OLD = None, 
        DL = None, DR = None, SHD = None, OSB = None
    ):
        # LFO = left flange offset. Distance from the lock nut 
        #     to the centre of the left flange.
        # RFO = right flange offset. Distance from the lock nut 
        #     to the centre of the right flange.
        # OLD = measurement from lock nut to lock nut
        # DL = spoke circle diameter non-drive side
        # DR = spoke circle diameter drive side
        # SHD = spoke hole diameter. The diameter of the spoke hole in the flange. 
        #     Normally in that range of 2mm to 2.5mm.
        # OSB = The distance from the centre of the spoke hole to the centre of the rim. 

        self.LFO = LFO
        self.RFO = RFO
        self.OLD = OLD
        self.DL = DL
        self.DR = DR
        self.SHD = SHD
        self.OSB = OSB

    def __repr__(self):
        
        return f"Hub({self.LFO}, {self.RFO}, {self.OLD}, {self.DL}, {self.DR}, {self.SHD})"