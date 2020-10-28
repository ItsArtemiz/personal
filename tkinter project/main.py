import tkinter as tk
import db
import time

# Functions

def errorOutput(e):
    error = tk.Tk()
    error.title("An error occured")
    error.geometry('1000x200')

    head = tk.Frame(error, width = 500, height=500)
    head.place(x=0, y=0)

    label = tk.Label(error, text="An Error Occured", font=("Calibri", 20))
    label.place(x=250, y=10)

    handler = tk.Label(error, text = e)
    handler.place(x=10, y=100)
    error.mainloop()

def quick_display():
    quick_clear_field()
    if i.get() == 1:
        total = db.totalMember()
        label = tk.Label(quick, text=f"Total number of members are: {total}", font=("Calibri", 10))
        label.place(x=400, y=50)

    if i.get() == 2:
        total = db.totalBooks()
        label = tk.Label(quick, text=f"Total number of members are: {total}", font=("Calibri", 10))
        label.place(x=400, y=50)

    if i.get() == 3:
        data = db.haveReturned()
        label = tk.Label(quick, text=f"Have Returned: {data['yes']} | Have Not Returned: {data['no']}")
        label.place(x=400, y=50)


def quick_clear_field():
    clear = tk.Label(quick,text='                                                                             ', font=("Calibri", 15))
    clear.place(x=400, y=50)

def member_info():
    try:
        n = member_number.get()
        info = db.memberInfo(n)
        placeInfo(info)
    except Exception as e:
        errorOutput(e)


def member_clear():
    number = tk.Label(member, text="                    ")
    number.place(x=500, y=70)

    name = tk.Label(member, text="                             ")
    name.place(x=500, y=100)

    bno = tk.Label(member, text="                    ")
    bno.place(x=500, y=130)

    doi = tk.Label(member, text="                    ")
    doi.place(x=500, y=160)

    dor = tk.Label(member, text="                    ")
    dor.place(x=500, y=190)

    ret = tk.Label(member, text="                    ")
    ret.place(x=500, y=220)

def placeInfo(n):
    number = tk.Label(member, text=n['id'])
    number.place(x=500, y=70)

    name = tk.Label(member, text=n['name'])
    name.place(x=500, y=100)

    bno = tk.Label(member, text=n['bno'])
    bno.place(x=500, y=130)

    doi = tk.Label(member, text=n['doi'])
    doi.place(x=500, y=160)

    dor = tk.Label(member, text=n['dor'])
    dor.place(x=500, y=190)

    ret = tk.Label(member, text=n['ret'])
    ret.place(x=500, y=220)


def member_insert():
    new = tk.Tk()
    new.title("Add Member")
    new.geometry('500x500')

def book():
    boo = tk.Tk()
    boo.title("All Books")
    boo.geometry('500x500')
    bFrame = tk.Frame(boo, width=500, height=500)
    e = db.allBooks()
    i = 0

    for info in e:
        print(info)
        label = tk.Label(bFrame, text=info[0])
        label.place(x=10, y=i+20)
        i = i+20

def member_remove():
    remove = tk.Tk()
    remove.title("Remove a member")
    remove.geometry("500x500")
    rFrame = tk.Frame(remove, width=500, height=500)
    rFrame.place(x=0, y=0)

    def member_delete():
        try:
            n = mem.get()
            a = db.memberRemove(n)
            if a is True:
                label = tk.Label(rFrame, text="Success")
                label.place(x=10, y=220)

                time.sleep(5)
                remove.destroy()
        except Exception as e:
            errorOutput(e)

    title = tk.Label(remove, text="Remove a Member", font=("Calibri", 20))
    title.place(x=10, y=10)

    mem = tk.Entry(remove, bd=3)
    mem.place(x=100, y=70)

    mem_title = tk.Label(remove, text="Member No.:")
    mem_title.place(x=10, y=70)

    button = tk.Button(remove, text="Delete Member", command=member_delete)
    button.place(x=15, y=125)

# GUI

wind = tk.Tk()
wind.title("Members and Books")
wind.geometry('700x700')

# Quick Selection

quick = tk.Frame(wind, width=700, height=200)
quick.place(x=0, y=0)

# Headers
quick_title = tk.Label(quick, text="Quick Information", font=("Calibri",20))
quick_title.place(x=10, y=10)

quick_output = tk.Label(quick, text="Output", font=("Calibri", 20))
quick_output.place(x=450, y=10)

# Titles for quick selection

i = tk.IntVar()
rad1=tk.Radiobutton(quick,text="Total number of members",font=("Calibri",10),value=1,variable=i)
rad2=tk.Radiobutton(quick,text="Total number of books",value=2,font=("Calibri",10),variable=i)
rad3=tk.Radiobutton(quick,text="Members who have/haven't returned the books",value=3,font=("Calibri",10),variable=i)
rad1.place(x=10,y=50)
rad2.place(x=10,y=80)
rad3.place(x=10,y=110)

# Action Buttons

quick_submit = tk.Button(quick, text = "Get Data", font=("Calibri",10), command=quick_display)
quick_submit.place(x=15, y=150)

quick_clear = tk.Button(quick, text = "Clear", font=("Calibri",10), command=quick_clear_field)
quick_clear.place(x=100, y=150)

# Particular Member

member = tk.Frame(wind, width = 700, height=500)
member.place(x=0, y=200)

# Headers

member_title = tk.Label(member, text="Member Information", font=("Calibri", 20))
member_title.place(x=10, y =10)

member_output = tk.Label(member, text="Output", font=("Calibri", 20))
member_output.place(x=450, y=10)

# Input Fields

member_number = tk.Entry(member, bd=3)
member_number.place(x=100, y=75)

# Title for inputs

number = tk.Label(member, text="Member No.:")
number.place(x=10, y=75)

# Action buttons

member_submit = tk.Button(member, text="Retrieve Data", command=member_info)
member_submit.place(x=15, y=120)

member_clear = tk.Button(member, text="Clear Data", command=member_clear)
member_clear.place(x=125, y=120)


# Member Info

no = tk.Label(member, text="Member Number:")
no.place(x=400, y=70)

name = tk.Label(member, text="Member Name:")
name.place(x=400, y=100)

bno = tk.Label(member, text="Book Number:")
bno.place(x=400, y=130)

doi = tk.Label(member, text="Date Of Issue:")
doi.place(x=400, y=160)

dor = tk.Label(member, text="Date Of Return:")
dor.place(x=400, y=190)

ret = tk.Label(member, text="Have Returned:")
ret.place(x=400, y=220)

# Member Insert and Delete

info = tk.Label(member, text="Other Functions", font=("Calibri", 20))
info.place(x=10, y=300)

insert = tk.Button(member, text="Add Member", command=member_insert)
insert.place(x=15, y=350)

delete = tk.Button(member, text="Delete Member", command=member_remove)
delete.place(x=120, y=350)

books = tk.Button(member, text="Book Info", command=book)
books.place(x=240, y=350)

wind.mainloop()