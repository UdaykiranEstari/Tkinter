from datetime import date
from tkinter import *
from turtle import width
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import ImageTk, Image

# Window Creation

gui_window=Tk()
gui_window.title("Graphical Interface")


# Canvas1

canvas = Canvas(gui_window, width=600, height=300,)
canvas.grid(columnspan=3,rowspan=4)


# Logo Command

logo = Image.open('reports/figures/Heading2.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=0,columnspan=3)

# def Codes1

dataset = pd.read_csv('data/processed/fulldataset.csv')
dataset['date'] = pd.to_datetime(dataset['date'])
df_date = dataset[['date','Total_cases']]

def Daily_cases(): 
    date_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='D')).sum()
    date_group = date_group.reset_index()
    plt.figure(figsize=(12,5),dpi=100)
    sns.lineplot(y='Total_cases', x= 'date',data= date_group
           ).set(title='Daily Cases')
    plt.show()



def Weekly_cases():
    weekly_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='W')).sum()
    weekly_group = weekly_group.reset_index()
    plt.figure(figsize=(12,5),dpi=100)
    sns.lineplot(y='Total_cases', x= 'date',data= weekly_group
           ).set(title='Weekly Cases')
    plt.show()

def Monthly_cases():
    monthly_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    monthly_group = monthly_group.reset_index()
    monthly_group['Month'] = monthly_group['date'].dt.month_name()
    monthly_group = monthly_group[['Month','Total_cases']]
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'Month',data= monthly_group, orient = 'h',palette='Set3' 
           ).set(title='Monthly Cases')
    plt.show()

def Areas_highest():
    df_place = dataset[['areaName','Total_cases']]
    place_group = df_place.groupby(['areaName']).sum()
    place_group = place_group.reset_index()
    Highest_cases = place_group.sort_values(by='Total_cases',ascending=False).head(10)
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'areaName',data= Highest_cases, orient = 'h',palette='autumn' 
           ).set(title='Areas with Highest No of Cases')
    plt.show()

def Areas_lowest():
    df_place = dataset[['areaName','Total_cases']]
    place_group = df_place.groupby(['areaName']).sum()
    place_group = place_group.reset_index()
    Least_cases = place_group.sort_values(by='Total_cases',ascending=True).head(10)
    plt.figure(figsize=(12,5),dpi=100)
    sns.barplot(x='Total_cases', y= 'areaName',data= Least_cases, orient = 'h',palette='viridis_r' 
           ).set(title='Areas with Lowest No of Cases')
    plt.show()

def Daily_change():
    date_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='D')).sum()
    date_group = date_group.reset_index()
    date_group['daily_change'] = date_group['Total_cases'].diff()
    plt.figure(figsize=(10,7),dpi=80)
    graph = sns.lineplot(x='date', y ='daily_change' ,data=date_group, color = 'skyblue', linewidth = 2)
    graph.axhline(0, linestyle = '--', color = 'black', linewidth = 1 )
    graph.set(title='Daily Change of Cases')
    plt.show()



# Buttons


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

graph_button6 = Button(gui_window,text="Daily Change",command=Daily_change,height=4, width=25)
graph_button6.grid(column=2,row=2)

Button_quit = Button(gui_window, text="Exit Programm", command=gui_window.quit,height=4, width=25)
Button_quit.grid(column=2,row=3)



# ======================================================================================================================

# Canvas2

canvas = Canvas(gui_window, width=600, height=300)
canvas.grid(columnspan=3,rowspan=4)

# Logo Command

