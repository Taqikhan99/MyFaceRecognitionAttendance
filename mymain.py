
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import numpy as np
import time
import os
import cv2

# from loginpage import LoginPage


# class MainWindow:
    

#     def __init__(self, root):
        
        
#         self.root = root
#         self.root.title("Attendance System")
#         self.root.geometry("900x650+300+100")
#         self.root.maxsize("900", "650")
#         self.root.minsize("900", "650")
# # boolean to check if pictures are taken or not
#         self.picturesTaken = False
#         # setting bg image
#         self.bImg = Image.open("images/wallpaper.jpg")
#         self.bImg = self.bImg.resize((900, 650), Image.ANTIALIAS)
#         self.bg = ImageTk.PhotoImage(self.bImg)
#         bg = Label(self.root, image=self.bg).place(
#             x=0, y=0, relwidth=1, relheight=1)

#         topImageFrame = Frame(self.root, bg="gray")
#         topImageFrame.place(x=0, y=0, relwidth=1, height="100")

#         # image of faces
#         img = Image.open('images/facialrecognition.png')
#         img = img.resize((430, 100), Image.ANTIALIAS)
#         self.topImg = ImageTk.PhotoImage(img)

#         aIimg = Image.open('images/artificial.jpg')
#         aIimg = aIimg.resize((430, 100), Image.ANTIALIAS)
#         self.aiImage = ImageTk.PhotoImage(aIimg)

#         # place faces image
#         topImagelbl = Label(topImageFrame, image=self.topImg, bd=0)
#         topImagelbl.place(x=460, y=0)

#         # place Ai image
#         topImagelbl = Label(topImageFrame, image=self.aiImage, bd=0)
#         topImagelbl.place(x=10, y=0)

#         # label for main heading
#         self.mainHead = Label(self.root, bg="white", fg="red",
#                               text="THA ATTENDANCE SYSTEM", width=53, height=2, font="arial 20 bold")
#         self.mainHead.place(x=0, y=105)

#         # timelabel
#         self.showTime()

#         # button for attendance
#         btnAttendance = Button(self.root, text="Take Attendance", fg="red",
#                                bg="white", width="13", height="2", font="helvetica 18 bold",command=self.faceRecognition)
#         btnAttendance.place(x=100, y=400)
#         # button for my records
#         btnRecords = Button(self.root, text="My Records", fg="red",
#                             bg="white", width="13", height="2", font="helvetica 18 bold")
#         btnRecords.place(x=580, y=300)

#         # button for training data
#         btnTraining = Button(self.root, text="Train Data", fg="red", bg="white",
#                              width="13", height="2", font="helvetica 18 bold", command=self.trainData)
#         btnTraining.place(x=340, y=300)

#         # logout button
#         btnLogout = Button(self.root, text="Logout", fg="white", bg="#282828",
#                            font="helvetica 14", bd=0, width=10, command=self.logOut)

#         btnLogout.place(x=740, y=600)

#           # Take photo
#         tkPhotobtn = Button(self.root, text="Take Photos", fg="red", bg="white",
#                              width="13", height="2", font="helvetica 18 bold", command=self.takeImages)
#         tkPhotobtn.place(x=100,y=300)

#     # function to show time
#     def showTime(self):

#         hour = time.strftime("%H")
#         minute = time.strftime("%M")
#         seconds = time.strftime("%S")
#         mytimelbl = Label(self.mainHead, bg="white",
#                           font="helvetica 20 bold", fg="green")
#         mytimelbl.config(text=hour+":"+minute+":"+seconds)
#         mytimelbl.place(x=10, y=15)
#         mytimelbl.after(1000, self.showTime)



#     # function to take images
#     def takeImages(self):

        
#         faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#         img_Id = 1
#         while(True):

#             ret, myframe = cap.read()
#             grayImg = cv2.cvtColor(myframe, cv2.COLOR_BGR2GRAY)
#             faces = faceClassifier.detectMultiScale(grayImg, 3, 5)
#             for(x, y, w, h) in faces:
#                 print(x, y, w, h)
#                 roiGray = grayImg[y:y+h, x:x+w]

