from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import ImageTk, Image


gui_window=Tk()

# Canvas

canvas = Canvas(gui_window, width=600, height=300)
canvas.grid(columnspan=3,rowspan=4)

gui_window.title("Graph Interface")


# Logo Command

logo = Image.open('Heading2.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=0,columnspan=3)

# def Codes

def Daily_cases():
    df = pd.read_csv('date_group.csv')
    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(12,5),dpi=100)
    sns.lineplot(x='date', y= 'Total_cases',data= df
           ).set(title='Areas with Highest No of Cases')
    plt.show()

def Weekly_cases():
    df2 = pd.read_csv('weekly_group.csv')
    plt.figure(figsize=(12,8),dpi=100)
    sns.barplot(x='Total_cases', y= 'date',data= df2, orient = 'h',palette='flare'
           ).set(title='Areas with Highest No of Cases')
    plt.show()

def Monthly_cases():
    monthly_group = pd.read_csv('month_group.csv')
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'Month',data= monthly_group, orient = 'h',palette='Set3' 
           ).set(title='Areas with Highest No of Cases')
    plt.show()

def Areas_highest():
    Highest_cases = pd.read_csv('AreasWith_HighestCases.csv')
    sns.set_style("whitegrid", {'axes.grid' : False})
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'areaName',data= Highest_cases, orient = 'h',palette='autumn' 
           ).set(title='Areas with Highest No of Cases')
    plt.show()

def Areas_lowest():
    Lowest_cases = pd.read_csv('AreasWith_LowestCases.csv')
    sns.set_style("whitegrid", {'axes.grid' : False})
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'areaName',data= Lowest_cases, orient = 'h',palette='viridis_r' 
           ).set(title='Areas with Highest No of Cases')
    plt.show()
       



graph_button = Button(gui_window,text="Daily_cases",command=Daily_cases,height=4, width=25,font='Raleway')
graph_button.grid(column=0,row=1)

graph_button2 = Button(gui_window,text="Weekly_cases",command=Weekly_cases,height=4, width=25)
graph_button2.grid(column=1,row=1)

graph_button3 = Button(gui_window,text="Montly_cases",command=Monthly_cases,height=4, width=25)
graph_button3.grid(column=2,row=1)

graph_button4 = Button(gui_window,text="Cities with Highest number of cases ",command=Areas_highest,height=4, width=55)
graph_button4.grid(column=0,row=2,columnspan=2)

graph_button5 = Button(gui_window,text="Cities with Least number of cases ",command=Areas_lowest,height=4, width=55)
graph_button5.grid(column=0,row=3,columnspan=2)


Button_quit = Button(gui_window, text="Exit Programm", command=gui_window.quit,height=6, width=25)
Button_quit.grid(column=2,row=2,rowspan=2)




gui_window.mainloop()