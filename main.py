todos = []

def main_menu(program_name):
    print("*" * 50)
    print(program_name)
    print("*" * 50)

def add_todo(title, text):
    """Add a todo into the list."""
    todos.append((title, text))


def show_todos():
    for i in todos:
        print(i[0], i[1])

main_menu("TODO APP")
