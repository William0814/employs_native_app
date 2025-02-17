import functions
import FreeSimpleGUI as gui


label = gui.Text("Action type: ")
input_box = gui.InputText(tooltip="Enter Employ", key="employ")
add_button = gui.Button("Add")

window = gui.Window("My Employ App",
                    layout=[[label, input_box, add_button]],
                    font= ("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            employs = functions.get_employs()
            new_employ = values['employ'].strip() + "\n"
            employs.append(new_employ.title())
            functions.write_employs(employs)

        case gui.WIN_CLOSED:
            break

    
window.close()