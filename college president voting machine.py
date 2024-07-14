def main():
    print("Welcome to the College President Voting System!")

    candidates = ["prince agarwal", "vishal agarwal", "aayush sharma"]
    votes = {candidate: 0 for candidate in candidates}

    while True:
        print("\nCandidates:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")

        choice = input("Enter the number of your chosen candidate (or 'q' to quit): ")

        if choice == 'q':
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(candidates):
                votes[candidates[choice - 1]] += 1
                print(f"Thank you! You voted for {candidates[choice - 1]}.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nVoting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

if __name__ == "__main__":
    main()
