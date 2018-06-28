# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:46:37 2018

@author: ali-j
"""
'''
Python 3.6
This is a program that calculates apportionment of seats based on the D'Hondt \
method of Proportional Representation. This is soley for a list system. An \
Additional Member System calculator will be upcoming.
'''

import numpy as np
from matplotlib import pyplot as plt

candidates = []
votes = []
seats = []

seats_to_fill = int(input("How many seats to fill: "))
seats_filled = 0

party_lists = int(input("How many party lists are there in this count: "))

print("For the purposes of this calculator please input any Independent candidates \
or lists with only one person either as \'Independent\' or \'Ind\'")

def add_vote(integer):
    votes = float(input("How many votes did the " + str(candidate_i) + " list recieve: "))
    return votes

for i in range(party_lists):
    candidate_i = input("Input list " + str(i + 1) +  " : ")
    try:
        votes_i = add_vote(i)
    except ValueError:
        print("That is not a number. Please Try again:")
        votes_i = add_vote(i)
    candidates.append(candidate_i)
    votes.append(votes_i)
    seats.append(0)


    
np_candidates = np.array(candidates)
np_votes = np.array(votes)
np_seats = np.array(seats)

print("I, the Acting Returning Officer, hereby give notice that the total \
number of votes given for each candidate at the election was as follows: \n")
for i in range(len(np_candidates)):
    print(str(np_candidates[i]) + ": " + str(np_votes[i]))
print()

while(seats_filled < seats_to_fill):
    criterion = np.array(votes)
    for i in range(len(np_candidates)):
        if((np_candidates[i].upper() == 'IND' or np_candidates[i].upper() == "INDEPENDENT") and (np_seats[i] == 1)):
            criterion[i] = 0
    criterion = criterion / (1 + np_seats)
    max_index = np.argmax(criterion)
    np_seats[max_index] += 1
    seats_filled += 1


print("And that the following seats have been duly granted to each list in \
this constituency: \n")
for i in range(len(np_candidates)):
    if(np_seats[i] != 0 ):
        print(str(np_candidates[i]) + ": " + str(np_seats[i]))


ask_pie = input("Do you want to see a chart of the results? If so push \"Y\" If not hit any other key: ")
if (ask_pie == "Y" or ask_pie == "y"):
    plt.pie(np_seats)
    plt.legend(np_candidates)
    plt.title("Share of the Seats")
    plt.show()
    plt.clf()
    plt.pie(np_votes)
    plt.legend(np_candidates)
    plt.title("Share of the votes")
    plt.show()