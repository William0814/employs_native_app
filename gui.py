import functions
import FreeSimpleGUI as gui


label = gui.Text("Action")
input_box = gui.InputText(tooltip="Enter Employ")
add_button = gui.Button("Add")

window = gui.Window("My Employ App", layout=[[label], [input_box, add_button]])
window.read()
window.close()