from pymysql import *
from tkinter import *
from tkinter import messagebox as mb


class Delete(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Enter Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l4 = Label(self, text='')
        self.b1 = Button(self, text='Submit', command=lambda: self.Delete(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l4.grid(row=4)
        self.b1.grid(row=5, column=0)
        self.b6.grid(row=5, column=1)

        self.pack()

    def Delete(self):
        recieptno = self.t1.get()
        if recieptno == '':
            mb.showinfo("Login", 'Please enter reciept no.')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % (
                recieptno))
            record = cur.fetchone()
            if record:
                cur.execute("delete from cropdata where recieptno='%s'" % (
                    recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Data Deleted Successfully!!')
            else:
                mb.showinfo("Crop Management System", 'Data not Found!!')
            con.close()
            self.t1.delete(0, 'end')

    def exitprog(self):
        exit()
