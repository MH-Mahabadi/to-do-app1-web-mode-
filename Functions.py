filepath = 'todos.txt'


def read_todos():
    """ Read a text file and return the list of
    to-do items.
    """
    
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local    


def write_todos(todos_arg, file_path=filepath):
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    todos = read_todos()
    print(todos)
