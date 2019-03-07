from pymysql import *
from tkinter import *
from tkinter import messagebox as mb


class Add(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Name')
        self.t2 = Entry(self, bd=2)
        self.l4 = Label(self, text='')
        self.l5 = Label(self, text='Father\'s Name')
        self.t3 = Entry(self, bd=2)
        self.l6 = Label(self, text='')
        self.l7 = Label(self, text='Date')
        self.t4 = Entry(self, bd=2)
        self.l8 = Label(self, text='')
        self.l9 = Label(self, text='Account No.')
        self.t5 = Entry(self, bd=2)
        self.l10 = Label(self, text='')
        self.l11 = Label(self, text='Category')
        self.t6 = Entry(self, bd=2)
        self.l12 = Label(self, text='')
        self.l13 = Label(self, text='Weight')
        self.t7 = Entry(self, bd=2)
        self.l14 = Label(self, text='')
        self.l15 = Label(self, text='Amount')
        self.t8 = Entry(self, bd=2)
        self.l16 = Label(self, text='')
        self.l17 = Label(self, text='Payment Status')
        self.t9 = Entry(self, bd=2)
        self.l18 = Label(self, text='')
        self.b1 = Button(self, text='Submit', command=lambda:self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.l4.grid(row=4)
        self.l5.grid(row=5, column=0)
        self.t3.grid(row=5, column=1)
        self.l6.grid(row=6)
        self.l7.grid(row=7, column=0)
        self.t4.grid(row=7, column=1)
        self.l8.grid(row=8)
        self.l9.grid(row=9, column=0)
        self.t5.grid(row=9, column=1)
        self.l10.grid(row=10)
        self.l11.grid(row=11, column=0)
        self.t6.grid(row=11, column=1)
        self.l12.grid(row=12)
        self.l13.grid(row=13, column=0)
        self.t7.grid(row=13, column=1)
        self.l14.grid(row=14)
        self.l15.grid(row=15, column=0)
        self.t8.grid(row=15, column=1)
        self.l16.grid(row=16)
        self.l17.grid(row=17, column=0)
        self.t9.grid(row=17, column=1)
        self.l18.grid(row=18)

        self.b1.grid(row=19, column=0)
        self.b6.grid(row=19, column=1)

        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        name = self.t2.get()
        fname = self.t3.get()
        date = self.t4.get()
        accno = self.t5.get()
        category = self.t6.get()
        weight = self.t7.get()
        amount = self.t8.get()
        payment_status = self.t9.get()
        if recieptno == '':
            mb.showinfo("Add Record", 'Please enter reciept no')
        elif name == '':
            mb.showinfo("Add Record", 'Please enter name')
        elif fname == '':
            mb.showinfo("Add Record", 'Please enter father\'s name')
        elif date == '':
            mb.showinfo("Add Record", 'Please enter date')
        elif accno == '':
            mb.showinfo("Add Record", 'Please enter account no.')
        elif category == '':
            mb.showinfo("Add Record", 'Please enter category')
        elif weight == '':
            mb.showinfo("Add Record", 'Please enter weight')
        elif amount == '':
            mb.showinfo("Add Record", 'Please enter amount')
        elif payment_status == '':
            mb.showinfo("Add Record", 'Please enter payment status')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("insert into cropdata values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (recieptno, name, fname, date, accno, category, weight, amount, payment_status))
            con.commit()
            mb.showinfo("Crop Management System", 'Data Inserted!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            self.t3.delete(0, 'end')
            self.t4.delete(0, 'end')
            self.t5.delete(0, 'end')
            self.t6.delete(0, 'end')
            self.t7.delete(0, 'end')
            self.t8.delete(0, 'end')
            self.t9.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()