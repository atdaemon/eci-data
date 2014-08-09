#!/usr/bin/env python
"""
input line format =  Candidate,Party,Votes,State,Constituency,State-code,Constituency-code 
print party name , vote count, vote percentage
"""
from collections import Counter
import csv
import sys

csv_path = "input/parliament-elections/election2014/eci-candidate-wise.csv"
csv_out = "output/party_wise_votes_count.csv"
CSV_OUT_HEADER_ROW = ["Party Name","Vote Count","Vote Percentage","Seats Won","Seats Percentage"]

CANDIDATE = 0
PARTY = 1
VOTES = 2
STATE = 3
CONSTITUENCY = 4
STATE_CODE = 5
CONSTITUENCY_CODE = 6


count = Counter()
with open(csv_path) as f :
	csv_reader = csv.reader(f)
	for line_num , line in enumerate(csv_reader) :
		if line_num == 0 :
			continue
		#line = line.strip()
#		print "LINE" , line_num , " >> " , line
		line_data = line#.split(',')
		print line_data[PARTY] , line_data[VOTES]
		count.update(Counter({line_data[PARTY] : int(line_data[VOTES])}))
#counting done. Do calc now

#Find total votes
total_votes = sum([count[party] for party in count])
print "total_votes = ",total_votes

#find total seat wins
winsDict = {} #partyName:Seats
csv_in="input/parliament-elections/election2014/eci-constituency-wise.csv"
LEADING_PARTY=3
with open(csv_in) as inFile :
	csv_reader = csv.reader(inFile) 
	for line in csv_reader :
		party = line[LEADING_PARTY]
#		print "Winning party = ",party
		if party in winsDict :
			winsDict[party]+=1
		else :
			winsDict[party] = 1
print winsDict

total_seats = sum(winsDict.values())
print "Total_seats = ", total_seats

	
with open(csv_out,'w') as out_file :
	writer = csv.writer(out_file)
	writer.writerow(CSV_OUT_HEADER_ROW)
	for partyData in count.most_common() :
		print partyData
		party =partyData[0]
		partyVotes = count[party]
		votePercent = float(partyVotes*100)/total_votes
		votePercentStr = "{:.10f}".format(votePercent)
		seatsWon = winsDict[party] if party in winsDict else 0
		seatPercent = float(seatsWon*100)/total_seats
		seatPercentStr = "{:.2f}".format(seatPercent)
		writer.writerow([party , partyVotes, votePercentStr, seatsWon, seatPercentStr])
#print count
print "output file :"+csv_out
