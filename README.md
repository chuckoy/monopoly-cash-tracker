# monopoly-cash-tracker
Python app that helps players organise their Monopoly games by digitising cash flow. (Basically an app version of the Monopoly calculator).

Running from command line:
    `python game.py -players <players> -initial_money <initial_money>`
      
* `players` is a comma-separated string of the names of the players.
* `initial_money` follows the format: `<number>` (M|K), where M stands for millions, and K stands for thousands.
  
Hotkeys:

* Numbers work as input to the calculator.
* '+' to add money to selected player.
* '-' to deduct money from selected player.
* 'space' to initiate a payment from multiple players to a single player.
* 'm' to set millions mode.
* 'k' to set thousands mode.
* 'c' to clear calculator.
* 'backspace' to delete previous digit input.
* '.' to input decimals.

Developed on Python 3 in an Ubuntu 12.04 instance running on Windows 10.

# Reflections:

I hadn't really studied testing when I was developing this app, so it's lacking tests. When I've finished my study on Ruby on Rails and Javascript I'll get back to this to polish my testing skills in Python in general.

When developing this app, I first started with the backend (making sure cash amounts were being tracked properly and that the transactions were carried out without bugs), migrating the system to use the frontend `tkinter` when I had finished the backend. It's my general approach in developing software with a GUI but I wonder if it would be better to develop the front-end first. Or perhaps develop both ends by modules.
