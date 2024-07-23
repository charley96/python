# kaggle datasets download -d abecklas/fifa-world-cup
from zipfile import ZipFile
import os
import sys
import pandas as pd
import random as r
import numpy as np

url = "https://www.kaggle.com/datasets/abecklas/fifa-world-cup/data"
zipped = "fifa-world-cup.zip"
paths = ["WorldCupMatches.csv", "WorldCupPlayers.csv", "WorldCups.csv"]


def main():
    global zipped, paths
    find_zip(zipped)
    try:
        extract_files(zipped, paths)
    except FileNotFoundError:
        sys.exit()

    world_cup_dict = create_dfs(paths)

    world_cup_df = clean_world_cup(world_cup_dict["WorldCups"])
    matches_df = clean_matches(world_cup_dict["WorldCupMatches"])
    players_df = formatting_players(world_cup_dict["WorldCupPlayers"])
    merged = merging_players(players_df, matches_df, world_cup_df)
    grouped = player_aggregation(merged)

    teams_list = get_teams(matches_df)
    p_dict = player_dict(grouped)
    c_dict = cup_dict(world_cup_df)
    w_dict, runner_up_dict = team_dicts(c_dict)
    while True:
        output = input(
            "Would you like to learn about a: \n 1) World Cup \n 2) Team \n 3) Player\nOr press 'Q' to exit.\n"
        )
        if output.lower() in ["1", "world cup"]:
            while True:
                try:
                    year = int(input("What year are you interested in?\n"))
                    print(cup_stats(year, c_dict))
                    break
                except (ValueError, KeyError):
                    print("Sorry, that's not a valid World Cup year.")
                    continue
        elif output.lower() in ["2", "team"]:
            while True:
                team = (
                    input(
                        "What international side are you interested in?\nOr press 'R' for a random team\n"
                    )
                    .strip()
                    .title()
                )
                if team == "R":
                    team = get_rand_country(teams_list)
                exists = country_check(team, teams_list)
                if exists == True:
                    won, runner_up = country_nums(team, w_dict, runner_up_dict)
                    wins, seconds = country_stats(won, runner_up, team)
                    print(wins)
                    try:
                        for i in w_dict[team]:
                            print(i)
                    except KeyError:
                        pass
                    print(seconds)
                    try:
                        for i in runner_up_dict[team]:
                            print(i)
                    except KeyError:
                        pass
                    break
                else:
                    print(
                        "Sorry, that is not a valid international side that has competed in a World Cup."
                    )
                    continue
        elif output.lower() in ["3", "player"]:
            while True:
                player = (
                    input(
                        "What player do you want to learn about?\nOr press 'R' for a random player\n"
                    )
                    .strip()
                    .title()
                )
                if player == "R":
                    chosen_player = get_rand_player(p_dict)
                else:
                    players_list = player_list(player, p_dict)
                    chosen_player = player_select(players_list)
                try:
                    output = player_stats(chosen_player, p_dict)
                    print(output)
                    break
                except KeyError:
                    print(
                        "Sorry, please enter a valid player who has featured in a World Cup."
                    )
                    continue
        elif output.lower() == "q":
            sys.exit("Thanks for participating.")
        else:
            print("Sorry, that is not one of the available options.")


def find_zip(zip_file):
    """
    Function checks whether the zip file containing the world cup data exists.
    If it doesn't exist then the program is aborted.
    """
    global url
    if os.path.exists(zip_file):
        return True
    else:
        sys.exit(f"Please download the world cup zip file from this location: {url}")


def extract_files(zip_file, files):
    """
    Checks whether files have already been extracted from the zip folder.
    If they have been, then the process is skipped.
    Otherwise, files are extracted to the working directory.
    """
    exists = []
    for f in files:
        isExist = os.path.exists(f)
        exists.append(isExist)
    if False in exists:
        with ZipFile(zip_file, "r") as unzip:
            unzip.extractall(path="")
        print("Files Extracted")
    else:
        print("Files already exist.")


def create_dfs(paths):
    """
    Create dataframes from the world cup files.
    Returns a dictionary containing the name of the file (minus the csv extension) and the corresponding dataframe
    """
    df_dict = {}
    for p in paths:
        df = pd.read_csv(p)
        name = p[: p.index(".")]
        df_dict[name] = df
    return df_dict


def clean_world_cup(df):
    """
    Working with the world cup file
    Combines West Germany and Germany
    Sets the index to be the year of the World Cup
    """
    df = df.replace("Germany FR", "Germany")
    df = df.set_index("Year")
    return df


