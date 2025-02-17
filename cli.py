# from functions import get_employs, write_employs
import functions


print('--- Welcome to the Program of Employs ---')

while True:
    user_action = input('Please select add, show, delete, edit or exit followed by the number: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        employ = user_action[4:] + '\n'

        employs = functions.get_employs()

        employs.append(employ.title())
        functions.write_employs(employs)

    elif 'show' in user_action:
        employs = functions.get_employs()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(employs):
            item = item.strip('\n')
            row = f'{index + 1}-{item.title()}'
            print(row)

    elif 'edit' in user_action:
        try:
            print('Here is names exiting:')
            print('----------------------')
            employs = functions.get_employs()

            for index, item in enumerate(employs):
                item = item.strip('\n')
                row = f'{index + 1}-{item.title()}'
                print(f'{row}')
            number = int(user_action[5:])
            number = number - 1
            new_employ = input('Enter new Employ: ')
            employs[number] = new_employ.title() + '\n'
            print(f'The new name is: {new_employ.title()}')

            functions.write_employs(employs)

        except ValueError or IndexError:
            print('Your command is not valid...')
            continue

    elif 'delete' in user_action:
        try:
            number = int(user_action[7:])

            employs = functions.get_employs()

            index = number - 1
            name_removed = employs[index].strip()
            employs.pop(index)

            functions.write_employs(employs)

            print(f'Name --{name_removed}-- was removed from the list.')
        except IndexError:
            print('There is nothing with this number..')
            continue

    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid..')

print('Ok Bye!!')