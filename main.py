import pandas as pd


def main():
    # Load the original catalog into a DataFrame.
    games = pd.read_csv("video_games_raw.csv")

    print("VIDEO GAME CATALOG MANAGER")

    # Keep asking until the user enters a valid row number.
    while True:
        try:
            row_number = int(input(f"\nEnter a row number (1-{len(games)}): "))
            if 1 <= row_number <= len(games):
                break
        except ValueError:
            pass

        print("Please enter a whole number in the displayed range.")

    # The user counts from 1, but .iloc counts from 0.
    selected_game = games.iloc[row_number - 1]

    print("\nSelected Game:")
    print(f"Title: {selected_game['Title']}")
    print(f"Platform: {selected_game['Platform']}")
    print(f"Genre: {selected_game['Genre']}")
    print(f"Rating: {selected_game['Rating']}")
    print(f"Current Status: {selected_game['Status']}")

    # Update one cell using the selected row's index label and column name.
    new_status = input("\nEnter a new status: ").strip()
    games.at[selected_game.name, "Status"] = new_status

    # Start every game at "No", then use .loc to update games that meet both criteria.
    games["Recommended"] = "No"
    qualifies = (games["Rating"] >= 8) & (games["Price"] <= 40)
    games.loc[qualifies, "Recommended"] = "Yes"

    # Use .query() to find recommended games and display the requested columns.
    recommended_games = games.query("Recommended == 'Yes'")
    print("\nRecommended Games:")
    print(recommended_games[["Title", "Platform", "Price", "Rating"]])

    # Write the updated catalog to a separate CSV without the DataFrame index.
    games.to_csv("video_games_cleaned.csv", index=False)
    print("\nThe catalog has been updated.")
    print("Saved as video_games_cleaned.csv.")


if __name__ == "__main__":
    main()