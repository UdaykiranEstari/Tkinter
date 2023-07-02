
# Importing required Libraries

from datetime import date
from tkinter import *
from turtle import width
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import ImageTk, Image
import plotly.graph_objects as go
import plotly.colors as colors
from tkcalendar import Calendar



# Window Creation

gui_window=Tk()
gui_window.title("Graphical Interface")


# Canvas1

canvas = Canvas(gui_window, width=600, height=300)
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

    fig = go.Figure(data=go.Scatter(x=date_group['date'], y=date_group['Total_cases']))

    fig.update_layout(
        template="plotly_dark",
        title_text='Daily Cases',
        title_font_size=25,
        xaxis_rangeslider_visible=True,
        xaxis_rangeslider_bordercolor='black',  # Set the color of the range slider border
        xaxis_title="Date",
        yaxis_title="No. of Cases",


    )

    fig.show()

def Weekly_cases():
    weekly_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='W')).sum()
    weekly_group = weekly_group.reset_index()
    
    fig = go.Figure(data=go.Scatter(x=weekly_group['date'], y=weekly_group['Total_cases']))

    fig.update_layout(
        
        template="plotly_dark",
        title="weekly Change in Cases",
        title_font_size=25,
        xaxis_rangeslider_visible=True,
        xaxis_rangeslider_bordercolor='black',  # Set the color of the range slider border
        xaxis_title="Date",
        yaxis_title="No. of Cases"

    )

    fig.show()

def Monthly_cases():
    monthly_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    monthly_group = monthly_group.reset_index()
    monthly_group['Month'] = monthly_group['date'].dt.month_name()
    monthly_group = monthly_group[['Month','Total_cases']]
    monthly_group.sort_values(by='Total_cases',ascending=False,inplace=True)
    palette = colors.qualitative.Pastel

    fig = go.Figure(data=go.Bar(y=monthly_group['Month'], x=monthly_group['Total_cases'], orientation='h',marker=dict(color=palette)))

    fig.update_layout(
        template="plotly_dark",
        title="Monthly Cases",
        xaxis_title="No of Cases",
        yaxis_title="Months",
        title_font_size=25,

    )

    fig.show()

def Areas_highest():
    df_place = dataset[['areaName','Total_cases']]
    place_group = df_place.groupby(['areaName']).sum()
    place_group = place_group.reset_index()
    Highest_cases = place_group.sort_values(by='Total_cases').head(10)
    palette = colors.qualitative.Pastel

    fig = go.Figure(data=go.Bar(y=Highest_cases['areaName'], x=Highest_cases['Total_cases'], orientation='h',marker=dict(color=palette)))

    fig.update_layout(
        template="plotly_dark",
        title="Areas with Highest No of Cases",
        xaxis_title="No of Cases",
        yaxis_title="Area Name",
        title_font_size=25,

    )

    fig.show()

def Areas_lowest():
    df_place = dataset[['areaName','Total_cases']]
    place_group = df_place.groupby(['areaName']).sum()
    place_group = place_group.reset_index()
    Least_cases = place_group.sort_values(by='Total_cases',ascending=False).head(10)
    palette = colors.qualitative.Pastel

    fig = go.Figure(data=go.Bar(y=Least_cases['areaName'], x=Least_cases['Total_cases'], orientation='h',marker=dict(color=palette)))

    fig.update_layout(
        template="plotly_dark",
        title="Areas with Least No of Cases",
        xaxis_title="No of Cases",
        yaxis_title="Area Name",
        title_font_size=25,

    )

    fig.show()

def Daily_change():
    date_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='D')).sum()
    date_group = date_group.reset_index()
    date_group['daily_change'] = date_group['Total_cases'].diff()
    fig = go.Figure(data=go.Scatter(x=date_group['date'], y=date_group['daily_change']))

    fig.update_layout(
        title="Daily Change in Cases",
        xaxis_title="Date",
        yaxis_title="No of Cases",
        template="plotly_dark", 
        title_font_size=25,

    )

    fig.show()



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



# Cases for a Particular place

