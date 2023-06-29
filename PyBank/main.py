import csv
import os

# Set the path to the CSV file
csvpath = "Resources/budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    csvheader = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the date and profit/loss values from the row
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total of profit/loss
        net_total += profit_loss
        
        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profit/loss
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding dates for the greatest increase and decrease
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the financial analysis to the terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Create the output folder if it doesn't exist
output_folder = "analysis"
os.makedirs(output_folder, exist_ok=True)

# Export the financial analysis to a text file
output_path = os.path.join(output_folder, "financial_analysis.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Analysis complete. The results have been saved to 'financial_analysis.txt' in the 'analysis' folder.")
