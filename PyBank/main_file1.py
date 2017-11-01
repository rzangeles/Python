#PyBank Rev1

#calculate the total number of months in the data set
#calculate the total number of revenue in the data set
#average change of revenue between months
#max increase in revenue month over month
#least increase in revenue month over month
#data is in sequential order so approach code accordingly

#import the csv file
#as you read the file do the following
#store data (month and revenue) on 2 separate lists with the same index
#store average revenue on a seaparate list with same index as well

#variables
#months = list for months
#revenue = list for revenue
#rev_change = list for revenue changes
#total_months = total number of months
#total_revenue = total revenue
#average_change_rev = average change of revenues
#max_change = greatest change on revenue
#max_change_month = greatest change revenue month
#min_change = least change in revenue
#min_change_month = least change in revenue month

#remaining item - convert numbers to long instead of float

import csv

i = 0
months = []
revenue = []
rev_change_list = []
total_months = 0
total_revenue = 0.00

#obtain data from the csv file
with open('budget_data_1.csv', newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for row in csvreader:

          months.append(row[0])
          revenue.append(row[1])

     # remove the headers
     del months[0]
     del revenue[0]
     
     #calculate and store values
     #calculate total months and total revenue

     index = 0
     rev_change = 0.00
     for i in months:
          total_months = total_months + 1
          total_revenue = total_revenue + float(revenue[index])

          if (index > 0):
               rev_change = float(revenue[index]) - float(revenue[index-1])
     
          rev_change_list.append(rev_change)
          index=index+1

     #calculate average revenue change
     total_rev_change = 0.00

     max_change = 0.00
     max_index = 0
     min_change = 0.00
     min_index = 0

     index = 0
     for i in rev_change_list:
          total_rev_change = total_rev_change + float(rev_change_list[index])
     
          if(float(rev_change_list[index]) >= max_change):
              max_change = float(rev_change_list[index])
              max_index = index

          elif(float(rev_change_list[index]) <= min_change):
               min_change = float(rev_change_list[index])
               min_index = index

          index = index + 1

     average_change_rev = total_rev_change/index


     print("Total Months: " + str(total_months))
     print("Total Revenue: $" + str(total_revenue))
     print("Average Revenue Change: $" + str(average_change_rev))
     print("Greatest Increase in Revenue: " + months[max_index] + " $" + str(max_change))
     print("Greatest Derease in Revenue: " + months[min_index] + " $" + str(min_change))

#     print(rev_change_list)
#     print(str(rev_change_list[0]))
#     print(str(rev_change_list[1]))
#     print(str(rev_change_list[2]))
#     print(str(rev_change_list[3]))

     
# check if data is collected
#     print(months)
#     print()

#     print(revenue)
#     print()


          
