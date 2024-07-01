# from functions import get_todos, write_todos
import functions
import time

time_now = time.strftime("%b %d %Y, %H:%M:%S")
print("Now is", time_now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:].capitalize()    # list slicing

        todos = functions.get_todos()

        todos.append(todo + "\n")
        
        todos = functions.write_todos(todos)

    elif 'show' in user_action:    # "|" can be used as "or" >> e.g., 'show' | 'display' :
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)

    elif 'edit' in user_action:
        try:
            number = int(user_action[5:]) - 1
            new_todo = input("Enter new todo: ")

            todos = functions.get_todos()
            todos[number] = new_todo.capitalize() + '\n'
            todos = functions.write_todos(todos)

        except ValueError:
            print("Command not valid - please add todo's number after 'edit' command")
            continue

    elif 'complete' in user_action:
        try:
            number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            todos = functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Command not valid")

print("Bye!")

