todos = []

def main_menu(program_name):
    print("*" * 50)
    print(program_name)
    print("*" * 50)


def show_todos():
    for i in todos:
        print(i[0], i[1])

main_menu("TODO APP")
