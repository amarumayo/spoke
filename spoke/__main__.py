import os
import argparse
import PySimpleGUI as sg
from spoke import calculator

def exists(var):
    try:
        var
        return True  # Variable exists
    except NameError:
        return False  # Variable doesn't exist


# read the arguments passed in from command line
this_client = "CLI"
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description = "argument client used to toggle CLI or GUI"
    )

    parser.add_argument("--client", required = True)
    args = parser.parse_args()
    this_client = args.client 

valid_clients = {'GUI', 'CLI'}
if not this_client in valid_clients:
    this_client = "CLI"


def clear_screen():
    """ function to clear the screen """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
# clear_screen()
calculator = calculator.Calculator(client = this_client)
ans = calculator.run()
string = f"Right Spoke Length: {ans.get('right')} \nLeft Spoke Length: {ans.get('left')}"

if this_client == "CLI":
    print(string)

elif this_client == "GUI":
    sg.popup(string, title = 'Spoke Lengths')




