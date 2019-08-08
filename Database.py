import sqlite3 as sg

db=sg.connect("ToDo.db")
def table():
    c=db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Checklist1(Name TEXT,date TEXT,Priority TEXT,Completed TEXT DEFAULT 0) ''')
    print(c.fetchall())
    c.close()

def readl():
    
    c = db.cursor()
    #c.execute('''SELECT Name,date,Priority FROM Checklist1 ORDER BY Priority ASC''')
    c.execute('''SELECT Name, date, Priority from Checklist1 WHERE Completed=0 ORDER BY date ASC ''')
    lst = c.fetchall()
    print(lst,end="")
    y = ""
    lst1 = []
    for k in lst:
        y = ''
        for i in k:
            for j in i:
                y += j
            y += " "
        lst1.append(y.strip())
    db.commit()
    c.close()
    return lst1
    
def readcomp():
    c=db.cursor()
    c.execute('''SELECT Name,date,Priority from Checklist1 WHERE Completed=1''')
    lst = c.fetchall()
    y = ""
    lst1 = []
    for k in lst:
        y = ''
        for i in k:
            for j in i:
                y += j
            y += " "
        lst1.append(y.strip())
    db.commit()
    c.close()
    return lst1


def add(lst):
    c=db.cursor()
    x=''
    for i in range(len(lst)):
        x = lst[i].split()
    c.execute('''INSERT INTO Checklist1(Name,date,Priority) VALUES(?,?,?)''',(x[0],x[1],x[3]))
    db.commit()
    c.close()


def deltable():
    c=db.cursor()
    c.execute('''DELETE FROM Checklist1''')
    db.commit()
    c.close()


def delc(x):
    c=db.cursor()
    z=''
    z=x.split()
    print(z[0])
    c.execute('''DELETE FROM Checklist1 WHERE Name=?''',(z[0],))
    db.commit()
    c.close()
	

def delname(x):
    c=db.cursor()
    y=''
    y=x.split()
    print(y[0])
    c.execute('''delete from Checklist1 where Name=?''',(y[0],))
    db.commit()
    c.close()

def compname(x):
    c=db.cursor()
    y=''
    y=x.split()
    c.execute('''UPDATE Checklist1 SET Completed=1 WHERE Name = ? ''',(y[0],))
    db.commit()
    c.close()


