filepath = "todos.txt"


def get_todos(filepath=filepath):
    """ Reads a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        read_todos_local = file.readlines()
    return read_todos_local


def write_todos(todos_arg, filepath=filepath):
    """ Writes the updated to-do list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# allows to execute code directly but doesn't get executed if called from another file
if __name__ == "__main__":
    print("Test")
