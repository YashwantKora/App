import tkinter as tk
from tkinter import ttk
from tkinter import messagebox #<--not in use for now :(
from datetime import date

#Age Calculator

def Age_Calculator():
    age_window = tk.Toplevel()
    age_window.title('Days Since')
    age_window.geometry('1080x720')
    mainframe4 = tk.Frame(age_window, bg='black')
    mainframe4.pack(fill='both', expand=True)

    def Calculate():
        current_date = date.today()
        year = int(year_box.get())
        month = int(month_box.get())
        day = int(day_box.get())
        DOB = date(year, month, day)
        age = current_date - DOB
        yage = round(age.days / 365, 1)
        age_label.config(text=f"You Are {age} Old!" if yage == 1 else f"You Are {age} old!")
        age2_label.config(text=f"OR {yage} Years Old")
        
    label = ttk.Label(mainframe4, text="Enter your DOB")
    label.grid(row=0,column=0)

    year_box = ttk.Entry(mainframe4)
    year_box.grid(row=1, column=0)

    y_l = ttk.Label(mainframe4, text="YYYY")
    y_l.grid(row=2,column=0)

    month_box = ttk.Entry(mainframe4)
    month_box.grid(row=1, column=1)
    
    m_l = ttk.Label(mainframe4, text="MM")
    m_l.grid(row=2,column=1)

    day_box = ttk.Entry(mainframe4)
    day_box.grid(row=1, column=2)

    d_l = ttk.Label(mainframe4, text="DD")
    d_l.grid(row=2,column=2)

    cal_button = ttk.Button(mainframe4, text="Calculate", command=Calculate)
    cal_button.grid(row=3, column=1)

    age_label = ttk.Label(mainframe4, text="...")
    age_label.grid(row=4, column=1)

    age2_label = ttk.Label(mainframe4, text="")
    age2_label.grid(row=5, column=1)

#To Do List

def to_do_list():
    to_do_list = tk.Toplevel()
    to_do_list.title('To Do List')
    to_do_list.geometry('1080x720')

    mainframe4 = tk.Frame(to_do_list, bg = 'black')
    mainframe4.pack(fill='both', expand=True)

    lbl_1 = ttk.Label(mainframe4, text = "To Do List", background='black', foreground='white', font=('New Times Roman', 40, 'bold'))
    lbl_1.grid(row=0, column=0, sticky='W', pady=10)
    lbl_1.place(x = 540, y = 30, anchor = 'center')

#Time Since 

def Time_since_window():
    time_since_window = tk.Toplevel()
    time_since_window.title('Days Since')
    time_since_window.geometry('700x720')

    def Calculate():
        current_year = int(txt_box_3.get())
        current_month = int(txt_box_2.get())
        current_day = int(txt_box_1.get())

        preset_date = date(2025,4,6)
        current_date = date(current_year, current_month, current_day)
        
        difference = abs(current_date - preset_date)
        day = abs(difference)
        lbl_8.config(text=f"{difference.days}") if current_date == current_date or current_date == (2024,9,16) else lbl_8.config(text=f"{day.days}")

        weeks_completed = day.days // 7 

        if weeks_completed >= 1:
            lbl_10.config(text=f"Week {weeks_completed} Completed")
        else:
            lbl_10.config(text="Keep it up!")

        


    mainframe3 = tk.Frame(time_since_window, bg='black')
    mainframe3.pack(fill='both', expand=True)

    lbl_1 = ttk.Label(mainframe3, text="Enter Today's Date: ", background='black', foreground='white', font=('poppins', 20))
    lbl_1.grid(row=0, column=0, sticky='W', pady=10)

    txt_box_1 = ttk.Entry(mainframe3)
    txt_box_1.grid(row=1, column=0, pady=20)

    lbl_2 = ttk.Label(mainframe3, text="DD", background='black', foreground='white', font=('poppins', 20))
    lbl_2.grid(row=2, column=0)

    txt_box_2 = ttk.Entry(mainframe3)
    txt_box_2.grid(row=1, column=1)

    lbl_3 = ttk.Label(mainframe3, text="MM", background='black', foreground='white', font=('poppins', 20))
    lbl_3.grid(row=2, column=1)

    txt_box_3 = ttk.Entry(mainframe3)
    txt_box_3.grid(row=1, column=2, padx=40)

    lbl_4 = ttk.Label(mainframe3, text="YYYY", background='black', foreground='white', font=('poppins', 20))
    lbl_4.grid(row=2, column=2)

    btn_1 = ttk.Button(mainframe3, text="Submit", command=Calculate)
    btn_1.grid(row=5, column=1, pady = 25)

    lbl_5 = ttk.Label(mainframe3, text="Preset Date: ", background='black', foreground='white', font=('poppins', 20))
    lbl_5.grid(row=3, column=0, pady=20,sticky="W")

    lbl_6 = ttk.Label(mainframe3, text="06-04-2025", background='black', foreground='white', font=('poppins', 30))
    lbl_6.grid(row=4, column=1)

    lbl_7 = ttk.Label(mainframe3, text="It's Been: ", background='black', foreground='white', font=('poppins', 20))
    lbl_7.grid(row=6, column=0, sticky='W')

    lbl_8 = ttk.Label(mainframe3, text="...", background='black', foreground='white', font=('poppins', 70))
    lbl_8.grid(row=7, column=1)

    lbl_9 = ttk.Label(mainframe3, text="🔥", background='black', foreground='white', font=('poppins', 70))
    lbl_9.grid(row=8, column=1)

    lbl_10 = ttk.Label(mainframe3, text="...", background='black', foreground='white', font=('poppins', 20))
    lbl_10.grid(row=9, column=1)


