import PySimpleGUI as sh
import os, time

files = []
list = []

layout = [[sh.Text("                                                                      FIle Explorer",text_color="red", background_color="sky blue",auto_size_text=True)],
          [sh.Text("Enter the Directory:", text_color="blue", background_color="sky blue"),
           sh.InputText("", key="direc",background_color="#DFEFF0"),
           sh.Text("Enter the type of file:", background_color="sky blue", text_color="blue"),
           sh.InputText("", size=(5, 1), key="type",background_color="#DFEFF0")],

          [sh.Text("Date                                                                     File                                                                 Size (In Bytes)",background_color="sky blue",text_color="dark blue")],
          [sh.Text("", key="box", size=(85, 25),background_color="#DFEFF0")],
          [sh.Button("Submit"), sh.Button("Exit")]

          ]
window = sh.Window("FILE EXPLORER", layout, background_color="sky blue")


def file_size(file_path):
    if os.path.isfile(file_path):
        modTimesinceEpoc = os.path.getmtime(file_path)
        return [os.path.getsize(file_path), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))]


def bro():
        tope = str(value["type"])
        for r, d, f in os.walk(path):
            for file in f:

                if tope in file:
                    files.append(os.path.join(r, file))


def robo():
    bro()
    print(files)
    st = ""
    for file in files:
        a, b = file_size(file)
        st += str(b)+"     "+file + "                       " + str(a) + "          " + "\n"

    return st

while True:

    button, value = window.Read()
    path = str(value["direc"])
    tope = str(value["type"])

    if button == "Submit":
        window.FindElement("box").Update(robo())
        sh.Popup("These are the" + " " +tope +" "+"files available in "+ " " +path )

    elif button == None or "Exit":
        break
