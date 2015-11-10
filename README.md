# monopoly-cash-tracker
Python app that helps players organise their Monopoly games by digitising cash flow. (Basically an app version of the Monopoly calculator)

Running from command line:
    `python game.py <num_players> <players> <initial_money>`
      
* `num_players` must be an integer
* `players` is a comma-separated string of the names of the players
* `initial_money` follows the format: <number>(M|K), where M stands for millions, and K stands for thousands
  
Hotkeys:

* Numbers will work
* '+' to add money to selected player
* '-' to deduct money from selected player
* 'space' to initiate a payment from multiple players to a single player
* 'm' to set millions mode
* 'k' to set thousands mode
* 'c' to clear calculator
* 'backspace' to delete previous digit input
* '.' to input decimals
