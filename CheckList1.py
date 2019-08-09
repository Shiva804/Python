
import PySimpleGUI as sh
import Database as ph

ph.table()
list=[]
list2=[]

list =ph.readl()
list2=ph.readcomp()


layout=[
    [sh.Text('Enter TO DO list:',text_color="blue",background_color="cyan")],
    [sh.InputText('',key='name',background_color="Sky Blue"),sh.Button('ADD',key="add",size=(6,1)),sh.CalendarButton("SELECT DATE",target="date",key="dat"),sh.InputText("",key = "date",size=(19,1),disabled=True ,do_not_clear=True),sh.Text("Priority:",text_color="blue",background_color="cyan"),sh.Spin([sz for sz in range(1, 6)], initial_value=1, change_submits=True, key='spin',size=(5,3),background_color="Sky Blue")],
    [sh.Text("All Tasks",text_color="blue",background_color="cyan"),sh.Listbox(size=(30,10),key="box", enable_events= True ,background_color="Sky Blue",values=list),sh.Text("Completed Tasks",text_color="blue",background_color="cyan"),sh.Listbox( enable_events= True,size=(30,10),key="cbox",background_color="Sky Blue",values=list2),sh.Button("Delete Completed",size=(13,1),key="delcomp")],
    [sh.Button("DELETE",key="del"),sh.Button("Completed",size=(8,1),key="comp",),sh.Button("Prioritize")],
    [sh.Button("EXIT",size=(5,1))]

]
form = sh.FlexForm('Calendar', no_titlebar=True)


window=sh.Window("CheckBox",layout,background_color="cyan")
if len(list)==0:
    sh.Popup("You don't have any tasks!")
if len(list)>10:
    sh.Popup("You have lots of work to do!")

while True:
    event,values=window.Read()
    print(event, values)
    if event is None or event == "EXIT":
        break
      
    
    if event=="add":
        
        if (values["date"] == ""):
            sh.Popup("Select a date")
            continue
        x = values["name"] + " " + values["date"] + " " + str(int(values["spin"]))
        list.append(x)
        window.FindElement('box').Update(values=list)
        window.FindElement("name").Update("")
        #window.FindElement('dat').Update("SELECT DATE")
        window.FindElement('date').Update("")
        window.FindElement('add').Update("ADD")
        
        ph.add(list)

      
    elif event=="del":
        list.remove(''.join(values['box'][0]))
        window.FindElement('box').Update(values=list)
        ph.delname(values["box"][0])
        
 
    elif event=="delcomp":
        list2.remove(''.join(values['cbox'][0]))
        window.FindElement('cbox').Update(values=list2)
        ph.delc(values["cbox"][0])
        

    elif event=="comp":
        
        list2.append(values['box'][0])
        ph.compname(values['box'][0])
        window.FindElement('cbox').Update(values=list2)
        list.remove(values['box'][0])
        window.FindElement('box').Update(values=list)
        window.FindElement('comp').Update("Completed")
        

    elif( event == "Prioritize"):
         for i in range(len(list)):
             min = i
             for j in range(i+1, len(list)):
                   if(list[min][-1] > list[j][-1]):
                       min=j
             list[i],list[min] = list[min],list[i]
             window.FindElement("box").Update(list)
        

window.Close()

