import random

# Return a list of choices for the player.
# Return a list of random choices.
def get_choices():

    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    
    choices = {
        'player': player_choice,
        'computer': computer_choice,
        }

    return choices


# Check if player has win.
def check_win(player, computer):
    print(f'You chose {player}, computer choose {computer}')
    if player == computer:
        return 'It\'s a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes Scissors! You have win!'      
        else:
            return 'Paper covers Rock! You lose.'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers Rock! You have win!'      
        else:
            return 'Scissors cuts Paper! You lose.'

    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts Paper! You have win!'      
        else:
            return 'Rock smashes Scissors! You lose.'
    
    # Returns a list of choices.
choices = get_choices()

result = check_win(choices['player'], choices['computer'])


print(result)


