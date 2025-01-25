from Calculator import Calculator
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

clear_screen()
calculator = Calculator()
ans = calculator.run()
string = f"Right Spoke Length: {ans.get('right')} \nLeft Spoke Length: {ans.get('left')}"

print(string)