#Temperature Converter

def temperature_window():
    temperature_window = tk.Toplevel()
    temperature_window.title('Temperature Converter')
    temperature_window.geometry('310x400')
   
    mainframe2 = tk.Frame(temperature_window, bg='black')
    mainframe2.pack(fill='both', expand=True)

    lbl_1 = ttk.Label(mainframe2, text = "To Do List", background='black', foreground='white', font=('New Times Roman', 40, 'bold'))
    lbl_1.grid(row=0, column=0, sticky='W', pady=10)
    
    def f_to_c():
        fahrenheit = float(text_box1.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{celsius:.2f}°C")

    def c_to_f():
        celsius = float(text_box2.get())
        fahrenheit = celsius * 9/5 + 32
        result_label.config(text=f"{fahrenheit:.2f}°C")
#F to C:
    label1 = ttk.Label(mainframe2, text="Enter a farhenheit value:", background='black', foreground='white', font=('poppins', 20))
    label1.grid(row=1, column=0, sticky='W')

    text_box1 = ttk.Entry(mainframe2)
    text_box1.grid(row=3, column=0, pady = 10)

    button3 = ttk.Button(mainframe2, text="Convert To Celsius", command= f_to_c)
    button3.grid(row=4, column=0, pady = 10)
# C to F:                                           nice hack lol v
    label2 = ttk.Label(mainframe2, text="Enter a celsius value:      " ,background='black', foreground='white', font=('poppins', 20))
    label2.grid(row=5, column=0)

    text_box2 = ttk.Entry(mainframe2)
    text_box2.grid(row=6,column=0, pady=10)

    button4 = ttk.Button(mainframe2, text="Convert To Farhenheit", command=c_to_f)
    button4.grid(row=7, column=0, pady=10) 

    result_label = ttk.Label(mainframe2, text="...", background='black', foreground='white', font=('poppins', 25) )
    result_label.grid(row=8, column=0, pady= 20, padx= 20) 

#Main Menu

window = tk.Tk()
window.geometry('800x400')
window.title("I have no idea what i am doing")

mainframe = tk.Frame(window, bg='black',)
mainframe.pack(fill='both', expand=True)


label = tk.Label(mainframe, text="Main Menu", foreground='white', background='black', font=('New Times Roman', 30, 'bold'))
label.grid(row=0, column=1)

button1 = ttk.Button(mainframe, text="Temperature Converter", command=temperature_window)
button1.grid(row=1, column=0, pady=20, padx=40)

bt1_label = ttk.Label(mainframe, text="- Converts Fahrenheit to Celsius and vice versa!", background='black', foreground='white', font=('poppins', 15))
bt1_label.grid(row=1, column=1)
#                                       lol v
button2 = ttk.Button(mainframe, text="           To Do List           ", command=to_do_list)
button2.grid(row=2, column=0, pady = 20)
#                                                           bruh!! v 
bt2_label = ttk.Label(mainframe, text="- Create and organize your tasks", background='black', foreground='white', font=('poppins', 15))
bt2_label.grid(row=2, column=1)

button3 = ttk.Button(mainframe, text="         Time Since           ", command=Time_since_window)
button3.grid(row=3, column=0, pady=20)

bt3_label = ttk.Label(mainframe, text="- How many Days have passed!", background='black', foreground='white', font=('poppins', 15))
bt3_label.grid(row=3, column=1)

button4 = ttk.Button(mainframe, text="       Age Calculator       ", command=Age_Calculator)
button4.grid(row=4, column=0, pady=20)

bt4_label = ttk.Label(mainframe, text="- Calculates your age!", background='black', foreground='white', font=('poppins', 15))
bt4_label.grid(row=4, column=1)

window.mainloop()