logo = Image.open('reports/figures/Heading3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0,row=4,columnspan=3)

# def Codes1

# Cases for a Particular place

def new_window():
    top = Toplevel()
    l1 = Label(top, text='Enter the name of the Place')
    e1 = Entry(top)
    l1.grid(column=1,row=2)
    e1.grid(column=2, row=2)

    def required_place():
        required_place = e1.get()
        DateAndArea_requiredArea = dataset[dataset['areaName'] == required_place]
        plt.figure(figsize=(9,5),dpi=100)
        sns.lineplot(x='date', y = 'Total_cases' ,data= DateAndArea_requiredArea 
                ).set(title = 'Cases in the '+ required_place)
        plt.show()

    graph_button22 = Button(top,text="Enter",command=required_place,height=2, width=15,font='Raleway')
    graph_button22.grid(column=1,row=3,columnspan=2)

# Comparing Places over time

def new_window2():
    top2 = Toplevel()
    labels = [Label(top2, text="areaName1:"), Label(top2, text="areaName2:"), Label(top2, text="areaName3:"), 
            Label(top2, text="areaName4:"), Label(top2, text="areaName5:")]
    entries = [Entry(top2), Entry(top2), Entry(top2), Entry(top2), Entry(top2)]

    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    def required_place():
        places = [entry.get() for entry in entries]
        dataset1 = dataset[dataset['areaName'].isin(places)]
        plt.figure(figsize=(12,5),dpi=100)
        sns.lineplot(x="date", y="Total_cases", hue="areaName", data=dataset1)
        plt.show()

    graph_button23 = Button(top2,text="Enter",command=required_place,height=2, width=15,font='Raleway')
    graph_button23.pack()

# Cases Between 2 dates

def new_window3():
    top3 = Toplevel()
    l3 = Label(top3, text="Enter the Start date Format:'YYYY-MM-DD' ")
    l4 = Label(top3, text="Enter the Start date Format:'YYYY-MM-DD' ")
    e3 = Entry(top3)
    e4 = Entry(top3)
    l3.grid(column=1,row=2)
    l4.grid(column=1,row=3)
    e3.grid(column=2, row=2)
    e4.grid(column=2,row=3)

    def required_date():
        date_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='D')).sum()
        date_group = date_group.reset_index()
        start_date = e3.get()
        End_date = e4.get()
        CaseInGiven_DateRange = date_group[(date_group['date']>= start_date) & (date_group['date']<= End_date)]
        plt.figure(figsize=(10,7),dpi=80)
        sns.lineplot(y="Total_cases", x="date",data=CaseInGiven_DateRange )
        plt.show()

    graph_button22 = Button(top3,text="Enter",command=required_date,
                            height=2, width=15,font='Raleway')
    graph_button22.grid(column=1,row=4,columnspan=2)

# Comparing Places 

def new_window4():
    top2 = Toplevel()
    labels = [Label(top2, text="areaName1:"), Label(top2, text="areaName2:"), Label(top2, text="areaName3:"), 
            Label(top2, text="areaName4:"), Label(top2, text="areaName5:")]
    entries = [Entry(top2), Entry(top2), Entry(top2), Entry(top2), Entry(top2)]

    for label, entry in zip(labels, entries):
        label.pack()
        entry.pack()

    def required_place():
        areas = [entry.get() for entry in entries]
        df_place = dataset[['areaName','Total_cases']]
        place_group = df_place.groupby(['areaName']).sum()
        place_group = place_group.reset_index()
        place_group = place_group[place_group['areaName'].isin(areas)]
        plt.figure(figsize=(12,5),dpi=100)
        sns.barplot(x='Total_cases', y= 'areaName',data= place_group, orient = 'h',palette='autumn' 
                ).set(title='Areas Vs Numbers of Cases')
        plt.show()


    graph_button23 = Button(top2,text="Enter",command=required_place,height=2, width=15,font='Raleway')
    graph_button23.pack()




# Buttons

graph_button22 = Button(gui_window,text="Cases in Particular place",command=new_window,height=4, width=25,font='Raleway')
graph_button22.grid(column=2,row=5)

graph_button25 = Button(gui_window,text="Comparing Places over time",command=new_window2,height=4, width=55,font='Raleway')
graph_button25.grid(column=0,row=6, columnspan=2)

graph_button25 = Button(gui_window,text="Cases in Between dates",command=new_window3,height=4, width=55,font='Raleway')
graph_button25.grid(column=0,row=5,columnspan=2)

graph_button25 = Button(gui_window,text="Comparing Places",command=new_window4,height=4, width=25,font='Raleway')
graph_button25.grid(column=2,row=6)


gui_window.mainloop()