
import PySimpleGUI as sh

file="C:\\Users\\krish\\OneDrive\\Desktop\\Python Project\\toDoList.txt"
file2="C:\\Users\\krish\\OneDrive\\Desktop\\Python Project\\Completed.txt"

lst=[]
lst2=[]
def readFile(lst):
    with open(file,"r") as f:
        lst = f.read().splitlines()
        return lst

def readFile2(lst2):
    with open(file2,"r") as g:
        lst2=g.read().splitlines()
        return lst2

def right(lst):
    with open(file,"w") as f :
        for i in range(len(lst)):
            f.write(lst[i])
            f.write("\n")


def left(lst2):
    with open(file2,"w") as g :
        for i in range(len(lst2)):
            g.write(lst2[i])
            g.write("\n")


lst=readFile(lst)
lst2=readFile2(lst2)
layout=[
    [sh.Text('Enter TO DO list:',text_color="blue",background_color="cyan")],
    [sh.InputText('',key='name',background_color="Sky Blue"),sh.Button('ADD',key="add",size=(6,1)),sh.CalendarButton("SELECT DATE",target=(1,0),key="dat")],
    [sh.Text("All Tasks",text_color="blue",background_color="cyan"),sh.Listbox(values=lst,size=(30,10),key="box", enable_events= True ,background_color="Sky Blue"),sh.Text("Completed Tasks",text_color="blue",background_color="cyan"),sh.Listbox( bind_return_key = True,size=(30,10),key="cbox",background_color="Sky Blue",values=lst2),sh.Button("Delete Completed",size=(13,1),key="delc")],
    [sh.Button("DELETE",key="del"),sh.Button("Completed",size=(8,1),key="comp",)],[sh.Text("Priority:",text_color="blue",background_color="cyan"),sh.Spin([sz for sz in range(1, 6)], initial_value=1, change_submits=True, key='spin',size=(5,3),background_color="Sky Blue")],
    [sh.Button("EXIT",size=(5,1))]

]
form = sh.FlexForm('Calendar', no_titlebar=True)




window=sh.Window("CheckBox",layout,background_color="cyan")

while True:
    event,values=window.Read()
    print(event, values)
    if event=="add":

        lst.append(values['name'])
        window.FindElement("name").Update("")
        window.FindElement('box').Update(values=lst)
        window.FindElement('dat').Update("SELECT DATE")
        window.FindElement('add').Update("ADD")
        right(lst)
        
     
    elif event=="del":

        lst.remove(''.join(values['box'][0]))
        window.FindElement('box').Update(values=lst)
        right(lst)

    elif event=="delc":
        lst2.remove(''.join(values['cbox'][0]))
        window.FindElement('cbox').Update(values=lst2)
        left(lst2)


    elif event=="comp":

        lst2.append(values['box'][0])
        window.FindElement('cbox').Update(values=lst2)
        lst.remove(values['box'][0])
        window.FindElement('box').Update(values=lst)
        window.FindElement('comp').Update("Completed")
        left(lst2)

    elif event=="spin":
        sz_spin = int(values['spin'])
        sz=sz_spin
        if sz_spin==1:
            v = ''.join(values["box"])
            lst.insert(0, lst.pop(lst.index(v)))
            window.FindElement('spin').Update(sz)
            window.FindElement('box').Update(values=lst)

        elif sz_spin==2:
            v = ''.join(values["box"])
            lst.insert(1, lst.pop(lst.index(v)))
            window.FindElement('spin').Update(sz)
            window.FindElement('box').Update(values=lst)

        elif sz_spin==3:
            v = ''.join(values["box"])
            lst.insert(2, lst.pop(lst.index(v)))
            window.FindElement('spin').Update(sz)
            window.FindElement('box').Update(values=lst)

        elif sz_spin==4:
            v = ''.join(values["box"])
            lst.insert(3, lst.pop(lst.index(v)))
            window.FindElement('spin').Update(sz)
            window.FindElement('box').Update(values=lst)

        elif sz_spin==5:
            v = ''.join(values["box"])
            lst.insert(4, lst.pop(lst.index(v)))
            window.FindElement('spin').Update(sz)
            window.FindElement('box').Update(values=lst)

    elif event=="EXIT":
        break

window.Close()

