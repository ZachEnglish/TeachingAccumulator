# This is a sample Python script.
import PySimpleGUI as sg

layout = [
    [sg.Text("First Name"), sg.Input(key="FIRST_NAME")],
    [sg.Text("Last Name"), sg.Input(key="LAST_NAME")],
    [sg.Button("Popup"), sg.Button("Read"), sg.Exit()],
]

window = sg.Window("My first GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Read":
        print(event, values)
    if event == "Popup":
        print("So you want a popup?")

window.close()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