def clean_matches(df):
    """
    Removes unnecessary columns from matches dataframe
    Combines West Germany and Germany.
    Renames Cote d'Ivoire due to issues in importing accented characters.
    """
    columns_to_drop = [
        "Datetime",
        "Stage",
        "Stadium",
        "City",
        "Win conditions",
        "Attendance",
        "Half-time Home Goals",
        "Half-time Away Goals",
        "Referee",
        "Assistant 1",
        "Assistant 2",
        "RoundID",
    ]
    df = df.drop(columns_to_drop, axis=1)
    df = df.replace("Germany FR", "Germany")
    df = df.replace("Cï¿½te d'Ivoire", "Cote d'Ivoire")
    return df


def get_teams(matches_df):
    """
    Creates a list of all teams to have competed in a World Cup.
    """
    teams_list = []
    home_teams = matches_df["Home Team Name"]
    away_teams = matches_df["Away Team Name"]

    for i in home_teams:
        if i not in teams_list:
            teams_list.append(i)

    for j in away_teams:
        if j not in teams_list:
            teams_list.append(j)

    teams_list.remove(np.nan)
    return teams_list


def formatting_players(df):
    """
    Removes unnecessary columns from players dataframe
    Removes the space between names if a full stop is used.
    Use the events column to create columns for goals, yellow cards and red cards.
    """
    columns_to_drop = ["RoundID", "Coach Name", "Line-up", "Shirt Number", "Position"]
    df = df.drop(columns_to_drop, axis=1)
    df["Player Name"] = df["Player Name"].apply(
        lambda x: x.replace("", "") if "." in x else x
    )
    events = df["Event"]
    goals = []
    yellows = []
    reds = []

    for i in events:
        i = str(i)
        scored = i.count("G")
        y_cards = i.count("Y")
        r_cards = i.count("R")
        goals.append(scored)
        yellows.append(y_cards)
        reds.append(r_cards)

    df = df.drop(columns=["Event"])
    df = df.assign(Goal=goals, Yellow=yellows, Red=reds)
    return df


def merging_players(players_df, matches_df, cup_df):
    """
    Merges all 3 dataframes and drops any further unneeded columns.
    Get the team name using the team initials and home team/away team name
    Determine whether a team was a world cup winner or runner up during a given world cup.
    Returns the filename of a new file containing the merged dataframe in a csv.
    """
    filename = "merged_df.csv"
    if os.path.exists(filename):
        return filename
    else:
        merged = players_df.merge(matches_df, how="left", on="MatchID")

        cup_columns_to_drop = [
            "Country",
            "Third",
            "Fourth",
            "GoalsScored",
            "QualifiedTeams",
            "MatchesPlayed",
            "Attendance",
        ]
        cup_df = cup_df.drop(cup_columns_to_drop, axis=1)

        merged_df = merged.merge(cup_df, how="left", left_on="Year", right_on="Year")
        merged_df["Team Name"] = merged_df.apply(
            lambda row: (
                row["Home Team Name"]
                if row["Team Initials"] == row["Home Team Initials"]
                else row["Away Team Name"]
            ),
            axis=1,
        )

        merged_df["Won"] = merged_df.apply(
            lambda row: True if row["Team Name"] == row["Winner"] else False, axis=1
        )
        merged_df["runner_up"] = merged_df.apply(
            lambda row: True if row["Team Name"] == row["Runners-Up"] else False, axis=1
        )
        merged_columns_to_drop = [
            "Home Team Name",
            "Away Team Name",
            "Team Initials",
            "Home Team Initials",
            "Away Team Initials",
            "Winner",
            "Runners-Up",
        ]
        merged_df = merged_df.drop(merged_columns_to_drop, axis=1)
        merged_df.to_csv(filename)
        return filename


def player_aggregation(filename):
    """
    Creates an aggregated dataframe for player data, using the merged dataframe file.
    Aggregates on Player Name and Team Name, to differentiate between players of the same surname that may have
    played for different countries.
    Returns a dataframe.
    Also checks that the inputted file is a csv.
    """
    if filename.endswith(".csv"):
        merged_df = pd.read_csv(filename)

        grouped_df = merged_df.groupby(["Player Name", "Team Name"]).agg(
            {
                "Goal": ["sum"],
                "Yellow": ["sum"],
                "Red": ["sum"],
                "Year": ["count"],
                "Won": ["max"],
                "runner_up": ["sum"],
            }
        )
        return grouped_df
    else:
        sys.exit(
            "Incorrect file format. Please ensure that the merged dataframe is saved as a csv file."
        )


def player_dict(grouped_df):
    """
    returns a dictionary from the aggregated dataframe
    Keys are player name and country name.

    """
    player_dict = grouped_df.to_dict(orient="index")
    player_dict_new = {}

    for player_name, stats_dict in player_dict.items():
        new_stats_dict = {}
        for key_tuple, value in stats_dict.items():
            new_key = key_tuple[0]
            if new_key == "Year":
                new_key = "Appearances"
                new_stats_dict[new_key] = value
            else:
                new_stats_dict[new_key] = value
        player_dict_new[player_name] = new_stats_dict
    return player_dict_new


