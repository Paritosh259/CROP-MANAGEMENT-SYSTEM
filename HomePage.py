from tkinter import *
from tkinter import messagebox as mb
from pymysql import *

import AddRecord
import ChangeRecord
import DeleteRecord
import SearchRecord


class Home(Frame):
    def __init__(self, master):
        super().__init__(master)

        '''creating the required labels buttons and text boxes'''
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='select the task:')
        self.l1.config(font=('algerian', 12))
        self.b1 = Button(self, text='Add record', width=15, height=1, command=lambda: self.add(), bd=5, bg='light gray')
        self.b2 = Button(self, text='Delete record', width=15, height=1, command=lambda: self.delete(), bd=5, bg='light gray')
        self.b3 = Button(self, text='Search record', width=15, height=1, command=lambda: self.search(), bd=5, bg='light gray')
        self.b4 = Button(self, text='Update record', width=15, height=1, command=lambda: self.change(), bd=5, bg='light gray')
        self.b5 = Button(self, text='Show All records', width=15, height=1, command=lambda: self.show(), bd=5, bg='light gray')
        self.b6 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')
        self.b7 = Button(self, text='Total Amount', width=15, height=1, command=lambda: self.total(),  bd=5, bg='light gray')
        self.b8 = Button(self, text='Pending Amount', width=15, height=1, command=lambda: self.pending(), bd=5, bg='light gray')
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='')
        self.l4 = Label(self, text='')
        self.l5 = Label(self, text='')
        self.l6 = Label(self, text='')

        '''creating the layouts'''
        self.h.grid(row=0, columnspan=4)
        self.l1.grid(row=1)
        self.l2.grid(row=2)
        self.b1.grid(row=3, column=1)
        self.b2.grid(row=3, column=2)
        self.l3.grid(row=4)
        self.b3.grid(row=5, column=1)
        self.b4.grid(row=5, column=2)
        self.l4.grid(row=6)
        self.b5.grid(row=7, column=1)
        self.b7.grid(row=7, column=2)
        self.l5.grid(row=8)
        self.b8.grid(row=9, column=1)
        self.l5.grid(row=8)
        self.b6.grid(row=9, column=2)

        self.pack()

    def add(self):
        other = Tk()
        root = AddRecord.Add(other)
        other.title('Crop Management System Add Record')
        other.geometry('500x800')
        other.mainloop()

    def delete(self):
        other = Tk()
        root = DeleteRecord.Delete(other)
        other.title('Crop Management System Delete Record')
        other.geometry('500x500')
        other.mainloop()

    def search(self):
        other = Tk()
        root = SearchRecord.Search(other)
        other.title('Crop Management System Search Record')
        other.geometry('500x500')
        other.mainloop()

    def change(self):
        other = Tk()
        root = ChangeRecord.Change(other)
        other.title('Crop Management System Change Record')
        other.geometry('500x800')
        other.mainloop()

    def show(self):
        con = connect('localhost', 'root', 'nimit', 'nt')
        cur = con.cursor()
        cur.execute("select * from cropdata")
        record = cur.fetchall()
        mb.showinfo("Crop Management System All Records", record)
        cur.close()

    def total(self):
        con = connect('localhost', 'root', 'nimit', 'nt')
        cur = con.cursor()
        cur.execute("select sum(amount) as totalsum from cropdata")
        record = cur.fetchall()
        mb.showinfo("Crop Management System All Records", record)
        cur.close()

    def pending(self):
        con = connect('localhost', 'root', 'nimit', 'nt')
        cur = con.cursor()
        cur.execute("select sum(amount) as totalsum from cropdata where payment_status='pending'")
        record = cur.fetchall()
        mb.showinfo("Crop Management System All Records", record)
        cur.close()


    def exitprog(self):
        exit()
