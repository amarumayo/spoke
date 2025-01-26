
import math
import PySimpleGUI as sg
import sys
import Rim 
import Hub

class Calculator:

    def __init__(self, client):
        self.client = client
           
    @staticmethod
    def is_numeric_string(string):
        """ Returns True if string is a number. """
        try:
            float(string)
            return True
        except:
            return False

    def make_calc(self):
        """ Calculates the spoke length """
        
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


    def get_inputs_GUI(self):

        """ Gets the inputs via GUI """

        # window 1 layout
        layout1 = [
            [sg.Text('Effective Rim Diameter'), sg.Input(key = "ERD", enable_events = True)],
            [sg.Text('Number of Spokes'), sg.Input(key = "NSPOKE", enable_events = True)],
            [sg.Text('Number of Crosses'), sg.Input(key = "NCROSS", enable_events = True)],
            [sg.Button('Hub Specs')] 
        ]

        # window 2 layout
        layout2 = [
            [sg.Text('Right Flange Offset'), sg.Input(key = "RFO", enable_events = True)],
            [sg.Text('Left Flange Offset'), sg.Input(key = "LFO", enable_events = True)],
            [sg.Text('axle length e.g. 100'), sg.Input(key = "OLD", enable_events = True)],
            [sg.Text('Left spoke circle diameter'), sg.Input(key = "DL", enable_events = True)],
            [sg.Text('Right spoke circle diameter'), sg.Input(key = "DR", enable_events = True)],
            [sg.Text('Spoke hole diameter e.g. 2.6'), sg.Input(key = "SHD", enable_events = True)],
            [sg.Text('Drilling offset. Enter O for none'), sg.Input(key = "OSB", enable_events = True)],
            [sg.Button('Submit')] 
        ]

        # Create the Window
        win1 = sg.Window('Rim Specs', layout1)
        win2_active = False

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event1, values1 = win1.read()
            if event1 == sg.WIN_CLOSED: # if user closes window 
                sys.exit()

            if event1 == 'ERD':
                if values1['ERD'] and values1['ERD'][-1] not in '0123456789':
                    # If the last character is not a digit, remove it
                    win1['ERD'].update(values1['ERD'][:-1])

            if event1 == 'NSPOKE':
                if values1['NSPOKE'] and values1['NSPOKE'][-1] not in '0123456789':
                    # If the last character is not a digit, remove it
                    win1['NSPOKE'].update(values1['NSPOKE'][:-1])

            if event1 == 'NCROSS':
                if values1['NCROSS'] and values1['NCROSS'][-1] not in '0123456789':
                    # If the last character is not a digit, remove it
                    win1['NCROSS'].update(values1['NCROSS'][:-1])

            # hide window 1 and open window 2
            if event1 == 'Hub Specs' and not win2_active:

                if not values1['ERD']:
                    sg.popup_error('Please enter the effective rim diameter.')
                elif not values1['NSPOKE']:
                    sg.popup_error('Please enter the number of spokes.')
                elif not values1['NCROSS']:
                    sg.popup_error('Please enter the number of crosses.')
                else:
                    win2_active = True
                    win1.Hide()
                    win2 = sg.Window('Hub Specs', layout2)

                    while True:
                        event2, values2 = win2.read()

                        if (event2 == sg.WIN_CLOSED):
                            sys.exit()

                        if (event2 == 'Submit'):
                            if not values2['RFO']:
                                sg.popup_error('Please enter the right flange offset.')
                            elif not values2['LFO']:
                                sg.popup_error('Please enter the left flange offset.')
                            elif not values2['OLD']:
                                sg.popup_error('Please enter the axle lenght.')
                            elif not values2['DL']:
                                sg.popup_error('Please enter the left spoke circle diameter.')
                            elif not values2['DR']:
                                sg.popup_error('Please enter the right spoke circle diameter.')
                            elif not values2['SHD']:
                                sg.popup_error('Please enter the spoke hole circle diameter.')
                            elif not values2['OSB']:
                                sg.popup_error('Please enter the drilling offset.')
                            else:
                                win2.Close()
                                win1.Close()
                                break
                            

                        if event2 == 'RFO':
                            if values2['RFO'] and values2['RFO'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['RFO'].update(values2['RFO'][:-1])

                        if event2 == 'LFO':
                            if values2['LFO'] and values2['LFO'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['LFO'].update(values2['LFO'][:-1])

                        if event2 == 'OLD':
                            if values2['OLD'] and values2['OLD'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['OLD'].update(values2['OLD'][:-1])

                        if event2 == 'DL':
                            if values2['DL'] and values2['DL'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['DL'].update(values2['DL'][:-1])

                        if event2 == 'DL':
                            if values2['DL'] and values2['DL'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['DL'].update(values2['DL'][:-1])

                        if event2 == 'SHD':
                            if values2['SHD'] and values2['SHD'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['SHD'].update(values2['SHD'][:-1])

                        if event2 == 'OSB':
                            if values2['OSB'] and values2['OSB'][-1] not in '.0123456789':
                                # If the last character is not a digit, remove it
                                win2['OSB'].update(values2['OSB'][:-1])

                    
                    break

        values1 = win1.ReturnValuesDictionary
        values2 = win2.ReturnValuesDictionary

        values1 = {k: float(v) for k, v in values1.items()}
        values2 = {k: float(v) for k, v in values2.items()}

        return(values1 | values2)

    def get_inputs_CLI(self):

        """ Gets the inputs via CLI """

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
        
        values = {
            'ERD':ERD, 'NSPOKE':num_spokes, 'NCROSS':num_crosses, 'LFO':LFO, 
            'RFO':RFO, 'OLD':OLD, 'DL':DL, 'DR':DR, 'SHD':SHD, 'OSB':OSB
        }
        
        return(values)

    def run(self):      

        """ run the program """         
        if (self.client == 'CLI'):
            values = self.get_inputs_CLI()
        elif (self.client == "GUI"):
            values = self.get_inputs_GUI()

        hub = Hub.Hub(
            LFO = values['LFO'], 
            RFO = values['RFO'],
            OLD = values['OLD'], 
            DL = values['DL'], 
            DR = values['DR'], 
            SHD = values['SHD'], 
            OSB = values['OSB']
        )

        rim = Rim.Rim(
            ERD = values['ERD'], 
            num_crosses = values['NCROSS'], 
            num_spokes = values['NSPOKE']
        )     

        self.hub = hub        
        self.rim = rim
        ans = self.make_calc()
        return ans
        