#                 imgItem = "images/students/std-"+self.txtFname.get()+"_"+self.txtLname.get() + \
#                         "."+str(img_Id)+".png"
#                 cv2.imwrite(imgItem, roiGray)

#             img_Id += 1
#             cv2.imshow('frame', myframe)

#                 # we will take 20 images
#             if cv2.waitKey(1) == 13 or img_Id == 70:

#                 self.picturesTaken = True
#                 break
#         messagebox.showinfo('Success', "Images saved successfully")
#         cap.release()
#         cv2.destroyAllWindows()

#     # function to train data
#     def trainData(self):
#         if self.picturesTaken==False:
#             messagebox.showerror("Error","Please take pictures first")
#         else:
#             myDirectory = ("images\students")
#             path = [os.path.join(myDirectory, file)
#                              for file in os.listdir(myDirectory)]

#             faces = []
#             ids = []
        
#         # try:
#             print(path)
#             for image in path:
#                 img = Image.open(image).convert('L')  # convert to gray
#                 imageNp = np.array(img, 'uint8')
             
#                 id = int(os.path.split(image)[1].split('.')[1])
#                 print(id)
#                 name = os.path.split(image)[1].split('.')[0]
#                 print(name)

#                 global currentUser
#                 currentUser=os.path.split(name)[1].split('-')[1]

#                 print(currentUser)
#                 faces.append(imageNp)
#                 ids.append(id)
#                 cv2.imshow('Training', imageNp)
#                 cv2.waitKey(1) == 13
             
#         # now train the classifier
#             ids=np.array(ids) 
#             classifier =cv2.face.LBPHFaceRecognizer_create()
#             classifier.train(faces, ids)
#             classifier.write("classifier.xml")
#             cv2.destroyAllWindows()
#             messagebox.showinfo("result", "Training data completed")

#         # except Exception as es :
#         #     messagebox.showerror("Error",str(es))


#     # face recognition
#     def faceRecognition(self):
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read('classifier.xml')

#         # taking video
#         cap=cv2.VideoCapture(0)

#         while True:
#             ret,img=cap.read()
#             print(ret)
            
#             img=self.recognizeFace(img,clf,faceCascade)
#             cv2.imshow("Face recognition",img)

#             if cv2.waitKey(1)==13:
#                 break
#         cap.release()
#         cv2.destroyAllWindows()



#     # draw boundary
#     def drawBoundary(self,img,classifier,scale,minNeighbour,color,text,clf):
        
#         grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         features=classifier.detectMultiScale(grayImage,scale,minNeighbour)

#         coordinates=[]
#         for (x,y,w,h) in features:
#             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#             id,predict=clf.predict(grayImage[y:y+h,x:x+w])
            
            
            
#             confidence=int(100*(1-predict/300))


#             con = pymysql.connect(
#                     host="127.0.0.1", user="root", password="Kiet2018", database="attendancesystemdb")
#             cur = con.cursor()

#             cur.execute("Select fName from tbl_students where studentid="+str(10))
#             name=cur.fetchone()
#             print(name)
#             print(currentUser)

#             cur.execute("Select age from tbl_students where studentid="+str(10))
#             age=cur.fetchone()
            

#             # confidence
#             if confidence>75:
#                 cv2.putText(img,f"Name: {name[0]}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,200,0),2)
#                 cv2.putText(img,f"Age: {age[0]}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,200,0),2)

#             else:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,200),3)
#                 cv2.putText(img,"Unknown face",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,200),2)

            
#             coordinates=[x,y,w,h]
#         return coordinates

#     def recognizeFace(self,img,clf,faceCascade):
#         coord=self.drawBoundary(img,faceCascade,1.1,5,(255,255,0),"Face",clf)
#         return img

#     # logout func

#     def logOut(self):
#         self.root.destroy()
#         import loginpage



# mainwindow = Tk()
# obj = MainWindow(mainwindow)
# mainwindow.mainloop()

