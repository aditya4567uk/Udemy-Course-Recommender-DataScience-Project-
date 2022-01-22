# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:20:57 2021

@author: adity
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import*
from tkinter import messagebox
import tkinter.font as font

data =pd.read_csv(r"C:\Users\adity\Desktop\html\py-project\7. Udemy Courses.csv")

root=Tk()

root.title("Udemy Course recommender")
root.iconbitmap('C:/Users/adity/Desktop/html/py-project/icon.ico')
root.geometry("1400x900")
myFont = font.Font(family='Helvetica', size=20, weight='bold')
myFont1 = font.Font(family='Helvetica', size=10, weight='bold')
mlbl=Label(root,text="WELCOME TO UDEMY COURSE RECOMMENDER",pady=10)
mlbl['font']=myFont
mlbl.grid(row=0,column=1)

avaop=Label(root,text="AVAILABLE OPTIONS---CHOOSE ANY OF BELOW",padx=10,pady=100).grid(row=1,column=0)
# labeling option1
mlbl1=Label(root,text="Different courses",padx=10,)
mlbl1['font']=myFont1
mlbl1.grid(row=2,column=0)

def op1():
    top=Toplevel()
    top.geometry("300x300")
    global arr1
    global lbl
    arr1=data.subject.unique()
    for i in range(0,len(arr1)):
        lbl=Label(top,text=arr1[i],padx=20,pady=20)
        lbl.pack()
        

#Defining Button for Option1
btn1=Button(root,text="Show data",command=op1).grid(row=2,column=2)

# labeling option2
mlbl2=Label(root,text="All available free courses",padx=10)
mlbl2['font']=myFont1
mlbl2.grid(row=3,column=0)

def op2():
    top=Toplevel()
    top.geometry("600x300")
    global lbl
    lbl=Label(top,text=data[data.is_paid==False]).pack()

#Defining Button for Option2
btn2=Button(root,text="Show data",command=op2).grid(row=3,column=2)


# labeling option3
mlbl3=Label(root,text="All available Paid courses",padx=10,pady=10)
mlbl3['font']=myFont1
mlbl3.grid(row=4,column=0)


def op3():
    top=Toplevel()
    top.geometry("600x300")
    global lbl
    lbl=Label(top,text=data[data.is_paid==True]).pack()
    

#Defining Button for Option3
btn3=Button(root,text="Show data",command=op3).grid(row=4,column=2)

# labeling option4
mlbl4=Label(root,text="Showing data of top selling courses",padx=10,pady=10)
mlbl4['font']=myFont1
mlbl4.grid(row=5,column=0)

def op4():
    top=Toplevel()
    top.geometry("600x300")
    global lbl
    lbl=Label(top,text=data.sort_values('num_subscribers',ascending=False)).pack()


#Defining Button for Option4
btn4=Button(root,text="Show data",command=op4).grid(row=5,column=2)


# labeling option5
mlbl5=Label(root,text="Showing data of least selling courses",padx=10,pady=10)
mlbl5['font']=myFont1
mlbl5.grid(row=6,column=0)

def op5():
    top=Toplevel()
    top.geometry("600x300")
    global lbl
    lbl=Label(top,text=data.sort_values('num_subscribers')).pack()

#Defining Button for Option5
btn5=Button(root,text="Show data",command=op5).grid(row=6,column=2)


# labeling option6
mlbl6=Label(root,text="Choose particular course with price range of 500",padx=10,pady=10)
mlbl6['font']=myFont1
mlbl6.grid(row=7,column=0)

def en1():
    top1=Toplevel()
    top1.geometry("600x600")
    global lblb
    lblb=Label(top1,text=data[(data.subject=="Musical instrument")&(data.price<"500")]).pack()

def en2():
    top1=Toplevel()
    top1.geometry("600x600")
    global lblb
    lblb=Label(top1,text=data[(data.subject=="Business finance")&(data.price<"500")]).pack()
    
def en3():
    top1=Toplevel()
    top1.geometry("600x600")
    global lblb
    lblb=Label(top1,text=data[(data.subject=="Graphic Design")&(data.price<"500")]).pack()

def en4():
    top1=Toplevel()
    top1.geometry("600x600")
    global lblb
    lblb=Label(top1,text=data[(data.subject=="Web development")&(data.price<"500")]).pack()


def op6():
    top=Toplevel()
    top.geometry("700x700")
    global lbl,bt1,bt2,bt3,bt4
    lbl1=Label(top,text="Choose any option for which you are looking courses").pack()
    bt1=Button(top,text="Musical instrument",command=en1).pack()
    bt2=Button(top,text="Business finance",command=en2).pack()
    bt3=Button(top,text="Graphic Design",command=en3).pack()
    bt4=Button(top,text="Web development",command=en4).pack()
    lbl2=Label(top,text="Select any option").pack()
    #lbl=Label(top,text=data.sort_values('num_subscribers')).pack()

#Defining Button for Option6
btn6=Button(root,text="Show data",command=op6).grid(row=7,column=2)

# labeling option7
mlbl7=Label(root,text="showing results by using specific word",padx=10,pady=10)
mlbl7['font']=myFont1
mlbl7.grid(row=8,column=0)

def op7():
    global s,lbl,e,d1,lbl1
    top=Toplevel()
    top.geometry("700x700")
    lbl1=Label(top,text="Python courses you might be looking for").pack()
    d1=data[data.course_title.str.contains("Python")]
    lbl=Label(top,text=d1).pack()

#Defining Button for Option7
btn7=Button(root,text="Show data",command=op7).grid(row=8,column=2)


# labeling option8
mlbl8=Label(root,text="showing courses published in 2017",padx=10,pady=10)
mlbl8['font']=myFont1
mlbl8.grid(row=9,column=0)

def op8():
    top=Toplevel()
    top.geometry("700x700")
    global yr,lbl
    yr=2017
    data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
    data.dtypes
    data['Year']=data['published_timestamp'].dt.year
    lbl=Label(top,text=data[data.Year==2017]).pack()

#Defining Button for Option8
btn8=Button(root,text="Show data",command=op8).grid(row=9,column=2)

# labeling option9
mlbl9=Label(root,text="max subscribers for each lvl courses (beginner , interm , advanced)",padx=10,pady=10)
mlbl9['font']=myFont1
mlbl9.grid(row=10,column=0)

def op9():
    top=Toplevel()
    top.geometry("700x300")
    global lbl ,lbl1,a,scatter3
    y = [161029,5172,29167]
    abc = ['beginner', 'expert', 'intermediate']
    plt.bar(np.arange(len(y)),y,tick_label = abc, width=0.4)
    a=plt.show()
    scatter3 = FigureCanvasTkAgg(a, top)
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    lbl=Label(top,text=data.level.unique).pack()
    lbl1=Label(top,text=data.groupby('level')['num_subscribers'].max()).pack()

#Defining Button for Option9
btn9=Button(root,text="Show data",command=op9).grid(row=10,column=2)

def credit():
    top=Toplevel()
    top.geometry("300x150")
    global lb1
    lb1=Label(top,text="20MIP10008---ADITYA KUMAR\n20MIP10002---AKANKSHA VERMA\n20MIP10018---CHARCHIT JAIN\n20MIP10035---ISHIKA SHRIVASTAV\n20MIP10044---PARAS YADAV").pack()

frame=LabelFrame(root,text="",padx=20,pady=20).grid(row=11,column=1,sticky=W+E)
b=Button(frame,text="Exit",width=20,command=root.destroy).grid(row=12,column=0)
b1=Button(frame,text="Credit",width=20,command=credit).grid(row=12,column=2,sticky=E)


root.mainloop()