# Reset the candidate variables
joe_votes = 0
charlie_votes = 0
mike_votes = 0

print("Enter the vote or 0 to finish")
print("1 - Joe")
print("2 - Charlie")
print("3 - Mike")

# Start an infinite loop
while True:
    # Read the vote
    vote = int(input("Enter vote or 0 to finish: "))

    # Count the vote
    if vote == 1:
        joe_votes = joe_votes + 1
    elif vote == 2:
        charlie_votes = charlie_votes + 1
    elif vote == 3:
        mike_votes = mike_votes + 1
    else:
        if vote != 0:
            print("Invalid vote, enter: 1, 2 or 3.")

    # This if simulates the exit condition at the end of the loop
    if vote == 0:
        break # Force the loop to stop

print(f"1 - Joe: {joe_votes} votes.")
print(f"2 - Charlie: {charlie_votes} votes.")
print(f"3 - Mike: {mike_votes} votes.")