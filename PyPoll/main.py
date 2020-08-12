#open file
import os
import csv

electionDataFilePath = os.path.join("Resources","election_data.csv")
with open(electionDataFilePath, newline='') as csvFile:
    csv_reader = csv.reader(csvFile,delimiter=',')
    csv_header = next(csv_reader)

#create variables - totalVotes int, candidateList = {candidate: votes}
    totalVotes=0
    totalCandidates=0
    candidateList=[]
    candidateVotes = []
    percentVotes = []
    Khan_votes =[]
    Correy_votes = []
    Ottoley_votes = []
    Li_votes =[]

#for each row
    for row in csv_reader:
        #Calculating total votes
        totalVotes = totalVotes + 1
        #Count each candidate vote into a list
        if (row[2] == 'Khan'):
            Khan_votes.append(row[2])
        elif (row[2] == 'Correy'):
            Correy_votes.append(row[2])
        elif (row[2] == 'Li'):
            Li_votes.append(row[2])
        elif (row[2] == "O\'Tooley"):
            Ottoley_votes.append(row[2])

    # Counting candidates votes
    Khan_total_votes = len(Khan_votes)
    Correy_total_votes = len(Correy_votes)
    Li_total_votes = len(Li_votes)
    Ottoley_total_votes = len(Ottoley_votes)

    # Calculating percentage 
    percentage_Khan = (Khan_total_votes/totalVotes) * 100
    percentage_Correy = (Correy_total_votes/totalVotes) * 100
    percentage_Li = round((Li_total_votes/totalVotes) * 100, 0)
    percentage_Ottoley = (Ottoley_total_votes/totalVotes) * 100

    winner = [Khan_total_votes, Correy_total_votes, Li_total_votes,Ottoley_total_votes]
    final_winner = max(winner)

    if final_winner == Khan_total_votes:
        winner_name = "Khan"
    elif final_winner == Correy_total_votes:
        winner_name = "Correy"
    elif final_winner == Li_total_votes:
        winner_name = "Li"
    elif final_winner == Ottoley_total_votes:
        winner_name = "O'Tooley"


#print results
print(f'Election Results' + '\n')
print(f'---------------------------' + '\n')
print(f'Total Votes: {totalVotes}\n')
print(f'---------------------------' + '\n')
print(f'Khan: {percentage_Khan:.3f}% ({Khan_total_votes})\n')
print(f'Correy: {percentage_Correy:.3f}% ({Correy_total_votes})\n')
print(f'Li: {percentage_Li:.3f}% ({Li_total_votes})\n')
print(f'O\'Tooley: {percentage_Ottoley:.3f}% ({Ottoley_total_votes})\n')
print(f'---------------------------' + '\n')
print(f'Winner: {winner_name}\n')
print(f'---------------------------' + '\n')

#print outPut
out_path = os.path.join("Analysis","Financial_Analysis.txt")

with open (out_path, "w", newline = '') as txtfile:
    txtfile.write(f'Election Results' + '\n')
    txtfile.write(f'---------------------------' + '\n')
    txtfile.write(f'Total Votes: {totalVotes}\n')
    txtfile.write(f'---------------------------' + '\n')
    txtfile.write(f'Khan: {percentage_Khan:.3f}% ({Khan_total_votes})\n')
    txtfile.write(f'Correy: {percentage_Correy:.3f}% ({Correy_total_votes})\n')
    txtfile.write(f'Li: {percentage_Li:.3f}% ({Li_total_votes})\n')
    txtfile.write(f'O\'Tooley: {percentage_Ottoley:.3f}% ({Ottoley_total_votes})\n')
    txtfile.write(f'---------------------------' + '\n')
    txtfile.write(f'Winner: {winner_name}\n')
    txtfile.write(f'---------------------------' + '\n')