from tkinter import *
from tkinter import messagebox as mb
from pymysql import *


class Name(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian',20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Name')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)

        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        name = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif name == '':
            mb.showinfo("Crop Management System", 'Please enter name')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute("update cropdata set name='%s' where recieptno='%s' " % (name, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Fname(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Father\'s Name')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)

        self.pack()

    def insert(self):

        recieptno = self.t1.get()
        fname = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif fname == '':
            mb.showinfo("Crop Management System", 'Please enter father\'s name')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute("update cropdata set fname='%s' where recieptno='%s' " % (fname, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Date(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Date')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        date = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif date == '':
            mb.showinfo("Crop Management System", 'Please enter date')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute(
                    "update cropdata set date='%s' where recieptno='%s' " % (date, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Account(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Account No.')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        accno = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif accno == '':
            mb.showinfo("Crop Management System", 'Please enter account no.')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute(
                    "update cropdata set accno='%s' where recieptno='%s' " % (accno, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Category(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Category')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        category = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif category == '':
            mb.showinfo("Crop Management System", 'Please enter Category')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute(
                    "update cropdata set category='%s' where recieptno='%s' " % (category, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Weight(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Weight')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=12, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        weight = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif weight == '':
            mb.showinfo("Crop Management System", 'Please enter weight')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute(
                    "update cropdata set weight='%s' where recieptno='%s' " % (weight, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()


class Amount(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Amount')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), width=15, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
            recieptno = self.t1.get()
            amount = self.t2.get()
            if recieptno == '':
                mb.showinfo("Crop Management System", 'Please enter reciept no.')
            elif amount == '':
                mb.showinfo("Crop Management System", 'Please enter anmount')
            else:
                con = connect('localhost', 'root', 'nimit', 'nt')
                cur = con.cursor()
                cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
                record = cur.fetchone()
                if record:
                    cur.execute(
                        "update cropdata set amount='%s' where recieptno='%s' " % (amount, recieptno))
                    con.commit()
                    mb.showinfo("Crop Management System", 'Record Updated')
                else:
                    mb.showinfo("Crop Management System", 'Record not Found!!')
                con.close()
                self.t1.delete(0, 'end')
                self.t2.delete(0, 'end')
                exit()

    def exitprog(self):
        exit()


class Payment(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='Reciept No.')
        self.t1 = Entry(self, bd=2)
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='Payment Status')
        self.t2 = Entry(self, bd=2)
        self.b1 = Button(self, text='Submit', command=lambda: self.insert(), bd=5, bg='light gray',width=15, height=1)
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')

        self.h.grid(row=0, columnspan=2)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l2.grid(row=2)
        self.l3.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.b1.grid(row=4, column=0)
        self.b6.grid(row=4, column=1)
        self.pack()

    def insert(self):
        recieptno = self.t1.get()
        payment_status = self.t2.get()
        if recieptno == '':
            mb.showinfo("Crop Management System", 'Please enter reciept no.')
        elif payment_status == '':
            mb.showinfo("Crop Management System", 'Please enter payment status')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropdata where recieptno='%s'" % recieptno)
            record = cur.fetchone()
            if record:
                cur.execute(
                    "update cropdata set payment_status='%s' where recieptno='%s' " % (
                        payment_status, recieptno))
                con.commit()
                mb.showinfo("Crop Management System", 'Record Updated')
            else:
                mb.showinfo("Crop Management System", 'Record not Found!!')
            con.close()
            self.t1.delete(0, 'end')
            self.t2.delete(0, 'end')
            exit()

    def exitprog(self):
        exit()
