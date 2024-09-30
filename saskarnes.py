import PySimpleGUI as sg

sg.theme('LightBrown13')

layout = [[sg.Text('Uzraksti kaut ko:')],
                 [sg.I(key='viens')],
                 [sg.I(key='divi')],
                 [sg.B('Read'), sg.Exit()]]

window = sg.Window('Lodziņš', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Read':
        summa = int(values['viens']) + int(values['divi'])



    sg.popup('Tu ievadīji:', summa)
    if event == sg.WIN_CLOSED or event ==  'Exit':
        break



window.close()
    
# import PySimpleGUI as sg

# sg.theme("LightBrown13")

# layout = [[sg.Text('Uzraksti kaut ko:')],
#                 [sg.I(key="-IN-")],
#                 [sg.Submit("Iesniegt"), sg.Cancel("Iziet")]]

# window = sg.Window("Lodziņš", layout)

# while True:
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == "Iziet":
#         break
# text_input = values["-IN-"]
# sg.popup("Tu ievadīji:", text_input)

# window.close()

