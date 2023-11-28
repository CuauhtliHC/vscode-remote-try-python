#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Array with values scissors, paper, rock
values = ["scissors", "paper", "rock"]

# function to return random value (scissors, paper, rock)
values = ["scissors", "paper", "rock"]

def random_selection():
    while True:
        selectionUser = input("Enter your choice (scissors, paper, rock): ")
        selectionValue = random.choice(values)
        print("Machine selection: " + selectionValue)
        if selectionUser == selectionValue:
            print("It's a tie!")
        elif selectionUser == "scissors":
            if selectionValue == "paper":
                print("You win!")
            else:
                print("You lose!")
        elif selectionUser == "paper":
            if selectionValue == "rock":
                print("You win!")
            else:
                print("You lose!")
        elif selectionUser == "rock":
            if selectionValue == "scissors":
                print("You win!")
            else:
                print("You lose!")
        else:
            print("Invalid selection, please try again.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

random_selection()