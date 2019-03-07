from pymysql import *
from tkinter import *
from tkinter import messagebox as mb


class Search(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Enter Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Enter Name')
        self.t2 = Entry(self, bd=2)
        self.l4 = Label(self, text='')
        self.b1 = Button(self, text='Submit', command=lambda: self.Search(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l4.grid(row=4)
        self.b1.grid(row=5, column=0)
        self.b6.grid(row=5, column=1)
        self.pack()

    def Search(self):
        recieptno = self.t1.get()
        if recieptno == '':
            mb.showinfo("Search Record", 'Please enter reciept no.')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                con.commit()
                mb.showinfo("Crop Management System", record)
            else:
                mb.showinfo("Crop Management System", 'Data not Found!!')
        con.close()
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        exit()

    def exitprog(self):
        exit()