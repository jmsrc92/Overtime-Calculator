from datetime import datetime
from sqlite3 import Date
import pandas as pd
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog




  

class Employee():
  
  month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
  


  def __init__(self, name, dataframe=None ,overtime=None) -> None:
    self.name = name
    self.hrs_jan = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_feb = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_mar = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_apr = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_may = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_jun = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_jul = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_aug = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_sep = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_oct = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_nov = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.hrs_dec = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_jan = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_feb = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_mar = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_apr = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_may = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_jun = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_jul = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_aug = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_sep = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_oct = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_nov = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.weeks_dec = pd.DataFrame(columns=['Name', 'Date', 'Overtime'])
    self.dataframe = dataframe
    self.overtime = overtime
    self.months_in_df = []
    
  def month_totals(self):  
    month_totals = [self.hrs_jan['Overtime'].sum(),
                    self.hrs_feb['Overtime'].sum(),
                    self.hrs_mar['Overtime'].sum(),
                    self.hrs_apr['Overtime'].sum(),
                    self.hrs_may['Overtime'].sum(),
                    self.hrs_jun['Overtime'].sum(),
                    self.hrs_jul['Overtime'].sum(),
                    self.hrs_aug['Overtime'].sum(),
                    self.hrs_sep['Overtime'].sum(),
                    self.hrs_oct['Overtime'].sum(),
                    self.hrs_nov['Overtime'].sum(),
                    self.hrs_dec['Overtime'].sum(), ]
    return month_totals
  
  def addlabels(x, y):
      for i in range(len(x)):
          plt.text(i, y[i]//2, y[i], ha='center')
          
       
  def plot(self):
    if sum(self.month_totals()) < 1: # Checks list of month totals to see if overtime has been calculated
      Employee.calculate_weeks(self)
        
    """  Takes x axis vales and y parameter vales then displays plot  """
    # creating data on which bar chart will be plot
    x = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
    y = self.month_totals()
    # setting figure size by using figure() function
    plt.figure(figsize=(15, 5))
    # making the bar chart on the data
    plt.bar(x, y)
    # calling the function to add value labels
    Employee.addlabels(x, y)
    # giving title to the plot
    plt.title("Overtime Totals Per Month")
    # giving X and Y labels
    plt.xlabel("Month")
    plt.ylabel("Hours")
    # visualizing the plot
    plt.show()
    
  def month_in_dataframe(self, month):
    month = str(month)
    dict_months = {
                    '1':'January',
                    '2': 'February',
                    '3':'March',
                    '4':'April',
                    '5':'May',
                    '6':'June',
                    '7':'July',
                    '8':'August',
                    '9':'September',
                    '10':'October',
                    '11':'November',
                    '12': 'December',
    }
    month_name = dict_months[month]
    if month_name in self.months_in_df:
      pass
    else:
      self.months_in_df.append(month_name)
    
      
    

    
  def sort_dataframes(old_df, old_df_weeks,current_week):    
 
    new_df = pd.DataFrame(
        {'Name': current_week['Employee'], 'Date': current_week['Date'], 'Overtime': current_week['Overtime']})
    old_df = pd.concat([old_df, new_df])
    new_df_weeks = pd.DataFrame({'Name': current_week['Employee'].iloc[0], 'Date': [current_week['Date'].iloc[0]], 'Overtime': current_week['Overtime'].sum()})
    old_df_weeks = pd.concat([old_df_weeks, new_df_weeks])    

    return old_df, old_df_weeks

  def calculate_weeks(self):

    all_hours_df = pd.DataFrame(self.dataframe)


    all_hours_df.reset_index()
    range_start = self.dataframe.Date.iloc[0]
    end_of_range = self.dataframe.Date.iloc[-1]
    # sample data
    df = pd.DataFrame(pd.date_range(range_start, end_of_range), columns=['Date'])
    # groupby your key and freq
    g = all_hours_df.groupby(pd.Grouper(key='Date', freq='W'))
    # groups to a list of dataframes with list comprehension
    df_grouped_by_week = [group for x, group in g]

    # create a dateframe with all wednesday in the daterange for min and max of df.Date
    wednesday = pd.DataFrame({'datetime': pd.date_range(
        df.Date.min(), df.Date.max(), freq='W-WED')})

    # use groubpy and last, to get the last Friday of each month into a list
    last_wednesday_in_daterange = wednesday.groupby(
        [wednesday.datetime.dt.year, wednesday.datetime.dt.month]).last()['datetime'].tolist()
      # Create months list with no overtime in
    month_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      # Creat empty list of week totals
    list_dataframe_weeks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # month = df_grouped_by_week[0]['Date'].array[0].month
  
    for week in df_grouped_by_week:
      if week.empty:
        pass
      else:
        try:
          month = week['Date'].iloc[2].month
        except:
          month = week['Date'].iloc[0].month

        if month == 1:
          self.hrs_jan, self.weeks_jan = Employee.sort_dataframes(self.hrs_jan, self.weeks_jan, week)
          self.month_in_dataframe(month)
        elif month == 2:
          self.hrs_feb, self.weeks_feb = Employee.sort_dataframes(self.hrs_feb, self.weeks_feb, week)
          self.month_in_dataframe(month)
        elif month == 3:
          self.hrs_mar, self.weeks_mar = Employee.sort_dataframes(self.hrs_mar, self.weeks_mar, week)
          self.month_in_dataframe(month)
        elif month == 4:
          self.hrs_apr, self.weeks_apr = Employee.sort_dataframes(self.hrs_apr, self.weeks_apr, week)
          self.month_in_dataframe(month)
        elif month == 5:
          self.hrs_may, self.weeks_may = Employee.sort_dataframes(self.hrs_may, self.weeks_may, week)
          self.month_in_dataframe(month)
        elif month == 6:
            self.hrs_jun, self.weeks_jun = Employee.sort_dataframes(self.hrs_jun, self.weeks_jun, week)
            self.month_in_dataframe(month)
        elif month == 7:
            self.hrs_jul, self.weeks_jul = Employee.sort_dataframes(self.hrs_jul, self.weeks_jul, week)
            self.month_in_dataframe(month)
        elif month == 8:
            self.hrs_aug, self.weeks_aug = Employee.sort_dataframes(self.hrs_aug, self.weeks_aug, week)
            self.month_in_dataframe(month)
        elif month == 9:
            self.hrs_sep, self.weeks_sep = Employee.sort_dataframes(self.hrs_sep, self.weeks_sep, week)
            self.month_in_dataframe(month)
        elif month == 10:
            self.hrs_oct, self.weeks_oct = Employee.sort_dataframes(self.hrs_oct, self.weeks_oct, week)
            self.month_in_dataframe(month)
        elif month == 11:
            self.hrs_nov, self.weeks_nov = Employee.sort_dataframes(self.hrs_nov, self.weeks_nov, week)
            self.month_in_dataframe(month)
        elif month == 12:
            self.hrs_dec, self.weeks_dec = Employee.sort_dataframes(self.hrs_dec, self.weeks_dec, week)
            self.month_in_dataframe(month)
        else:
          print("error")
        
      # handle bug if wednseday not in first week
      # if wednesday is in the list
      while True:
        try:
          if week['Date'].array[2] in last_wednesday_in_daterange:
              month += 1
              break
          else:
            break  
        except IndexError:
          break   
        
  
  def month_plotter(self, selected_month):
    if sum(self.month_totals()) < 1:  # Checks list of month totals to see if overtime has been calculated
      Employee.calculate_weeks(self)
    if self.dataframe.empty == True:
      return print("Month not available in file, choose a different month.\n")
    else:
      
      months = {'January': [self.weeks_jan, 'January'],
                'February': [self.weeks_feb, 'February'],
                'March': [self.weeks_mar, 'March'],
                'April': [self.weeks_apr, 'April'],
                'May': [self.weeks_may, 'May'],
                'June': [self.weeks_jun, 'June'],
                'July': [self.weeks_jul, 'July'],
                'August': [self.weeks_aug, 'August'],
                'September': [self.weeks_sep, 'September'],
                'October': [self.weeks_oct, 'October'],
                'November': [self.weeks_nov, 'November'],
                'December': [self.weeks_dec, 'December'], }
      
      df = months[selected_month][0]
      # Change time format
      while True:
        try:
          df['Date'] = df.Date.dt.strftime('%d-%m')
          break
        except:
          pass
          break
        
      new_title = f"{df['Name'].iloc[0]} {selected_month} Overtime"
      #create bar plot to visualize sales by product
      ax = df.plot.bar(x='Date', y='Overtime', legend=False, figsize=(15, 8), title=new_title)
      #annotate bars
      ax.bar_label(ax.containers[0])
      plt.show() 
        
def open_file():
  file_path = tkinter.filedialog.askopenfilename(
      title="Open Target File", initialdir=r"T:\Quality\Reports", filetypes=[('Excel Files', '*.xls')])
  return file_path


""" START OUT OF CLASS"""

def calculate_ot(worked_hours=float, day=int):
  if day < 4:
    daily_hrs = 8.5
  elif day == 4:
    daily_hrs = 5
  else:
    daily_hrs = 0
  
  if worked_hours == 0:
    if day == 6 or day == 5:
      worked_hours= 0
    else:
      worked_hours = daily_hrs
      
  overtime = worked_hours - daily_hrs

  if overtime < 0:
    return 0
  else:
    return overtime
  
def process_employees():  
  
  ot_sheet = pd.read_excel(open_file(),
                          sheet_name=0, header=4, usecols=("A,B,D,F"), skiprows=0, skipfooter=3)         
  #Empty overtime list
  overtime = []
  employees_list = []
  employee_months = {}
  final_db = pd.DataFrame(columns=['Employee','Date', 'Hrs Attended', 'Hrs Wkd', 'Day', 'Overtime'])

  # PLace overtime value in column + add emloyee name to list
  for index, row in ot_sheet.iterrows():
    if type(row[1]) == datetime:
      new_df = pd.DataFrame({'Employee': [row['Employee']],
                            'Date': [row['Date']],
                            'Hrs Attended': [row['Hrs Attended']],
                            'Hrs Wkd': [row['Hrs Wkd']],
                            'Day': [row['Date'].weekday()],
                            'Overtime': [calculate_ot(row[3], row['Date'].weekday())]})
      final_db = pd.concat([final_db, new_df], ignore_index=True)
      overtime.append(calculate_ot(row[3], row['Date'].weekday()))
      current_month = row['Date'].month
      employee_name = row[0]
      if employee_name not in employees_list:
        employees_list.append(employee_name)
      else:
        pass
    else:
      pass


  # Seperate dataframes y employee name
  employee_grp = final_db.groupby('Employee')

  #employee objects list  
  employee_objects = []
  #Create all employees from Employee names list  and store them to employee objcts list
  employee_num = 0
  # for employee in employees_list:
  #   employee_objects.append(Employee(employee, employee_grp.get_group(employees_list[employee_num])))
  #   employee_num += 1
  employee_dict = {}
  employee_months_in_df = {}
  
  for employee in employees_list:
    employee_dataframe = employee_grp.get_group(employees_list[employee_num])
    employee_dict.update({employee : employee_dataframe})
    employee_num += 1
    
    
  
  # for index, employee in enumerate(employees_list):
  #   print(index, employee)
  
  return employees_list, employee_dict
  
# while True:
  
#   employee_choice = input("Press Number to select Employee, type 'exit' to leave\n ") 
  
#   if employee_choice.lower() == 'exit': break
  
#   chosen_employee = employee_objects[int(employee_choice)]
  
#   ot_choice = input("Press '1' to see your monthly overtime \nPress '2' to see your weekly overtime\n ")
  
#   if ot_choice == '1':
#     """ Shows yearly overtime"""
#     Employee.plot(chosen_employee)
#   elif ot_choice == '2':  
#     """Shows month overtime"""
#     while True:
#       chosen_month = input("Enter number between '1-12' to see overtime in that month\n ")
#       try:
#         if int(chosen_month) in range(1,13):
#           Employee.month_plotter(chosen_employee, str(chosen_month))
#           break
#         elif chosen_month.lower() == "exit": break
#         else:
#           print("Choose a number between '1 - 12' \nType exit to leave\n")
#       except:
#         print("Month not in file, try again. \nType exit to leave\n")
#   else:
#     print("Press '1' or '2'")

 
        

 


