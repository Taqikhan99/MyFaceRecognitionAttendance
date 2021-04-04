from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
import cv2
import numpy as np
import time
import os
from datetime import datetime



global currentUser
currentUserId=0

currentUserName=""

global loginOpen
loginOpen=False

# My Login Class
class LoginPage:
    regopen=False
    homeopen=False
    def __init__(self,root):
        global loginOpen
        loginOpen=True

        self.root=root
        self.root.title("Login form")
        self.root.geometry("900x600+300+100")
        self.root.maxsize("900","600")
        self.root.minsize("900","600")

        # setting bg image
        self.bImg=Image.open("images/bg1.jpg")
        self.bg=ImageTk.PhotoImage(self.bImg)
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        # Setting the login frame
        loginframe=Frame(self.root,bg='#7ef9ff')
        loginframe.place(x=100,y=50,width=700,height=500)

        loginTitle=Label(loginframe,text="LOGIN PAGE" ,font="Arial 26 bold underline", fg="blue",bg="#73c2fb").place(x=250,y=20)

        # email label and textbox
        email=Label(loginframe,text="Email",font="helvetica 20 bold", fg="black",bg="#7ef9ff").place(x=170,y=100)
        self.txtEmail=Entry(loginframe,font="helvetica 16", bg="white" ,width=30)
        self.txtEmail.place(x=170,y=140)
         # Password
        password=Label(loginframe,text="Password",font="helvetica 20 bold", fg="black",bg="#7ef9ff").place(x=170,y=200)
        self.txtPass=Entry(loginframe,font="helvetica 16", bg="white" ,width=30,show='*')
        self.txtPass.place(x=170,y=240)
        
        

        btnreg=Button(loginframe,text="Register new Account?",font="helvetica 11",fg="red",bd=0,bg="#7ef9ff",cursor="hand2", command=self.toRegPage).place(x=170,y=280)
        

        loginbtn=Button(loginframe,text="LOGIN",fg="blue",bg="lightgray",width="16",height="2",font="helvetica 12 bold",bd=0,cursor="hand2",command=self.loginVals).place(x=280,y=320)

   
    def loginVals(self):
        if self.txtEmail.get()=="" or self.txtPass.get()=="":
            messagebox.showerror('Error','Please fill all fields.',parent=self.root)
        
        else:
            
            con=pymysql.connect(host="127.0.0.1",user="root",password="Kiet2018",database="attendancesystemdb")
            cur=con.cursor()
            cur.execute("select * from tbl_students where email=%s and password=%s",(self.txtEmail.get(),self.txtPass.get()))
            row=cur.fetchone()
           
            print(row)
            if row==None:
                messagebox.showerror("Error","Invalid email or password!",parent=self.root)
            else:
                global currentUserId
                currentUserId=row[0]
                print(currentUserId)
                messagebox.showinfo("Success","Login successful",parent=self.root)
                self.toHomePage()
                     
            # except Exception as es:
            #     messagebox.showerror("Error",f"Error due to: {str(es)}")

       
    def toRegPage(self):
        # if self.regopen==False:
            
        #     self.newWindow=Toplevel(self.root)
        #     self.app=Register(self.newWindow)
            
        #     self.regopen=True
        # else:
        #     messagebox.showerror("Error","Reg page already opened")
        self.root.destroy()
        newroot=Tk()
        app=Register(newroot)
        newroot.mainloop()

    def toHomePage(self):
            
        self.root.destroy()
        newroot=Tk()
        app=MainWindow(newroot)
        newroot.mainloop() 

#********************************Login class ends*******************************# 

