from tkinter import *
from pymysql import *
from tkinter import messagebox as mb
import HomePage
import SignUp


class Login(Frame):
    def __init__(self, master):
        super().__init__(master)
        '''creating the  labels'''
        self.h = Label(self, text='crop management system', height=3)
        self.h.config(font=('algerian', 20))
        self.l1 = Label(self, text='User ID')
        self.l2 = Label(self, text='Password')
        self.l3 = Label(self, text='')
        self.l4 = Label(self, text='')
        self.t1 = Entry(self, bd=2)
        self.t2 = Entry(self, show='*', bd=2)

        self.b1 = Button(self, text='Login', height=1, width=12, command=lambda: self.authenticate(), bd=5, bg='light gray')

        '''creating the layouts'''
        self.h.grid(row=0, columnspan=3)
        self.l1.grid(row=1, column=0)
        self.t1.grid(row=1, column=1)
        self.l3.grid(row=2)
        self.l2.grid(row=3, column=0)
        self.t2.grid(row=3, column=1)
        self.l4.grid(row=4)
        self.b1.grid(row=5, column=1)

        '''showing the layout'''
        self.pack()

    '''this method is used for the authentication of the user'''
    def authenticate(self):
        userid = self.t1.get()
        password = self.t2.get()
        if userid == '':
            mb.showinfo("Login", 'Please enter userid')
        elif password == '':
            mb.showinfo("Login", 'Please enter password')
        else:
            con = connect('localhost', 'root', 'nimit', 'nt')
            cur = con.cursor()
            cur.execute("select * from cropusers where userid='%s' and password='%s'" % (userid, password))
            record = cur.fetchall()
            if record:
                self.t1.delete(0, 'end')
                self.t2.delete(0, 'end')
                self.homepage()

            else:
                mb.showinfo("Login", 'Invalid User ID or Password')
                self.t1.delete(0, 'end')
                self.t2.delete(0, 'end')

    '''this method is used to move to homepage'''
    def homepage(self):
        other =Tk()
        ob = HomePage.Home(other)
        other.title('Crop management System Homepage')
        other.geometry('500x500')
        other.mainloop()


root = Tk()
object = Login(root)
root.title('Crop Management System Login')
root.geometry('500x500')
root.mainloop()
