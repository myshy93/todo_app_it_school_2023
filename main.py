todos = []
def main_menu(program_name):
    print("*" * 50)
    print(program_name)
    print("*" * 50)

def add_todo(title, text):
    todos.append((title, text))



main_menu("TODO APP")
