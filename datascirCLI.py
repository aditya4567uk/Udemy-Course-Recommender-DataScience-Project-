# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:20:57 2021

@author: adity
"""

import pandas as pd
import tableprint as tp
from rich.console import Console
from rich.table import Column, Table
data =pd.read_csv(r"C:\Users\adity\Desktop\html\py-project\7. Udemy Courses.csv")

def ask():
    i=int(input("Do you want to use another option?\n press 1 to use another option or press 2 to exit"))
    if i==1:
        again()
    elif i==2:
        close()
    else:
        print("Exception")

def close():
    ex=input("THANK YOU!!\nPress any key and enter to exit")

def op1():
    print("Total number of different courses")
    arr1=data.subject.unique()
    for i in range(0,len(arr1)):
        print(arr1[i])
#op1()

#function for showing free courses
def op2():
    print("All available free courses")
    print(data[data.is_paid==False])
#op2()

#function for showing free courses
def op3():
    print("All available Paid courses")
    print(data[data.is_paid==True])
#op3()

#function for showing top selling courses
def op4():
    print("Showing data of top selling courses")
    print(data.sort_values('num_subscribers',ascending=False))
#op4()

#function for showing least selling courses
def op5():
    print("Showing data of least selling courses")
    print(data.sort_values('num_subscribers'))
#op5()

#function for showing particular course with price range
def op6():
    #a=input("select any one of these course categories")
    print("1.Musical instrument\n2.Business finance\n3.GraphicDesign\n4.Web development")
    print("Select any number between 1 to 4")
    a=int(input("select any one of these course categories"))
    #print("Select any number between 1 to 4")
    if a==1:
        sub="Musical instrument"
    elif a==2:
        sub="Business finance"
    elif a==3:
        sub="Graphic Design"
    elif a==4:
        sub="Web development"
    else:
        print("PLEASE CHECK YOUR INPUT , CHOOSE INPUT BETWEEN 1 TO 4")
    print("now please enter the max budget you want to spend")
    b=int(input("ENTER YOUR MAX BUDGET"))
    c=str(b)
    print(data[(data.subject==sub)&(data.price<c)])
#op6()

#function for showing results by using specific word
def op7():
    print("Enter the keyword , you want to find courses related to")
    string=input("Enter word")
    d1=data[data.course_title.str.contains(string)]
    print(d1)
#op7()

#function for showing courses published on specific year
def op8():
    yr=int(input("Enter the Year for which you want to find courses"))
    data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
    data.dtypes
    data['Year']=data['published_timestamp'].dt.year
    print(data[data.Year==yr])
#op8()

#function to show max subscribers for each lvl courses (beginner , interm , advanced)
def op9():
    print(data.level.unique)
    print(data.groupby('level')['num_subscribers'].max())
#op9()

#function to show results for specific subjects as well as subcribers
def op10():
    print("Available Subject names\n1.Musical instrument\n2.Business finance\n3.Graphic Design\n4.Web development")
    sub=input("Enter subject name")
    numsub=int(input("enter the minimum number of subcribers"))
    p=data[(data.subject==sub) & (data.num_subscribers>=numsub)]
    print(p)
#op10()


tp.banner("Project Review 2")
tp.banner("Analysis of udemey courses using pandas lib!!")

console = Console()

table = Table(show_header=True, header_style="Yellow")
table.add_column("Reg no", style="dim", width=12)
table.add_column("Name")

table.add_row("20MIP10002","Akanksha Verma")
table.add_row("20MIP10008","Aditya Kumar")
table.add_row("20MIP10018","Charchit Jain")
table.add_row("20MIP10035","Ishika Shrivastav")
table.add_row("20MIP10044","Paras Yadav")
console.print(table)

print("Welcome to course recommender , here you can find out desire course as per your need by using different functions")

table1=Table(show_header=True)
table1.add_column("Option Number")
table1.add_column("Result")

table1.add_row("1","Total number of different courses")
table1.add_row("2","All available free courses")
table1.add_row("3","All available Paid courses")
table1.add_row("4","Showing data of top selling courses")
table1.add_row("5","Showing data of least selling courses")
table1.add_row("6","show particular course with price range")
table1.add_row("7","showing results by using specific word")
table1.add_row("8","show courses published on specific year")
table1.add_row("9","show max subscribers for each lvl courses (beginner , interm , advanced)")
table1.add_row("10","show results for specific subjects as well as subcribers")

console.print(table1)

console.print("Choose any one option from 1 to 10\t",style=("uu"))

option=int(input("Enter option ---> "))

if option>10 or option<0:
    print("INVALID INPUT PLEASE INPUT NUMBER BETWEEN 1 TO 10")

def again():
    if option==1:
        op1()
        
        ask()
    if option==2:
        op2()
        ask()
    if option==3:
        op3()
        ask()
    if option==4:
        op4()
        ask()
    if option==5:
        op5()
        ask()
    if option==6:
        op6()
        ask()
    if option==7:
        op7()
        ask()
    if option==8:
        op8()
        ask()
    if option==9:
        op9()
        ask()
    if option==10:
        op10()
        ask()

again()