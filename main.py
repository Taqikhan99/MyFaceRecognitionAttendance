from os import write
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import numpy as np
import cv2


# class Register:

#     def __init__(self, root):
        
#         self.root = root
#         self.root.title("Registeration form")
#         self.root.geometry("900x600+300+100")
#         self.root.maxsize("900", "600")
#         self.root.minsize("900", "600")
        
#         # boolean to check if pictures are taken or not
#         self.picturesTaken = False

#         # setting bg image
#         self.bImg = Image.open("images/bg1.jpg")
#         self.bg = ImageTk.PhotoImage(self.bImg)
#         bg = Label(self.root, image=self.bg).place(
#             x=0, y=0, relwidth=1, relheight=1)

#         frame1 = Frame(self.root, bg='white')
#         frame1.place(x=100, y=50, width=700, height=500)

#         rTitle = Label(frame1, text="REGISTER PAGE",
#                        font="Arial 22 bold", fg="red").place(x=230, y=20)

#         # fname label and text box

#         fname = Label(frame1, text="First Name", font="helvetica 14 ",
#                       fg="Gray", bg="white").place(x=70, y=100)
#         self.txtFname = Entry(frame1, font="helvetica 14", bg="lightgray")
#         self.txtFname.place(x=70, y=130)

#         # Lname label and text box
#         lname = Label(frame1, text="Last Name", font="helvetica 14 ",
#                       fg="Gray", bg="white").place(x=400, y=100)
#         self.txtLname = Entry(frame1, font="helvetica 14", bg="lightgray")
#         self.txtLname.place(x=400, y=130)

#         # Email lbl and textbox
#         email = Label(frame1, text="Email", font="helvetica 14 ",
#                       fg="Gray", bg="white").place(x=70, y=200)
#         self.txtEmail = Entry(frame1, font="helvetica 14", bg="lightgray")
#         self.txtEmail.place(x=70, y=230)
#         # Age
#         age = Label(frame1, text="Age", font="helvetica 14 ",
#                     fg="Gray", bg="white").place(x=400, y=200)
#         self.txtAge = Entry(frame1, font="helvetica 14", bg="lightgray")
#         self.txtAge.place(x=400, y=230)

#         # Password
#         password = Label(frame1, text="Password", font="helvetica 14 ",
#                          fg="Gray", bg="white").place(x=70, y=300)
#         self.txtPass = Entry(frame1, font="helvetica 14", bg="lightgray",show='*')
#         self.txtPass.place(x=70, y=330)

#         cPassword = Label(frame1, text="Confirm Password",
#                           font="helvetica 14 ", fg="Gray", bg="white").place(x=400, y=300)
#         self.txtCpass = Entry(frame1, font="helvetica 14", bg="lightgray",show='*')
#         self.txtCpass.place(x=400, y=330)
#         # buttons
#         # Take photo
#         tkPhotobtn = Button(frame1, text="TAKE PHOTOS", fg="green", bg="lightgray", width="12", height="1",
#                             font="helvetica 12 bold", bd=0, cursor="hand2", command=self.takeImages).place(x=70, y=400)

#         # reg btn

#         regbtn = Button(frame1, text="REGISTER", fg="green", bg="lightgray", width="12", height="1",
#                         font="helvetica 12 bold", bd=0, cursor="hand2", command=self.registerData).place(x=70, y=440)

#         # Go to login page using login btn
#         loginbtn = Button(frame1, text="LOGIN", fg="blue", bg="lightgray", width="12", height="1",
#                           font="helvetica 12 bold", bd=0, cursor="hand2", command=self.login_window).place(x=490, y=440)

#     # go to reg window

#     def login_window(self):
#         self.root.destroy()
#         import loginpage



#     def takeImages(self):

#         # check if any field is empty
#         if self.txtFname.get() == "" or self.txtLname.get() == "" or self.txtEmail.get() == "" or self.txtAge.get() == "" or self.txtPass.get() == "" or self.txtCpass.get() == "":
#             messagebox.showerror(
#                 'Error', "Please Fill the data first", parent=self.root)
#         else:


#             faceClassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#             cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#             img_Id=1
#             while(True):
        
#                 ret,myframe=cap.read()
#                 grayImg = cv2.cvtColor(myframe,cv2.COLOR_BGR2GRAY)
#                 faces = faceClassifier.detectMultiScale(grayImg, 3, 5)
#                 for(x,y,w,h) in faces:
#                     print(x,y,w,h)
#                     roiGray=grayImg[y:y+h,x:x+w]
                
#                     imgItem="images/students/std-"+self.txtFname.get()+"_"+self.txtLname.get()+"."+str(img_Id)+".png"
#                     cv2.imwrite(imgItem,roiGray)

            

#                 img_Id+=1
#                 cv2.imshow('frame',myframe)

#                 # we will take 20 images
#                 if cv2.waitKey(1)==13 or img_Id==70:
                
#                     self.picturesTaken=True
#                     break
#             messagebox.showinfo('Success',"Images saved successfully")       
#             cap.release()
#             cv2.destroyAllWindows()
        
        
        

#     # getting data from textbox

#     def registerData(self):

#         # check if any field is empty
#         if self.txtFname.get() == "" or self.txtLname.get() == "" or self.txtEmail.get() == "" or self.txtAge.get() == "" or self.txtPass.get() == "" or self.txtCpass.get() == "":
#             messagebox.showerror(
#                 'Error', "All fields are required", parent=self.root)

#         # check if password and confirm password are same or not
#         elif self.txtPass.get() != self.txtCpass.get():
#             messagebox.showerror(
#                 "Error", "Password and Confrim password not match", parent=self.root)
#         elif self.picturesTaken == False:
#             messagebox.showerror(
#                 "Error", "Please take pictures first", parent=self.root)
#         # otherwise success
#         else:
#             try:
#                 con = pymysql.connect(
#                     host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
#                 cur = con.cursor()


# # cursor helps in performing queries
#                 cur.execute("insert into tbl_students(fName,lName,email,age,password) values(%s,%s,%s,%s,%s)",
#                             (
#                                 self.txtFname.get(),
#                                 self.txtLname.get(),
#                                 self.txtEmail.get(),
#                                 self.txtAge.get(),
#                                 self.txtPass.get()
#                             ))
#                 con.commit()
#                 con.close()
#                 messagebox.showinfo("Success", "Registration successful")
#                 # incrementing id
                
#                 self.root.destroy()
#                 import loginpage

#             except Exception as es:
#                 messagebox.showerror(
#                     "Error", f"Error due to {str(es)}", parent=self.root)




# regPage = Tk()
# obj = Register(regPage)
# regPage.mainloop()
