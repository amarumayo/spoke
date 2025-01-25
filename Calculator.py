import Rim 
import Hub
import math

class Calculator:
       
    
    @staticmethod
    def is_numeric_string(string):
        """ Returns True if string is a number. """
        try:
            float(string)
            return True
        except:
            return False

    def make_calc(self):
        
            R = self.rim.ERD / 2
            LH = self.hub.DL / 2
            LF = self.hub.LFO
            R = self.rim.ERD / 2
            RH = self.hub.DR / 2
            RF = self.hub.RFO
            h = self.rim.num_spokes

            ML = 2 * R * LH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
            left_length = round((math.sqrt(R**2 + LH**2 + LF**2 - ML)) - self.hub.SHD / 2, 1)
            
            MR = 2 * R * RH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
            right_length = round((math.sqrt(R**2 + RH**2 + RF**2 - MR)) - self.hub.SHD / 2, 1)

            return {'right':right_length, 'left':left_length}
        
    def run(self):
        print ("getting hub specs...")
               
        # build hub
        LFO = ''        
        while not Calculator.is_numeric_string(LFO):
            LFO = input('enter left flange offset e.g. 35: ')
        LFO = float(LFO)

        RFO = ''        
        while not Calculator.is_numeric_string(RFO):
            RFO = input('enter right flange offset e.g. 35: ')
        RFO = float(RFO)

        OLD = ''        
        while not Calculator.is_numeric_string(OLD):
            OLD = input('enter OLD e.g. 100: ')        
        OLD = int(OLD)

        DL = ''        
        while not Calculator.is_numeric_string(DL):
            DL = input('enter left spoke circle diameter e.g. 57: ')      
        DL = int(DL)

        DR = ''        
        while not Calculator.is_numeric_string(DR):
            DR = input('enter right spoke circle diameter e.g. 57: ')      
        DR = int(DR)

        SHD = ''        
        while not Calculator.is_numeric_string(SHD):
            SHD = input('enter spoke hole diameter e.g. 2.6: ')      
        SHD = float(SHD)
        
        OSB = ''        
        while not Calculator.is_numeric_string(OSB):
            OSB = input('enter offset spoke bed. 0 for none: ')      
        OSB = float(OSB)

        hub = Hub.Hub(
            LFO = LFO, RFO = RFO, OLD = OLD, 
            DL = DL, DR = DR, SHD = SHD, OSB = OSB
        )

        print ("getting rim specs...")
                        
        # build rim
        ERD = ''        
        while not Calculator.is_numeric_string(ERD):
            ERD = input('enter effective rim diameter e.g. 599: ')
        ERD = int(ERD)

        num_spokes = ''        
        while not Calculator.is_numeric_string(num_spokes):
            num_spokes = input('enter number of spokes e.g. 32: ')
        num_spokes = int(num_spokes)

        num_crosses = ''        
        while not Calculator.is_numeric_string(num_crosses):
            num_crosses = input('enter number of crosses e.g. 3: ')
        num_crosses = float(num_crosses)
        
        rim = Rim.Rim(
           ERD = ERD, num_crosses = num_crosses, num_spokes = num_spokes
        )     

        self.hub = hub
        self.rim = rim
        
        return(self.make_calc())