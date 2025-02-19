import functions
import FreeSimpleGUI as gui


label = gui.Text("Action type: ")
input_box = gui.InputText(tooltip="Enter Employ", key="employ")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_employs(), key='employs', enable_events=True, size=[45, 10])

edit_button = gui.Button("Edit")

window = gui.Window("My Employ App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font= ("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['employs'])
    match event:
        case 'Add':
            employs = functions.get_employs()
            new_employ = values['employ'].strip() + "\n"
            employs.append(new_employ.title())
            functions.write_employs(employs) 
            window['employs'].update(values=employs)

        case 'Edit':
            employ_to_edit = values['employs'][0]
            new_employ = values['employ']

            employs = functions.get_employs()
            index = employs.index(employ_to_edit)
            employs[index] = new_employ.title()
            functions.write_employs(employs)
            window['employs'].update(values=employs) 

        case 'employs':
            window['employ'].update(value=values['employs'][0])

        case gui.WIN_CLOSED:
            break

    
window.close()