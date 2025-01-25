from Calculator import Calculator
import os
import Rim 
import Hub

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

clear_screen()
calculator = Calculator()
values = calculator.get_inputs_CLI()
# values = calculator.get_inputs_CLI()



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



calculator.hub = hub        
calculator.rim = rim
ans = calculator.make_calc()
string = f"Right Spoke Length: {ans.get('right')} \nLeft Spoke Length: {ans.get('left')}"

print(string)