def cup_dict(cup_df):
    """
    returns a dictionary, where the world cup year is the key.
    """
    cup_dict = cup_df.to_dict(orient="index")
    return cup_dict


def team_dicts(cup_dict):
    """
    Returns 2 dictionaries, for winners and runners-up
    Keys are the team names, whilst values are the years in which they won/came second.
    """
    winner_dict = {}
    runner_up_dict = {}

    for year, stats_dict in cup_dict.items():
        winner_key = stats_dict["Winner"]
        runner_up_key = stats_dict["Runners-Up"]

        winner_dict.setdefault(winner_key, [])
        runner_up_dict.setdefault(stats_dict["Runners-Up"], [])

        winner_dict[winner_key].append(year)
        runner_up_dict[runner_up_key].append(year)

    return winner_dict, runner_up_dict


def cup_stats(year, cup_dict):
    """
    Final output for the world cup year data.
    Should read in a year from the user, plus the cup dictionary
    Output is an f string, stating the world cup year, host nation, winner and runner-up.
    """
    world_cup_year = cup_dict[year]
    return f"World Cup Year: {year}\nHost Nation: {world_cup_year['Country']}\nWinner: {world_cup_year['Winner']}\nRunner-Up: {world_cup_year['Runners-Up']}"


def get_rand_country(teams_list):
    """
    returns a random country from the list of countries to have competed at the world cup.
    """
    size = len(teams_list)
    num = r.randint(0, size - 1)
    country = teams_list[num]
    return country


def country_check(country, teams_list):
    """
    Checks whether the user input team has competed at a world cup.
    If the user wanted a random team, that automatically returns True.
    """
    if country == "R":
        return True
    elif country in teams_list:
        return True
    else:
        return False


def country_nums(country, winner_dict, runner_up_dict):
    """
    obtains the number of world cup wins and 2nd places for the given team from the user input.
    """
    if country in winner_dict.keys():
        num_wins = len(winner_dict[country])
    else:
        num_wins = 0

    if country in runner_up_dict.keys():
        num_second = len(runner_up_dict[country])
    else:
        num_second = 0

    return num_wins, num_second


def country_stats(num_wins, num_second, country):
    """
    Final output for the world cup team section.
    Outputs whether a team has won the world cup/been runner up.
    Year of win/2nd place is outputted in the main function.
    """
    if num_wins > 0:
        wins = f"{country} has won the World Cup {num_wins} time(s).\nThey won it in the following year(s):"
    else:
        wins = f"{country} has never won the World Cup."

    if num_second > 0:
        seconds = f"{country} has been runner up {num_second} time(s).\nThey came 2nd in the following year(s):"
    else:
        seconds = f"{country} has never been runner-up at the World Cup."

    return wins, seconds


def player_list(player_name, player_dict):
    """
    returns a list of all players in the player dictionary that match the user input
    """
    players = []
    for key in player_dict.keys():
        if player_name.lower() in key[0].lower():
            players.append(key)
    return players


def player_select(player_list):
    """
    uses the player list to determine who the user wants to learn about
    If the player list only has one name in, then that name is automatically chosen
    If the user gave a player that hasn't featured in a world cup, that player is assigned to be 0.
    Otherwise, the user is then given the option to select which player they want to learn about, from the list of player names
    and their country.
    Accepted input is a number only.
    """
    if len(player_list) == 1:
        player = player_list[0]
    elif len(player_list) == 0:
        player = 0
    else:
        print("Which of the following players did you mean?")
        indexes = []
        for index, player in enumerate(player_list):
            indexes.append(index)
            print(f"{index+1}: {player[0]} from {player[1]}")
        while True:
            try:
                option = int(input("\nPlease select from the numbers listed: "))
                if option - 1 in indexes:
                    player = player_list[option - 1]
                    break
                else:
                    continue
            except ValueError:
                continue
    return player


def get_rand_player(player_dict):
    """
    gets a random player from the player dictionary
    Used if the user indicates they want a random player
    """
    player = r.choice(list(player_dict.keys()))
    return player


def player_stats(player, player_dict):
    """
    Final output for player data.
    Outputs who the player played for and how many world cup appearances they made
    How many goals they scored, as well as yellow and red cards received
    Finally, indicates whether they won the world cup, or were a runner-up.
    """
    player_info = player_dict[player]
    line1 = f"{player[0]} played for {player[1]}, making {player_info['Appearances']} appearances."
    line2 = f"They scored {player_info['Goal']} goals, received {player_info['Yellow']} yellow and {player_info['Red']} red cards."
    if player_info["runner_up"] == True:
        line3 = "They received a runners-up medal at the World Cup."
    elif player_info["Won"] == True:
        line3 = "They won the World Cup during their career."
    else:
        line3 = "They have not won the World Cup, nor been a runner-up."
    return f"{line1}\n{line2}\n{line3}\n"


if __name__ == "__main__":
    main()