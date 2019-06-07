import pandas as pd
import numpy as np
csv_path = 'Resource/03-Python_Homework_PyPoll_Resources_election_data.csv'
Election_Data = pd.read_csv(csv_path)

print("Election Results")
print('---------------------------------')

# total votes
total_votes = Election_Data['Voter ID'].nunique()
print(f"Total Voters: {total_votes}")
print('---------------------------------')

# group by candidate
candidate_table = Election_Data.groupby(["Candidate"])
candidate_group = pd.DataFrame(candidate_table['Voter ID'].agg(np.size))
candidate_group_sort = candidate_group.sort_values('Voter ID',ascending = False)

#calculate percentage
total_votes1 = candidate_group_sort['Voter ID'].sum()
candidate_group_sort['Percentage']= candidate_group_sort['Voter ID']/total_votes1
#format %
candidate_group_sort['Percentage'] = pd.Series(["{0:.3f}%".format(per * 100) for per in candidate_group_sort['Percentage']],index=candidate_group_sort.index)
#format count
candidate_group_sort["string_Voter_ID"]="("+candidate_group_sort['Voter ID'].astype(str) + ")"
#covert index to a column
candidate_group_sort['Candidate1']=candidate_group_sort.index


#show results in 2 columns & remove header
candidate_group_sort_display = candidate_group_sort[['Percentage','string_Voter_ID']]
candidate_group_sort_display.columns = ["",""]
del candidate_group_sort_display.index.name
print(candidate_group_sort_display)

#Winner
winner = candidate_group_sort.iloc[0,3]
print()
print(f"Winner: {winner}")
print('---------------------------------')