def new_window():
    top = Toplevel()
    top.geometry("320x100")
    l1 = Label(top, text='Enter the name of the Place')
    clicked = StringVar()
    clicked.set("Select the Place ")
    e1 = OptionMenu(top, clicked, *dataset['areaName'].unique())
    l1.grid(column=1,row=2)
    e1.grid(column=2, row=2)


    def required_place():
        required_place = clicked.get()
        DateAndArea_requiredArea = dataset[dataset['areaName'] == required_place]
        DateAndArea_requiredArea.sort_values(by='date',ascending=False,inplace=True)
        fig = go.Figure(data=go.Scatter(x=DateAndArea_requiredArea['date'], y=DateAndArea_requiredArea['Total_cases']))

        fig.update_layout(
            title = 'Cases in the '+ required_place,
            xaxis_title="Date",
            yaxis_title="No of Cases",
            template="plotly_dark", 
            title_font_size=25,

        )

        fig.show()
        top.destroy()
    

    graph_button22 = Button(top,text="Enter",command=required_place,height=2, width=15,font='Raleway')
    graph_button22.grid(column=1,row=3,columnspan=2)

# Comparing Places over time

def open_places_window1():
    top = Toplevel()
    top.title("Number of Places")

    def submit():
        num_places = int(entry.get())  # Get the number of places from the entry widget
        top.destroy()  # Close the input window
        create_places_window1(num_places)  # Call the function to create the places window

    label = Label(top, text="Enter the number of places:")
    label.pack()

    entry = Entry(top)
    entry.pack()

    button = Button(top, text="Submit", command=submit)
    button.pack()

def create_places_window1(num_places):
    top2 = Toplevel()
    top2.title("Compare Places")

    labels = []  # Create an empty list for labels
    clicked_vars = []  # Create an empty list for clicked_var variables

    for _ in range(num_places):
        label = Label(top2, text="areaName:")
        labels.append(label)  # Append the label to the list

        clicked_var = StringVar()
        clicked_var.set("Select the Place ")
        clicked_vars.append(clicked_var)  # Append the StringVar to the list

    option_menus = []  # Create a list to store OptionMenu instances

    for i in range(num_places):
        option_menu = OptionMenu(top2, clicked_vars[i], *dataset['areaName'].unique())
        option_menus.append(option_menu)  # Append the OptionMenu instance to the list
        labels[i].pack()
        option_menu.pack()


    def required_place1():
        places = [var.get() for var in clicked_vars]  # Retrieve selected places from each dropdown
        dataset1 = dataset[dataset['areaName'].isin(places)]
        dataset1.sort_values(by='date', ascending=False, inplace=True)
        
        # Group the data by 'areaName'
        groups = dataset1.groupby('areaName')
        fig = go.Figure()

        # Iterate over the groups and create separate traces for each area
        for name, group in groups:
            fig.add_trace(go.Scatter(
                x=group['date'],
                y=group['Total_cases'],  # Use the appropriate numerical column from your dataset
                mode='lines',
                name=name  # Set the name for the legend
            ))

        fig.update_layout(
            title='Cases in the Selected Areas over Time',
            xaxis_title='Date',
            yaxis_title='No of Cases',
            template='plotly_dark',
            title_font_size=25
        )
        
        fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
            buttons=list([
                dict(count=7, label='1w', step='day', stepmode='backward'),
                dict(count=1, label='1m', step='month', stepmode='backward'),
                dict(count=6, label='6m', step='month', stepmode='backward'),
                dict(count=1, label='YTD', step='year', stepmode='todate'),
                dict(count=1, label='1y', step='year', stepmode='backward'),
                dict(step='all')
            ]),
            font=dict(color='black')  # Set button text color to black
        ))
        
        fig.show()
        top2.destroy()


    button = Button(top2, text="Show", command=required_place1,height=2, width=15,font='Raleway')
    button.pack()


# Cases Between 2 dates



