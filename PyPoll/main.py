import csv
import os

# File paths
file_path = "Resources/election_data.csv"
output_folder = "analysis"
output_file = os.path.join(output_folder, "election_results.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
try:
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        next(csvreader)

        # Count the total number of votes and tally votes for each candidate
        for row in csvreader:
            total_votes += 1
            candidate = row[2]

            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

    # Determine the winner based on popular vote
    for candidate, votes in candidates.items():
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Export the analysis to a text file
    with open(output_file, "w") as f:
        f.write("Election Results\n")
        f.write("-------------------------\n")
        f.write(f"Total Votes: {total_votes}\n")
        f.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        f.write("-------------------------\n")
        f.write(f"Winner: {winner}\n")
        f.write("-------------------------\n")

    print("Analysis complete. The results have been saved to 'election_results.txt'.")

except FileNotFoundError:
    print("Error: The file 'election_data.csv' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
