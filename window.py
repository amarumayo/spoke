import PySimpleGUI as sg

# All the stuff inside your window.
layout = [
    [sg.Text('Effective Rim Diameter'), sg.Input(key = "-ERD-", enable_events = True)],
    [sg.Text('Number of Spokes'), sg.Input(key = "-NSPOKE-", enable_events = True)],
    [sg.Text('Number of Crosses'), sg.Input(key = "-NCROSS-", enable_events = True)],
    [sg.Button('Ok')] 
]

# Create the Window
window = sg.Window('Rim Specs', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
        break

    if event == '-ERD-':
        if values['-ERD-'] and values['-ERD-'][-1] not in '0123456789':
            # If the last character is not a digit, remove it
            window['-ERD-'].update(values['-ERD-'][:-1])

    if event == '-NSPOKE-':
        if values['-NSPOKE-'] and values['-NSPOKE-'][-1] not in '0123456789':
            # If the last character is not a digit, remove it
            window['-NSPOKE-'].update(values['-NSPOKE-'][:-1])

    if event == '-NCROSS-':
        if values['-NCROSS-'] and values['-NCROSS-'][-1] not in '0123456789':
            # If the last character is not a digit, remove it
            window['-NCROSS-'].update(values['-NCROSS-'][:-1])


print(values['-ERD-'])
print(values['-NSPOKE-'])
print(values['-NCROSS-'])


window.close()