import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a task for your to-do list")
input_box = sg.InputText(tooltip="Enter a todo", key='to-do')
add_button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['to-do'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

