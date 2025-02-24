

print('Welcome to the Program of Employs')

while True:
    user_action = input('Please select add, show, delete, edit or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('enter Employ: ') + '\n'
            with open('Employs.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo.title())
            with open('Employs.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'show' | 'display':
            with open('Employs.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index+1}-{item.title()}'
                print(row)

        case 'edit':
            number = int(input('Number of the Employ to edit: '))
            number = number - 1
            print('Here is names exiting:')
            with open('Employs.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item.title()}'
                print(f'{row}')
            new_todo = input('Enter new Employ: ')
            todos[number] = new_todo.title() + '\n'
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item.title()}'
                print(row)
            with open('Employs.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'delete':
            number = int(input('Number of the Employ to delete: '))
            with open('Employs.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            name_removed = todos[index].strip()
            todos.pop(index)
            with open('Employs.txt', 'w') as file:
                todos = file.writelines(todos)
            print(f'Name --{name_removed}-- was removed from the list.')

        case 'exit':
            break

        case anything:
            print('your command is not valid....')

print('Ok Bye!!')

# cambios para git