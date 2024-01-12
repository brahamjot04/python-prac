# Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total

new_videos = int(input("Enter the number of new videos rented: "))
old_videos = int(input("Enter the number of old videos rented: "))
total_charge = (new_videos * 3.00) + (old_videos * 2.00)
print("Total charge: $", total_charge)
