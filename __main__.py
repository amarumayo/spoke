from Calculator import Calculator
import os
import Rim 
import Hub
import argparse

def exists(var):
    try:
        var
        return True  # Variable exists
    except NameError:
        return False  # Variable doesn't exist


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="test"
    )

    parser.add_argument("--client", required = True)
    args = parser.parse_args()
    this_client = args.client 


if not(exists(this_client)):
    this_client = "CLI"

valid_clients = {'GUI', 'CLI'}
if not this_client in valid_clients:
    this_client = "CLI"

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    
#clear_screen()
calculator = Calculator(client = this_client)
ans = calculator.run()
string = f"Right Spoke Length: {ans.get('right')} \nLeft Spoke Length: {ans.get('left')}"
print(string)
