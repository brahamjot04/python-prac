import random

# In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so on. A little mathematical analysis reveals that there are not enough ways to win to make the game worthwhile; however, because many people’s eyes glaze over at the first mention of mathematics, your challenge is to write a program that demonstrates the futility of playing the game. Your program should take as input the amount of money that the player wants to put into the pot and play the game until the pot is empty. At that point, the program should print the number of rolls it took to break the player, as well as the maximum amount of money in the pot.


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def play_lucky_sevens(initial_pot):
    max_pot = initial_pot
    rolls = 0

    while initial_pot > 0:
        rolls += 1
        if roll_dice() == 7:
            initial_pot += 4
        else:
            initial_pot -= 1
        if initial_pot > max_pot:
            max_pot = initial_pot

    print("Number of rolls:", rolls)
    print("Maximum amount of money in the pot:", max_pot)


# Example usage
initial_pot = 20
play_lucky_sevens(initial_pot)
