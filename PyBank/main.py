
import pandas as pd
csv_path = "resource/03-Python_Homework_PyBank_Resources_budget_data.csv"
budget_data = pd.read_csv(csv_path)


# count month
distinct_month = budget_data['Date'].nunique()
print(f"total month: {distinct_month}")

#sum profit/loss
total_revenue = budget_data["Profit/Losses"].sum()
print(f"total: ${total_revenue}")

#avg p & l
net_change = budget_data.set_index('Date').diff()
avg_change = net_change.mean()
formated_avg = format(float(avg_change),".2f")
#print(formated_avg)
print("Average Change: $", formated_avg,sep=" ")


#max
max_change = net_change.max()
print (f"Greatest Increase in Profits:{max_change}")

#min
min_change =  net_change.min()
print ("Greatest Decrease in Profits: $",min_change,")")