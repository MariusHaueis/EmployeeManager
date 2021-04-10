#This script is a employee manager.
#@author Marius Haueis
#@version 09.04.2021
import pandas as pd
employee_tabel = pd.read_csv("employees.csv")

#returns the total wage per week
total_earned = (lambda row: 
    row["hours_worked"] * row["hourly_wage"] 
    if row["hours_worked"]<= 40 
    else 40 * row["hourly_wage"]+(row["hours_worked"]-40)*row["hourly_wage"] * 1.50)

#Adds to the table a new column with all the wages
def get_wages():
    employee_tabel["total_earned"] = employee_tabel.apply(total_earned, axis =1)
    return employee_tabel

#Returns all top earners per hour
def get_top_earners_per_hour():
    salary = employee_tabel["hourly_wage"]
    top_salary = salary.max()
    top_earners_per_hour = employee_tabel[employee_tabel["hourly_wage"] == top_salary]
    return top_earners_per_hour

#Returns all low earners per hour
def get_low_earners_per_hour():
    salary = employee_tabel["hourly_wage"]
    low_salary = salary.min()
    low_earners_per_hour = employee_tabel[employee_tabel["hourly_wage"] == low_salary]
    return low_earners_per_hour

#Returns all employees who worked overtime
def get_overtime_workers():
    overtime_workers = employee_tabel[employee_tabel["hours_worked"] > 40]
    return overtime_workers

#Cost of each overtime working staff
cost_of_overtime = (lambda rl:
    0
    if rl["hours_worked"]<40
    else (rl["hours_worked"]-40) * rl["hourly_wage"] * 1.50)

#Adds to the table a new column with all the wages paid for overtime
def get_cost_of_overtime():
    employee_tabel["paid_overtime"] = employee_tabel.apply(cost_of_overtime, axis =1)
    return employee_tabel

