import PySimpleGUI as sg

class Logs:

    sg.theme('LightBrown13')

    menu_def = [
        ['&File', ['&Open', '&Save', '---', '&Properties', 'E&xit']],
        ['&Edit', ['Paste', ['Special', 'Normal,'], 'Undo'],],
        ['&Help', '&About...'],]

    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.T('Uzraksti kaut ko:')],
                    [sg.I(key='viens')],
                    [sg.I(key='divi')],
                    [sg.T(key='tris')],
                    [sg.B('Read'), sg.B('Write'), sg.B('Nolasīt datni'), sg.Exit()]]

    window = sg.Window('Lodziņš', layout, default_element_size=(50, 1), default_button_element_size=(12, 1))

    while True:
        event, values = window.read()
        print(event, values)

        if event == 'Read':
            summa = int(values['viens']) + int(values['divi'])
            sg.popup('Tu ievadīji:', summa)

        if event == sg.WIN_CLOSED or event ==  'Exit':
            break

        if event == 'Write':
            window['tris'].update((int(values['viens'])) + (int(values['divi'])))

        if event == 'Nolasīt datni':
            datne = open('saskarnes.txt')
            print(datne.read())
            print(datne.read())
            window['tris'].update(datne.read())

        

    window.close()