import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a task for your to-do list")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_button]])

window.read()
window.close()
