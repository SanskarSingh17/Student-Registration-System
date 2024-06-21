from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #====== BG image=====#
        self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

         #====Login Frame=====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=600, y=150, height=340, width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#fc5f76",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Admin login",font=("Goudy old style",15,"bold"),fg="#fb7a90",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90, y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90, y=240,width=350,height=35)


        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#fc5f76",font=("times new roman",20)).place(x=750,y=470,width=180,height=40)
     

    def login_function(self): 
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="admin" or self.txt_user.get()!="admin":
            messagebox.showerror("Error", "Invalid Username/Password",parent=self.root)
        else:
            messagebox. showinfo("Welcome",f"Welcome {self.txt_pass.get()}",parent=self.root)
            self.root.destroy()
            
    


root=Tk()
obj=Login(root)
root.mainloop()
