# 6.11

"""Analyzing the Game of Craps"""

import random
from matplotlib import pyplot as plt
from collections import Counter



def roll_dice():
    """Roll two dices and returns their face values as a tuple."""
    
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    
    return (die1, die2)




def crabs_simulation(max_rolls, total_games):
    """Simulates througth the game of craps multiple times"""
    
    wins_dict = {}

    losses_dict = {}
    
    for _ in range(total_games):
        
        my_point = None
        
        #counter get incremented after each roll and resets after a win or loss
        counter = 0
        
        game_status = "CONTINUE"
        
        while game_status == 'CONTINUE' and counter < max_rolls:
            
            counter += 1
            
            die_values = roll_dice()
            
            sum_of_dice = sum(die_values)

            #first roll of the game
            if counter == 1:
            
                if sum_of_dice in (7, 11):
            
                    game_status = 'WON'
                    
                    #puts current roll number and increments its value in wins dictionary
                    wins_dict[counter] = wins_dict.get(counter, 0) + 1
            
                elif sum_of_dice in (2, 3, 12):
            
                    game_status = 'LOST'
                    
                    losses_dict[counter] = losses_dict.get(counter, 0) + 1
            
                else:
            
                    my_point = sum_of_dice

            #when rolls > 1 then it will move to this condition
            else:
            
                if sum_of_dice == my_point:
            
                    game_status = 'WON'
                    
                    wins_dict[counter] = wins_dict.get(counter, 0) + 1
            
                elif sum_of_dice == 7:
            
                    game_status = 'LOST'
                    
                    losses_dict[counter] = losses_dict.get(counter, 0) + 1


    return (wins_dict, losses_dict)



def display_stats(wins_dict, losses_dict, total_games):
    """Plots the results from the game of crabs"""


    #the dictionary are sorted total are calculated
    sorted_wins_dict = dict(sorted(wins_dict.items()))

    sorted_losses_dict = dict(sorted(losses_dict.items()))

    total_wins = sum(wins_dict.values())

    total_losses = sum(losses_dict.values())

    total_games = total_wins + total_losses



    percentage_wins = (total_wins / total_games) * 100
        
    percentage_losses = (total_losses / total_games) * 100



    #repititions on each roll are counted with the python collections counter 
    counter_for_wins = Counter(wins_dict)

    counter_for_losses = Counter(losses_dict)

    combined_counter = counter_for_wins + counter_for_losses

    combined_dict = dict(combined_counter)
    


    percent_of_wins = (total_wins/total_games)*100

    percent_of_losses = (total_losses/total_games)*100



    print(f'Percentage of wins: {percent_of_wins:.2f}%')

    print(f'Percentage of losses: {percent_of_losses:.2f}%')

    print('Percentage of wins/losses based on total number of rolls:')

    print()

    print(f'{"% Resolved":>25}{"Cummulative %":>29}')

    print(f'{"Rolls":<5}{"on this roll":>20}{"of games resolved":>29}')


    resolved_dict = {}

    cumulative_dict = {}

    cumulative_percentage = 0


    #%resolved on this roll and cumulative % of games resolved
    #is calculated in a loop printed in 3 columns using f-strings
    for roll, outcome in sorted(combined_dict.items()):
            
        percentage_resolved = (outcome / total_games) * 100
            
        cumulative_percentage += percentage_resolved

        cumulative_dict[roll] = cumulative_percentage

        resolved_dict[roll] = percentage_resolved

        print(f'{roll:>5}{percentage_resolved:>19.2f}%{cumulative_percentage:>28.2f}%')




    #sorting and converting the dictionaries into lists before plotting
    sorted_cumulative = dict(sorted(cumulative_dict.items()))
        
    sorted_resolved = dict(sorted(resolved_dict.items()))

    keys_cumulative = list(sorted_cumulative.keys())

    values_cumulative = list(sorted_cumulative.values())

    keys_resolved = list(sorted_resolved.keys())

    values_resolved = list(sorted_resolved.values())



    plt.xlabel('Number of rolls')

    plt.ylabel('Games resolved on roll') 

    plt.title('Resolved on rolls')

    plt.plot(keys_resolved, values_resolved, label = "Resolved on roll %")

    plt.plot(keys_cumulative, values_cumulative, label = "Cumulative %")


    plt.legend()
    plt.show()



max_rolls = 25

total_games = 1000000



wins, losses = crabs_simulation(max_rolls,total_games)

display_stats(wins, losses, total_games)