# My Registration class
class Register:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Registeration form")
        self.root.geometry("900x600+300+100")
        self.root.maxsize("900", "600")
        self.root.minsize("900", "600")
        
        

        # setting bg image
        self.bImg = Image.open("images/bg1.jpg")
        self.bg = ImageTk.PhotoImage(self.bImg)
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg='white')
        frame1.place(x=100, y=50, width=700, height=500)

        rTitle = Label(frame1, text="REGISTER PAGE",
                       font="Arial 22 bold", fg="red").place(x=230, y=20)

        # fname label and text box

        fname = Label(frame1, text="First Name", font="helvetica 14 ",
                      fg="Gray", bg="white").place(x=70, y=100)
        self.txtFname = Entry(frame1, font="helvetica 14", bg="lightgray")
        self.txtFname.place(x=70, y=130)

        # Lname label and text box
        lname = Label(frame1, text="Last Name", font="helvetica 14 ",
                      fg="Gray", bg="white").place(x=400, y=100)
        self.txtLname = Entry(frame1, font="helvetica 14", bg="lightgray")
        self.txtLname.place(x=400, y=130)

        # Email lbl and textbox
        email = Label(frame1, text="Email", font="helvetica 14 ",
                      fg="Gray", bg="white").place(x=70, y=200)
        self.txtEmail = Entry(frame1, font="helvetica 14", bg="lightgray")
        self.txtEmail.place(x=70, y=230)
        # Age
        age = Label(frame1, text="Age", font="helvetica 14 ",
                    fg="Gray", bg="white").place(x=400, y=200)
        self.txtAge = Entry(frame1, font="helvetica 14", bg="lightgray")
        self.txtAge.place(x=400, y=230)

        # Password
        password = Label(frame1, text="Password", font="helvetica 14 ",
                         fg="Gray", bg="white").place(x=70, y=300)
        self.txtPass = Entry(frame1, font="helvetica 14", bg="lightgray",show='*')
        self.txtPass.place(x=70, y=330)

        cPassword = Label(frame1, text="Confirm Password",
                          font="helvetica 14 ", fg="Gray", bg="white").place(x=400, y=300)
        self.txtCpass = Entry(frame1, font="helvetica 14", bg="lightgray",show='*')
        self.txtCpass.place(x=400, y=330)
        # buttons

        # reg btn

        regbtn = Button(frame1, text="REGISTER", fg="green", bg="lightgray", width="12", height="1",
                        font="helvetica 12 bold", bd=0, cursor="hand2", command=self.registerData).place(x=70, y=440)

        # Go to login page using login btn
        loginbtn = Button(frame1, text="LOGIN", fg="blue", bg="lightgray", width="12", height="1",
                          font="helvetica 12 bold", bd=0, cursor="hand2", command=self.toLoginPage).place(x=490, y=440)

    def toLoginPage(self):
        
        self.root.destroy()
        newroot=Tk()
        app=LoginPage(newroot)
        newroot.mainloop()

    # getting data from textbox

    def registerData(self):

        # check if any field is empty
        if self.txtFname.get() == "" or self.txtLname.get() == "" or self.txtEmail.get() == "" or self.txtAge.get() == "" or self.txtPass.get() == "" or self.txtCpass.get() == "":
            messagebox.showerror(
                'Error', "All fields are required", parent=self.root)

        # check if password and confirm password are same or not
        elif self.txtPass.get() != self.txtCpass.get():
            messagebox.showerror(
                "Error", "Password and Confrim password not match", parent=self.root)

        # otherwise success
        else:
            try:
                con = pymysql.connect(
                    host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
                cur = con.cursor()

                cur.execute("insert into tbl_students(fName,lName,email,age,password) values(%s,%s,%s,%s,%s)",
                            (
                                self.txtFname.get(),
                                self.txtLname.get(),
                                self.txtEmail.get(),
                                self.txtAge.get(),
                                self.txtPass.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration successful")
                
                # go to login page after successful registration
                self.toLoginPage()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to {str(es)}", parent=self.root)

# *********************Register class ends*******************#

# My HomePage Window
class MainWindow:
    # boolean to check if pictures are taken or not
    picturesTaken = False
    def __init__(self, root):
        print(currentUserId)
         
        self.root = root
        self.root.title("Attendance System")
        self.root.geometry("900x650+300+100")
        self.root.maxsize("900", "650")
        self.root.minsize("900", "650")

        # setting bg image
        self.bImg = Image.open("images/wallpaper.jpg")
        self.bImg = self.bImg.resize((900, 650), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.bImg)
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        topImageFrame = Frame(self.root, bg="gray")
        topImageFrame.place(x=0, y=0, relwidth=1, height="100")

        # image of faces
        img = Image.open('images/facialrecognition.png')
        img = img.resize((430, 100), Image.ANTIALIAS)
        self.topImg = ImageTk.PhotoImage(img)

        aIimg = Image.open('images/artificial.jpg')
        aIimg = aIimg.resize((430, 100), Image.ANTIALIAS)
        self.aiImage = ImageTk.PhotoImage(aIimg)

        # place faces image
        topImagelbl = Label(topImageFrame, image=self.topImg, bd=0)
        topImagelbl.place(x=460, y=0)

        # place Ai image
        topImagelbl = Label(topImageFrame, image=self.aiImage, bd=0)
        topImagelbl.place(x=10, y=0)

        # label for main heading
        self.mainHead = Label(self.root, bg="white", fg="red",
                              text="THA ATTENDANCE SYSTEM", width=53, height=2, font="arial 20 bold")
        self.mainHead.place(x=0, y=105)

        # timelabel
        self.showTime()

    # button for takingpics
        btnPhotos = Button(self.root, text="Take Photos", fg="red", bg="white",
                             width="13", height="2", font="helvetica 18 bold", command=self.takeImages)
        btnPhotos.place(x=100, y=300)
        # button for attendance
        
        btnAttendance = Button(self.root, text="Take Attendance", fg="red",
                               bg="white", width="13", height="2", font="helvetica 18 bold",command=self.faceRecognition)
        btnAttendance.place(x=340, y=300)
        # button for my records
        btnRecords = Button(self.root, text="My Records", fg="red",
                            bg="white", width="13", height="2", font="helvetica 18 bold")
        btnRecords.place(x=100, y=400)

        # button for training data
        btnTraining = Button(self.root, text="Train Data", fg="red", bg="white",
                             width="13", height="2", font="helvetica 18 bold", command=self.trainData)
        btnTraining.place(x=580, y=300)

        # logout button
        btnLogout = Button(self.root, text="Logout", fg="white", bg="#282828",
                           font="helvetica 14", bd=0, width=10, command=self.logOut)

        btnLogout.place(x=740, y=600)

          # Take photo
    def takeImages(self):

        faceClassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        img_Id=1
        while(True):
        
            ret,myframe=cap.read()
            grayImg = cv2.cvtColor(myframe,cv2.COLOR_BGR2GRAY)
            faces = faceClassifier.detectMultiScale(grayImg, 3, 5)
            for(x,y,w,h) in faces:
                print(x,y,w,h)
                roiGray=grayImg[y:y+h,x:x+w]
                
                imgItem="images/students/std-"+str(currentUserId)+"."+str(img_Id)+".png"
                cv2.imwrite(imgItem,roiGray)

            

            img_Id+=1
            cv2.imshow('frame',myframe)

                # we will take 50 images
            if cv2.waitKey(1)==13 or img_Id==50:
                
                self.picturesTaken=True
                break
        messagebox.showinfo('Success',"Images saved successfully")       
        cap.release()
        cv2.destroyAllWindows()
        

    # function to show time
    def showTime(self):

        hour = time.strftime("%H")
        minute = time.strftime("%M")
        seconds = time.strftime("%S")
        mytimelbl = Label(self.mainHead, bg="white",
                          font="helvetica 20 bold", fg="green")
        mytimelbl.config(text=hour+":"+minute+":"+seconds)
        mytimelbl.place(x=10, y=15)
        mytimelbl.after(1000, self.showTime)


    # function to train data
    def trainData(self):
        
        myDirectory = ("images\students")
        path = [os.path.join(myDirectory, file)
                         for file in os.listdir(myDirectory)]
        faces = []
        ids = []
    
        for image in path:
            img = Image.open(image).convert('L')  # convert to gray
            imageNp = np.array(img, 'uint8')
            
            id = int(os.path.split(image)[1].split('-')[1].split('.')[0])
            print(id)

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training', imageNp)
            cv2.waitKey(1) == 13
             
        # now train the classifier
        ids=np.array(ids) 
        classifier =cv2.face.LBPHFaceRecognizer_create()
        print(ids)
        classifier.train(faces, ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result", "Training data completed")

    # face recognition
    def faceRecognition(self):
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        # taking video
        cap=cv2.VideoCapture(0)

        while True:
            ret,img=cap.read()
            print(ret)
            
            img=self.recognizeFace(img,clf,faceCascade)
            cv2.imshow("Face recognition",img)

            if cv2.waitKey(1)==13:
                break
        self.takingAttendance()
        cap.release()
        cv2.destroyAllWindows()

    # draw boundary
    def drawBoundary(self,img,classifier,scale,minNeighbour,color,text,clf):
        
        grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(grayImage,scale,minNeighbour)

        coordinates=[]
        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(grayImage[y:y+h,x:x+w])
            
            print(id)
            
            confidence=int(100*(1-predict/300))


            con = pymysql.connect(
                    host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
            cur = con.cursor()
            cur.execute("select concat(fName,'',lName) from tbl_students where studentid="+str(id))
            name=cur.fetchone()
            # print(name)

            cur.execute("Select age from tbl_students where studentid="+str(id))
            age=cur.fetchone()
            

            # confidence
            if confidence>75:
                cv2.putText(img,f"Name: {name[0]}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,200,0),2)
                cv2.putText(img,f"Age: {age[0]}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,200,0),2)
                cv2.putText(img,f"Conf: {confidence}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,200,0),2)

            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,200),3)
                cv2.putText(img,"Unknown face",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,200),2)

            
            coordinates=[x,y,w,h]
        
        return coordinates

    def recognizeFace(self,img,clf,faceCascade):
        coord=self.drawBoundary(img,faceCascade,1.1,5,(255,255,0),"Face",clf)
        
        return img

    # attendance marking func
    def takingAttendance(self):
        print(currentUserId)
        currentDate=datetime.today().strftime("%d-%m-%Y")
        print(currentDate)

        currentTime=time.strftime("%H:%M:%S")
        print(currentTime)

        try:
            con = pymysql.connect(
                    host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
            cur = con.cursor()
            # we make sure one student can mark attendance only one time a day.
            cur.execute("Select * from tbl_attendance where studentid= %s"+" and  date= %s",(str(currentUserId),currentDate))
            myAttendance=cur.fetchone()
            print(myAttendance)
        except Exception as es:
            messagebox.showerror("exception",str(es))

        if myAttendance is not None:
            messagebox.showerror("attendance status","User "+str(currentUserId)+" attendance is already marked for date: "+currentDate)
        else:

            # marking attendance
            con = pymysql.connect(
                    host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
            curAttend = con.cursor()
            curAttend.execute("insert into tbl_attendance (date,time,attendaceMarked,studentid) values(%s,%s,%s,%s)",(currentDate,currentTime,str(1),str(currentUserId)))

            con.commit()
            con.close()
            messagebox.showinfo("attendance status","Attendance marked successfully")
            


    def logOut(self):
        self.root.destroy()
        newroot=Tk()
        app=LoginPage(newroot)
        newroot.mainloop()
        

if __name__=="__main__":
    logPage=Tk()
    obj=LoginPage(logPage)    
    logPage.mainloop()