def new_window3():
    top3 = Toplevel()

    l3 = Label(top3, text="Enter the Start date ")
    l4 = Label(top3, text="Enter the End date ")
    e3 = Entry(top3)
    e4 = Entry(top3)

    l3.grid(column=1, row=2)
    l4.grid(column=1, row=3)
    e3.grid(column=2, row=2)
    e4.grid(column=2, row=3)

    def pick_start_date():
        def calendar_date():
            selected_date = cal.selection_get()
            e3.delete(0, END)
            e3.insert(0, selected_date.strftime("%Y-%m-%d"))
            top.destroy()

        top = Toplevel(top3)
        cal = Calendar(top, selectmode="day", year=2023, month=6, 
                       background="darkblue", foreground="black", 
                       selectbackground="steelblue")
        cal.pack(pady=20)
        ok_button = Button(top, text="OK", command=calendar_date)
        ok_button.pack()

    def pick_end_date():
        def calendar_date():
            selected_date = cal.selection_get()
            e4.delete(0, END)
            e4.insert(0, selected_date.strftime("%Y-%m-%d"))
            top.destroy()

        top = Toplevel(top3)
        cal = Calendar(top, selectmode="day", year=2023, month=6, 
                       background="darkblue", foreground="black", 
                       selectbackground="steelblue")
        cal.pack(pady=20)
        ok_button = Button(top, text="OK", command=calendar_date)
        ok_button.pack()

    start_date_button = Button(top3, text="Select Start Date", command=pick_start_date)
    start_date_button.grid(column=3, row=2)

    end_date_button = Button(top3, text="Select End Date", command=pick_end_date)
    end_date_button.grid(column=3, row=3)


    def required_date():
        date_group = df_date.groupby(pd.Grouper(key='date', axis=0, freq='D')).sum()
        date_group = date_group.reset_index()
        start_date = e3.get()
        end_date = e4.get()
        CaseInGiven_DateRange = date_group[(date_group['date'] >= start_date) & (date_group['date'] <= end_date)]
        fig = go.Figure(data=go.Scatter(x=CaseInGiven_DateRange['date'], y=CaseInGiven_DateRange['Total_cases']))

        fig.update_layout(
            title="Cases in a given data range",
            xaxis_title="Date",
            yaxis_title="No of Cases",
            template="plotly_dark", 
            title_font_size=25,

        )

        fig.show()
        top3.destroy()

    graph_button22 = Button(top3, text="Enter", command=required_date, height=2, width=15, font='Raleway')
    graph_button22.grid(column=1, row=4, columnspan=2)


# Comparing Places 

def open_places_window2():
    top = Toplevel()
    top.title("Number of Places")

    def submit():
        num_places = int(entry.get())  # Get the number of places from the entry widget
        top.destroy()  # Close the input window
        create_places_window(num_places)  # Call the function to create the places window

    label = Label(top, text="Enter the number of places:")
    label.pack()

    entry = Entry(top)
    entry.pack()

    button = Button(top, text="Submit", command=submit)
    button.pack()

def create_places_window(num_places):
    top2 = Toplevel()
    top2.title("Compare Places")

    labels = []  # Create an empty list for labels
    clicked_vars = []  # Create an empty list for clicked_var variables

    for _ in range(num_places):
        label = Label(top2, text="areaName:")
        labels.append(label)  # Append the label to the list

        clicked_var = StringVar()
        clicked_var.set("Select the Place ")
        clicked_vars.append(clicked_var)  # Append the StringVar to the list

    option_menus = []  # Create a list to store OptionMenu instances

    for i in range(num_places):
        option_menu = OptionMenu(top2, clicked_vars[i], *dataset['areaName'].unique())
        option_menus.append(option_menu)  # Append the OptionMenu instance to the list
        labels[i].pack()
        option_menu.pack()


    palette = colors.qualitative.Pastel

    def required_place2():
        areas = [var.get() for var in clicked_vars]
        df_place = dataset[['areaName','Total_cases']]
        place_group = df_place.groupby(['areaName']).sum()
        place_group = place_group.reset_index()
        place_group = place_group[place_group['areaName'].isin(areas)]

        fig = go.Figure(data=go.Bar(x=place_group['Total_cases'], y=place_group['areaName'], orientation='h',marker=dict(color=palette)))

        fig.update_layout(
            title = 'Cases in the Selected areas over time',
            xaxis_title="Date",
            yaxis_title="Area Name",
            template="plotly_dark", 
            title_font_size=25,

        )

        fig.show()
        top2.destroy()



    graph_button23 = Button(top2,text="Enter",command=required_place2,height=2, width=15,font='Raleway')
    graph_button23.pack()




# Buttons

graph_button22 = Button(gui_window,text="Cases in Particular place",command=new_window,height=4, width=25,font='Raleway')
graph_button22.grid(column=2,row=5)

graph_button25 = Button(gui_window,text="Comparing Places over time",command=open_places_window1,height=4, width=55,font='Raleway')
graph_button25.grid(column=0,row=6, columnspan=2)

graph_button25 = Button(gui_window,text="Cases in Between dates",command=new_window3,height=4, width=55,font='Raleway')
graph_button25.grid(column=0,row=5,columnspan=2)

graph_button25 = Button(gui_window,text="Comparing Places",command=open_places_window2,height=4, width=25,font='Raleway')
graph_button25.grid(column=2,row=6)


gui_window.mainloop()