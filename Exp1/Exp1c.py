# Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total

print("Welcome to Five Star Retro Video")
print("New videos: $3.00 each")
print("Old videos: $2.00 each")
print("Do you want old videos or new videos?")
switch = input("Enter 'n' for new videos and 'o' for old videos: ")
if switch == 'n' | switch == 'N':
    new_videos = int(input("Enter the number of new videos rented: "))
    total_charge = new_videos * 3.00
    print("Total charge: $", total_charge)
elif switch == 'o' | switch == 'O':
    old_videos = int(input("Enter the number of old videos rented: "))
    total_charge = old_videos * 2.00
    print("Total charge: $", total_charge)
else:
    print("Invalid input")
