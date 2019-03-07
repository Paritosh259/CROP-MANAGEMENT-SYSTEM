from tkinter import *
import UpdateRecord

class Change(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='')
        self.l2 = Label(self, text='')
        self.b1 = Button(self, text='Update Name', command=lambda: self.uname(), width=18, height=1, bd=5, bg='light gray')
        self.b2 = Button(self, text='Update Father\'s name', command=lambda: self.ufname(), width=18, height=1, bd=5, bg='light gray')
        self.b3 = Button(self, text='Update Date', command=lambda: self.udate(), width=18, height=1, bd=5, bg='light gray')
        self.b4 = Button(self, text='Update Account No.', command=lambda: self.uacc(), width=18, height=1, bd=5, bg='light gray')
        self.b5 = Button(self, text='Update Category', command=lambda: self.ucat(), width=18, height=1, bd=5, bg='light gray')
        self.b6 = Button(self, text='Update Weight', command=lambda: self.uwt(), width=18, height=1, bd=5, bg='light gray')
        self.b7 = Button(self, text='Update Amount', command=lambda: self.uamt(), width=18, height=1, bd=5, bg='light gray')
        self.b8 = Button(self, text='Update Payment Status', command=lambda: self.ups(), width=18, height=1, bd=5, bg='light gray')
        self.b9 = Button(self, text='Exit', width=15, height=1, command=lambda: self.exitprog(), bd=5, bg='light gray')
        self.l2 = Label(self, text='')
        self.l3 = Label(self, text='')
        self.l4 = Label(self, text='')
        self.l5 = Label(self, text='')
        self.l6 = Label(self, text='')

        '''creating the layouts'''
        self.h.grid(row=0, columnspan=3)
        self.l1.grid(row=1)
        self.l2.grid(row=2)
        self.b1.grid(row=3, column=1)
        self.b2.grid(row=3, column=2)
        self.l3.grid(row=4)
        self.b3.grid(row=5, column=1)
        self.b4.grid(row=5, column=2)
        self.l4.grid(row=6)
        self.b5.grid(row=7, column=1)
        self.b6.grid(row=7, column=2)
        self.l5.grid(row=8)
        self.b7.grid(row=9, column=1)
        self.b8.grid(row=9, column=2)
        self.l6.grid(row=10)
        self.b9.grid(row=11, columnspan=3)


        self.pack()

    def uname(self):
        other = Tk()
        root = UpdateRecord.Name(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def ufname(self):
        other = Tk()
        root = UpdateRecord.Fname(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def udate(self):
        other = Tk()
        root = UpdateRecord.Date(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def uacc(self):
        other = Tk()
        root = UpdateRecord.Account(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def ucat(self):
        other = Tk()
        root = UpdateRecord.Category(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def uwt(self):
        other = Tk()
        root = UpdateRecord.Weight(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def uamt(self):
        other = Tk()
        root = UpdateRecord.Amount(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def ups(self):
        other = Tk()
        root = UpdateRecord.Payment(other)
        other.title('Crop Management System Update Record')
        other.geometry('500x800')
        other.mainloop()

    def exitprog(self):
        exit()