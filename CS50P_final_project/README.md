# World Cup Infopack

#### Video Demo:  https://youtu.be/v1VOXTPuG-w

#### Description:

This project uses datasets found on Kaggle (https://www.kaggle.com/datasets/abecklas/fifa-world-cup/data) to produce information for the user regarding the FIFA Men's World Cup.

The necessary modules can be found in the requirements.txt file.

This project was built to extract the files from the fifa-world-cup.zip folder. This zip folder must exists in the working directory prior to running the python program. Download requires a Kaggle account.

Using this program, you can find out about a particular World Cup year, a team that has participated at a World Cup or any individual World Cup Player.

The first stages involve checking for the existance of the world cup zip folder. If it does not exist, then the program will exit.

Following this, the program extracts the necessary csv files from the zip folder.

The next stages involve creating dataframes from the csv files (using the Pandas module) and then cleaning the dataframes - removing unnecessary columns, reformatting certain rows.

The dataframes are later merged and aggregated, for the purpose of the player information.

For the user, they get the option to choose whether they are interested in a particular world cup year, a world cup team, or a world cup player.

Once chosen, the script will output information for them, for the world cup year this includes: year, host nation, winner, runner-up.

For the team: whether they have ever won the world cup and which year(s) if so, and the same for whether they've ever been a runner-up.

For the player: their number of appearances, goals, yellow cards, red cards and whether they have won the world cup or been a runner-up.

The test_project.py file is used to run various tests on the project.py file, to ensure that everything is running as expected.
