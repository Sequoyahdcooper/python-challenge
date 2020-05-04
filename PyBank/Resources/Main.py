#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv

#Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Path For File
csvpath = os.path.join('budget_data.csv')


# In[4]:


#Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
    #CSV Reader 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read The Header Row First 
    csv_header = next(csvreader)
    row = next(csvreader)
    
    #Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    #Read Each Row Of Data After The Header
    for row in csvreader:
        
        #Calculate Total Number Of Months Included In Dataset
        total_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        net_amount += int(row[1])

        #Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]


# In[6]:


#Calculate The Average & The Date
average_change = sum(monthly_change)/ len(monthly_change)
    
highest = max(monthly_change)
lowest = min(monthly_change)


# In[7]:


#Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

#Specify File To Write To
output_file = os.path.join('budget_data.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")


# In[ ]:




