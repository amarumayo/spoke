import PySimpleGUI as sg
import sys

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


values = values1 | values2



