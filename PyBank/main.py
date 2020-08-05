###The total number of months included in the dataset

    #print(f'Total Months : {TotalMonths}')

import os
import csv

budgetDataFilePath = os.path.join("Resources","budget_data.csv")

with open(budgetDataFilePath, newline='') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    csv_header = next(csv_reader)

#print(csv_header)
    TotalMonths = 0
    Total_net = 0
    monthlyChange = []
    previousMonth = []
    Totalchange = 0
    greatestIncrease = 0
    greatestDecrease = 0
    monthDecrease = ""
    monthIncrease = ""

    for i in csv_reader:
        
        # Finding total Months
        TotalMonths = TotalMonths + 1

        # Finding Total Net
        Total_net = Total_net + int(i[1])
        final_profits = int(i[1])
        if TotalMonths ==1:
            monthlyChange = i[1]
            previousMonth.append(i[1])
            index = 0

        else:
            monthlyChange=final_profits - int(previousMonth[index])
            previousMonth.append(i[1])
            index = index +1
            Totalchange = Totalchange + monthlyChange

        if int(monthlyChange) < greatestDecrease:
            greatestDecrease = int(monthlyChange)
            monthDecrease = i[0]

        if int(monthlyChange) > greatestIncrease:
            greatestIncrease = int(monthlyChange)
            monthIncrease = i[0]
 
 

average_changes = round(Totalchange/(TotalMonths-1),2)
print(f'Financial Analysis' + '\n')
print(f'---------------------------' + '\n')
print(f'Total Months: {TotalMonths}')
print(f'Total: {Total_net}')
print(f'Average Change: {average_changes}')
print(f'Greatest Increase in Profits: {monthIncrease} (${greatestDecrease})')
print(f'Greatest Decrease in Profits: {monthDecrease} (${greatestIncrease})')

# Output to a text file

out_path = os.path.join("Financial_Analysis.txt")

with open (out_path, "w", newline = '') as txtfile:
    txtfile.write(f'Financial Analysis' + '\n')
    txtfile.write(f'---------------------------' + '\n')
    txtfile.write(f'Total Months: {TotalMonths}\n')
    txtfile.write(f'Total: {Total_net}\n')
    txtfile.write(f'Average Change: {average_changes}\n')
    txtfile.write(f'Greatest Increase in Profits: {monthIncrease} (${greatestDecrease})\n')
    txtfile.write(f'Greatest Decrease in Profits: {monthDecrease} (${greatestIncrease})\n')


###The net total amount of "Profit/Losses" over the entire period 
    #
    #currentProfit/loss (item[1])
    #total = current profit loss + total
    #print(f'Total: $ {Total}')
###The average of the changes in "Profit/Losses" over the entire period
    #monthlyChange =[]
    #previousMonth = 0.00
    #previousMonth = currentMonth 
    #append currentMonth - previousMonth to monthlyChange ^
    

###The greatest increase in profits (date and amount) over the entire period
    #greatestIncrease ={}
    #print(f'Greatest Increase in Profits: )


###The greatest decrease in losses (date and amount) over the entire period
    #print(f'Greatest Decrease in Profits: )    



