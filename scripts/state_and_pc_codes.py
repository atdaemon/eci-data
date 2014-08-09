#!/usr/bin/env python
"""
input file = input/parliament-elections/election2014/eci-candidate-wise.csv
input line format =  Candidate,Party,Votes,State,Constituency,State-code,Constituency-code 
output files = 
output/state_codes.csv - state-code,state-name
output/pc_codes.csv - state-code,state-name,pc-code,pc-name
"""
import csv

csv_path = "input/parliament-elections/election2014/eci-candidate-wise.csv"
csv_out_states = "output/state_codes.csv"
csv_out_pc = "output/pc_codes.csv"
CSV_STATES_HEADER_ROW = ["State Code","State Name"]
CSV_PC_CODES_HEADER_ROW = ["State Code","State Name","PC code","PC name"]

CANDIDATE = 0
PARTY = 1
VOTES = 2
STATE = 3
CONSTITUENCY = 4
STATE_CODE = 5
CONSTITUENCY_CODE = 6


#count = Counter()
states = {}
pc_codes = {}
with open(csv_path) as f :
	csv_reader = csv.reader(f)
	for line_num , line_data in enumerate(csv_reader) :
		if line_num == 0 :
			continue
#		print "LINE" , line_num , " >> " , line_data
		state = line_data[STATE]
		state_code = line_data[STATE_CODE]
		if state_code not in states.keys() :
			states[state_code] = state
			pc_codes[state_code] = {}
		pc_code = line_data[CONSTITUENCY_CODE]
		pc_name = line_data[CONSTITUENCY]
		if pc_code not in pc_codes[state_code].keys() :
			pc_codes[state_code][pc_code] = pc_name
		
		print line_data[STATE],line_data[STATE_CODE],line_data[CONSTITUENCY_CODE],line_data[CONSTITUENCY]


with open(csv_out_states,'w') as out_file :
	writer = csv.writer(out_file)
	writer.writerow(CSV_STATES_HEADER_ROW)
	for state_code in sorted(states.keys()) :
		writer.writerow([state_code,states[state_code]])
print "output file :"+csv_out_states

with open(csv_out_pc,'w') as out_file :
	writer = csv.writer(out_file) 
	writer.writerow(CSV_PC_CODES_HEADER_ROW)
	for state_code in sorted(pc_codes.keys()) :
		for pc_code in sorted(map(int,pc_codes[state_code].keys())) :
			pc_code = str(pc_code)
			writer.writerow([state_code,states[state_code],pc_code,pc_codes[state_code][pc_code]])
print "output file :"+csv_out_pc
