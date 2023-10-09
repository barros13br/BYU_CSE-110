

first_choice = input("You were at summer camp and it was night, while everyone was sleeping you heard a noise," 
      "what do you do? (WAKE UP your friends or GO SEE what it is on your own): ")

if first_choice.capitalize() == "Wake up":
    print('You wake up your friends and together you discover what made the noise,'
          '"look! it is a rabbit!" said one of his friends, and soon everyone went back to sleep.')
    second_choice_pt1 = input("")


if first_choice.capitalize() == "Go see":
    second_choice_pt2 = input("You get up and go see what made the noise. When you get there you find nothing and lose your way back to camp. what do you do?"
                            "(SCREAMS for help, or turns on the flashlight, be careful, the place can be dangerous): ")
    if second_choice_pt2.capitalize() == "Screams":
        third_chooice_pt2 = input("you scream for help and a noise of something big and heavy starts approaching you very quickly through the bushes!"
                               " what would you do? (turn on the FLASHLIGHT and point in that direction or RUN): ")
        if third_chooice_pt2.capitalize() == "Flashligt":
            print("you see a giant and hungry bear, he makes the first attack and hits a bag of marshmallows that you were carrying, and accidentally one falls right"
                   "into his mouth, he likes it, and becomes your friend companion, you both return to camp and in the morning everyone is impressed with your new mascot. [The End.]")