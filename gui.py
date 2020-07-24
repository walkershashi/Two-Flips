import PySimpleGUI as GUI

def displayGui():

    GUI.theme('DarkAmber')	# Add a touch of color
    
    # All the stuff inside your window.
    layout = [  
        [GUI.Text('Name:'), GUI.InputText()],
        [GUI.Button('Ok'), GUI.Button('Cancel')]
    ]

    # Create the Window
    window = GUI.Window('TwoFlips', layout)

    # Event Loop to process "events" and get the "values" of the inputs

    while True:
        event, values = window.read()

        if event == GUI.WIN_CLOSED or event == 'Cancel' or event == 'Ok':
            break

    window.close()
    return values[0]
