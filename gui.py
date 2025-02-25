import functions
import FreeSimpleGUI as gui
import time


gui.theme("DarkBlue15")
clock = gui.Text('', key='clock')
label = gui.Text("Action type: ")
input_box = gui.InputText(tooltip="Enter Employ", key="employ")
add_button = gui.Button(key='Add', size=10, image_source='add.png', tooltip='Add Employ')
list_box = gui.Listbox(values=functions.get_employs(), key='employs', enable_events=True, size=[45, 10])

edit_button = gui.Button(key="Edit", size=10, image_source='edit.png', tooltip='Edit Employ')
delete_button = gui.Button(key='Delete', size=10, image_source='delete.png', tooltip='Delete Employ')
exit_button = gui.Button(key='Exit', size=15, image_source='exit.png', tooltip='Exit')

layout = [ [clock],
           [label], 
           [input_box, add_button],
           [list_box, edit_button, delete_button],
           [exit_button]]

window = gui.Window("My Employ App",
                    layout=layout,
                    font= ("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%d-%m-%y %H:%M:%S:'))
    print(1, event)
    print(2, values)
    print(3, values['employs'])
    match event:
        case 'Add':
            employs = [e.strip() for e in functions.get_employs()]
            new_employ = values['employ'].strip().title() 
            employs.append(new_employ)
            functions.write_employs(employs) 
            window['employs'].update(values=employs)
            window['employ'].update(value='')
            
        case 'Edit':
            try:
                employ_to_edit = values['employs'][0]
                new_employ = values['employ'].strip().title()
                employs = [e.strip() for e in functions.get_employs()]
                index = employs.index(employ_to_edit)
                employs[index] = new_employ.title()
                functions.write_employs(employs)
                window['employs'].update(values=employs) 
            except IndexError:
                gui.popup('Please select an item first.', font=("Helvetica", 15), title='Error')

        case 'Delete':
            try:
                employ_delete = values['employs'][0]
                employs = [e.strip() for e in functions.get_employs()]
                employs.remove(employ_delete)
                functions.write_employs(employs)
                window['employs'].update(values=employs)
                window['employ'].update(value='')
            except IndexError:
                gui.popup('Please select an item first.', font=("Helvetica", 15), title='Error')
        case 'Exit':
            break
        case 'employs':
            window['employ'].update(value=values['employs'][0])

        case gui.WIN_CLOSED:
            break

    
window.close()
