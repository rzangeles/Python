#PyPoll Rev 1

#Below are the tasks to complete
#Calculate total number of votes cast
#Complete list of candidates that received votes
#Total number of votes for each candidate
#The winner of the election based on the popular vote
#print data on the screen
#print data to a new file "results.csv"

#import the csv file
#create two lists:  1 for the candidate list and 2 for the qty of votes
#as your read the file, do the following
#check if the candidate exist in the candidate list
#if yes, add the vote to the count.  if no, append the new candidate and append a new vote count and start with 1
#print the list of candidates and their total votes and perentage of votes
#print the winner with the highest votes

#variables
#candidate_list = list of candidates
#votes_list = list of total votes
#total_votes - total count of votes
#max_candidate - winner candidate

import csv

candidate_list = []
votes_list = []
total_votes = 0
found = False

print("Welcome to the Election Polling Counter Software")
print()
file_name = input("What is the name of the file? ")

#obtain data from the csv file
with open(file_name, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')


     
     for row in csvreader:

          index = 0
#         temp_counter = 0
          found = False
          
          for i in candidate_list:
               #if candidate matches the item on the list
               if (row[2] == candidate_list[index]):
     
                    #extract the value on the respective index
                    #add 1 vote to the count and store back to the same index
                    count = int(votes_list[index])

                    count = count + 1
                    votes_list[index] = str(count)

                    index = 0
                    found = True
                    
                    break
                    
               #if candidate does not match the item the list
               elif (row[2] != candidate_list[index]):

                    index = index + 1
                    
          if (found == False):
               
          #if candidate does not exist even at the end of the list                    
          #add new candidate to the list
               candidate_list.append(row[2])
               votes_list.append("1")

#remove the headers
     del candidate_list[0]
     del votes_list[0]

#calculate the total votes

     index = 0
     
     for i in candidate_list:
          total_votes = total_votes + int(votes_list[index])
     
          index = index + 1
          
#find the winner

     ind = 0
     
     max_vote = 0.00

     for i in candidate_list:
          if (int(votes_list[ind]) >= max_vote):
               max_vote = int(votes_list[ind])
               winner = candidate_list[ind]

               ind = ind + 1
          else:
               ind = ind + 1

#          print(winner)

#print required results
     print()
     print("Election Results")
     print("--------------------------")
     print("Total Votes: " + str(total_votes))
     print("--------------------------")

     index = 0

     for i in candidate_list:
          percentage = (int(votes_list[index])/total_votes)*100
          print(candidate_list[index] + ": " + "%.0f%%"%(percentage)+ " (" + str(votes_list[index]) + ")")  

          index = index + 1
                
     print("--------------------------")
     print("Winner: " + winner)

     #print results so far
#     print(candidate_list)
#     print(votes_list)

