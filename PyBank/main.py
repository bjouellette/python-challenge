#The total number of months included in the dataset

#print(f'Total Months : {TotalMonths}')

#with open (budgetDataPath) as csvFile
#csvReader = csv.reader(csvFile)
import os
import csv
budgetDataFilePath = os.path.join("/Users/brittanyouellette/python-challenge/PyBank/Resources" + "budget_data.csv")
with open("budget_data.csv","r") as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=",")
        csv_header = next(csvFile)
        print(f'Financial Analysis' + '\n')
        print(f'---------------------------' + '\n')
        #for i in csvReader:
            #TotalMonths = i[0]
            #Total = i[1]
            #iTotal = int(Total)
            #previousMonth = 0.00
            #diff = iTotal - previousMonth
            #diffMax = 0
            #diffMin = 0
       
#TotalMonths = TotalMonths + 1
#total += int(Total)



#The net total amount of "Profit/Losses" over the entire period 
    #Total = 0.00
    #currentProfit/loss (item[1])
    #total = current profit loss + total
    #print(f'Total: $ {Total}')
#The average of the changes in "Profit/Losses" over the entire period
    #monthlyChange =[]
    #previousMonth = 0.00
    #previousMonth = currentMonth 
    #append currentMonth - previousMonth to monthlyChange ^
    

#The greatest increase in profits (date and amount) over the entire period
    #greatestIncrease ={}
    #print(f'Greatest Increase in Profits: )


#The greatest decrease in losses (date and amount) over the entire period
    #print(f'Greatest Decrease in Profits: )    

