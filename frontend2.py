from tkinter import *
import backend2
window=Tk()
window.title("BookStore")
def view_command():
    list1.delete(0,END)
    for i in backend2.view():
        list1.insert(END,i)
def search_command():
        list1.delete(0,END)
        for rows in backend2.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            print(1)
            list1.insert(END,rows)
def add_command():
    backend2.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])

    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

    e4.delete(0,END)
    e4.insert(END,  selected_tuple[4])
def delete_command():
    backend2.delete(selected_tuple[0])
def update_command():
    backend2.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

l1=Label(window,text="Title",bd=9).grid(row=0,column=0,sticky=N+S+E+W)
l2=Label(window,text="Author",bd=9).grid(row=0,column=2,sticky=N+S+E+W)
l3=Label(window,text="Year",bd=9).grid(row=1,column=0,sticky=N+S+E+W)
l4=Label(window,text="ISBN",bd=9).grid(row=1,column=2,sticky=N+S+E+W)


title_text=StringVar()
e1=Entry(window,text="Title",bd=9,font="Times",textvariable=title_text)
e1.grid(row=0,column=1,sticky=N+S+E+W)

author_text=StringVar()
e2=Entry(window,text="Author",bd=9,font="Times",textvariable=author_text)
e2.grid(row=0,column=3,sticky=N+S+E+W)

year_text=StringVar()
e3=Entry(window,text="Year",bd=9,font="Times",textvariable=year_text)
e3.grid(row=1,column=1,sticky=N+S+E+W)

isbn_text=StringVar()
e4=Entry(window,text="ISBN",bd=9,font="Times",textvariable=isbn_text)
e4.grid(row=1,column=3,sticky=N+S+E+W)

list1=Listbox(window,height=10,width=100)
list1.grid(row=2,column=1,rowspan=6,columnspan=3,sticky=N+S+E+W)

sb1=Scrollbar(window,activebackground="grey",bg="grey")
sb1.grid(row=2,column=4,rowspan=7,sticky=N+S+E+W)


list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View all",width=12,bd=3,bg='green',command=view_command)
b1.grid(row=2,column=0)

b2=Button(window,text="Search Entry",width=12,bd=3,bg="green",command=search_command)
b2.grid(row=3,column=0)

b3=Button(window,text="Add Entry",width=12,bd=3,bg='green',command=add_command)
b3.grid(row=4,column=0)

b4=Button(window,text="Update",width=12,bd=3,bg="green",command=update_command)
b4.grid(row=5,column=0)

b5=Button(window,text="Delete",width=12,bd=3,bg="red",command=delete_command)
b5.grid(row=6,column=0)

b6=Button(window,text="Close",width=12,bd=3,bg="red",command=window.destroy)
b6.grid(row=7,column=0)







window.mainloop()
