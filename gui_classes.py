from cgitb import text
from tkinter import filedialog
from turtle import width
import tkinter
import customtkinter
import ot_new_df
import pandas as pd
from datetime import datetime
import re



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("750x300")
        self.title("Overtime Calculator")
        self.minsize(500, 250)

        # create 2x2 grid system
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure((0, 5), weight=1)

        self.label = customtkinter.CTkLabel(master=self, text='Overtime Calculator',font=('times',24),width=150, height=30 )
        self.label.grid(row=0, column=2,padx=0, pady=0, columnspan=2)

        self.buttongo = customtkinter.CTkButton(master=self, command=self.button_callback, text="Go")
        self.buttongo.grid(row=5, column=5, padx=20, pady=20)
        
        self.buttonbrowse = customtkinter.CTkButton(master=self, command=self.button_browse, text="Open File")
        self.buttonbrowse.grid(row=5, column=0, padx=20, pady=20)
        
        self.segmented_button = customtkinter.CTkSegmentedButton(master=self,values=["Monthly", "Weekly"],
                                                                 command=self.segmented_button_callback)
        self.segmented_button.grid(
            row=1, column=2 ,padx=20,pady=20, sticky='ew')
        self.segmented_button.set("Monthly")  # set initial values
        
        
        
        """Employee dropdown"""


        self.optionmenu_employee_var = customtkinter.StringVar(value="Employee")  # set initial value
        self.employee_combobox = customtkinter.CTkOptionMenu(master=self,
                                                        values=["Employee"],
                                                        command=self.optionmenu_employee_callback,
                                                        variable=self.optionmenu_employee_var
                                                        )
        self.employee_combobox.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky='ew')

    def optionmenu_employee_callback(self,choice):
        print("optionmenu_employee dropdown clicked:", choice)
        
        
    def month_in_dataframe(self, df):
                
        df['Date'] = pd.to_datetime(df['Date']) #Convert to date and time
        df = df.groupby(df['Date'].dt.strftime('%B')) # Group by month and rename month to string name
        # df = dataframe.groupby(pd.Grouper(freq='M')) 
        df_groups = df.groups
        list_of_months = list(df_groups.keys())
        list_of_months.sort(key=lambda m: datetime.strptime(m, "%B")) # function that uses datetime to sort the months in ascending order
                    
        return list_of_months

    def button_callback(self):
        chosen_employee = self.employee_combobox.get()
        chosen_emp_df = self.employee_dataframe[chosen_employee]
        active_employee = ot_new_df.Employee(chosen_employee, chosen_emp_df)
                  
        overtime_selection = self.segmented_button.get()
        
        if overtime_selection=="Monthly":            
            ot_new_df.Employee.plot(active_employee)
        elif overtime_selection=="Weekly":
            selected_month = month_combobox.get()
            active_employee.month_plotter(selected_month)
                
        
    def button_browse(self):
        """Open file for main app"""
        """ progress bar"""


        progressbar = customtkinter.CTkProgressBar(master=app, orientation='horizontal', mode='determinate')
        progressbar.grid(row=3, column=2)
        progressbar.start()
        self.employee_list, self.employee_dataframe = ot_new_df.process_employees()
        
        
        employee_list = sorted(self.employee_list, key=lambda i: int(
            re.match(r'\((\d+)\)', i).group(1))) # orders the list by employee number, remove if wanted
        
        self.employee_combobox.set(employee_list[0])
        self.employee_combobox.configure(values=employee_list)
        progressbar.set(1)
        progressbar.stop()
            
                     
    def segmented_button_callback(self,value):
        print("segmented button clicked:", value)
        if value == "Monthly":
            month_combobox.configure(state="disabled")
        else:
            month_combobox.configure(state="normal")
        if value == "Weekly":
            employee = self.employee_combobox.get()
            df = self.employee_dataframe[employee]
            months_in_df = self.month_in_dataframe(df)
            month_combobox.set(months_in_df[0])
            month_combobox.configure(values=months_in_df)
            
            



        
        
        
        
        

        
if __name__ == "__main__":
    app = App()
    
    






"""Month dropdown"""

optionmenu_month_var = customtkinter.StringVar(value="First Month")  # set initial value


def optionmenu_month_callback(choice):
    print("optionmenu_month dropdown clicked:", choice)
    



month_combobox = customtkinter.CTkOptionMenu(master=app,
                                    values=["First Month"],
                                    command=optionmenu_month_callback,
                                    variable=optionmenu_month_var,
                                    state="disabled")
month_combobox.grid(row=2, column=4, columnspan=2,
                    padx=20, pady=20, sticky='ew')

   

app.mainloop()
