#Joe Brennan
#CS 021 Final Project
#Uno game

import random

def main ():
    
    #Make lists sorting cards into colors
    red_cards = ["red 0", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4", "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9","red draw 2", "red draw 2", "red reverse", "red reverse", "red skip", "red skip", "red",]
    blue_cards = ["blue 0", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4", "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9", "blue draw 2", "blue draw 2", "blue reverse", "blue reverse", "blue skip", "blue skip", "blue"]
    yellow_cards = ["yellow 0", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4", "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9", "yellow draw 2", "yellow draw 2", "yellow reverse", "yellow reverse", "yellow skip", "yellow skip", "yellow"] 
    green_cards = ["green 0", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4", "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9", "green draw 2", "green draw 2", "green reverse", "green reverse", "green skip", "green skip", "green"] 
    wild_cards = ["wild (pick color)", "wild (pick color)", "wild (pick color)", "wild (pick color)", "wild draw 4", "wild draw 4", "wild draw 4", "wild draw 4"]

    #Make lists sorting into card numbers or type of card
    zero_cards = ["red 0", "blue 0", "green 0", "yellow 0"]
    one_cards = ["red 1", "blue 1", "green 1", "yellow 1"]
    two_cards = ["red 2", "blue 2", "green 2", "yellow 2"]
    three_cards = ["red 3", "blue 3", "green 3", "yellow 3"]
    four_cards = ["red 4", "blue 4", "green 4", "yellow 4"]
    five_cards = ["red 5", "blue 5", "green 5", "yellow 4"]
    six_cards = ["red 6", "blue 6", "green 6", "yellow 6"]
    seven_cards = ["red 7", "blue 7", "green 7", "yellow 7"]
    eight_cards = ["red 8", "blue 8", "green 8", "yellow 8"]
    nine_cards = ["red 9", "blue 9", "green 9", "yellow 9"]
    draw_two_cards = ["red draw 2", "blue draw 2", "green draw 2", "yellow draw 2"]
    reverse_cards = ["red reverse", "blue reverse", "green reverse", "yellow reverse"]
    skip_cards = ["red skip", "blue skip", "green skip", "yellow skip"]
    wild_pick_color = ["wild (pick color)"]
    wild_draw_four = ["wild draw 4"]

    #Make deck
    deck = ["red 0", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4", "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9","red draw 2", "red draw 2", "red reverse", "red reverse", "red skip", "red skip", "blue 0", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4", "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9", "blue draw 2", "blue draw 2", "blue reverse", "blue reverse", "blue skip", "blue skip", "yellow 0", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4", "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9", "yellow draw 2", "yellow draw 2", "yellow reverse", "yellow reverse", "yellow skip", "yellow skip", "green 0", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4", "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9", "green draw 2", "green draw 2", "green reverse", "green reverse", "green skip", "green skip", "wild (pick color)", "wild (pick color)", "wild (pick color)", "wild (pick color)", "wild draw 4", "wild draw 4", "wild draw 4", "wild draw 4"] 

    #Initialize play_again variable and set to y for yes
    play_again = "y"

    #Set up loop to continue playing games as long as user selects y to play again
    while play_again == "y":

        #Initialize user_hand list to keep track of cards in user's hand
        user_hand = []
        #Initialize comp_hand list to keep track of cards in computer's hand
        comp_hand = []




        #Dealing cards to user and computer

        #Call deal_card function to deal cards to user
        user_hand = deal_cards(deck, user_hand)
        
        #Call deal_card function to deal cards to computer
        comp_hand = deal_cards(deck,comp_hand)


        #Call begin_game function to flip first card and start the game
        played_card = begin_game (deck)

        #if played_card in wild_cards user chooses color
        if played_card in wild_cards:
            print ("A wild card was flipped! User must choose a color!")
            #User input color
            color = input("Choose a color: ")
            #Make color lowercase
            color = color.lower()
            #Color must be red blue yellow or green
            while not(color == "red") and not(color == "blue") and not(color == "yellow") and not(color == "green"):
                print ("Invalid color entered. Please try again")
                color = input("Choose a color: ")
                color = color.lower()
            #Assign the played card to that chosen color
            played_card = color

            print ("\n")
        




            
        #Continue game until either user or computer has 0 cards in hand
        while len(user_hand) > 0 and len(comp_hand) > 0:

            
            #Call user_turn function
            played_card, ignore_action = user_turn (deck, user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)
            


            #Checking to see if user played an action or wild card
            #If they did then perform the actions of those cards
            
            #Ignore action must be no to check for actions
            if ignore_action == "no":
                #If user plays a card that causes the opponent to miss turn they play again but only if ignore action == no
                while (played_card in skip_cards or played_card in reverse_cards or played_card in draw_two_cards or played_card in wild_draw_four) and ignore_action == "no" and len(user_hand) > 0:

                    #If user plays skip card, skip message is printed
                    if played_card in skip_cards:
                        print ("Computer was skipped! It's user's turn again!", "\n")

                    #If user plays reverse card reverse message is printed
                    if played_card in reverse_cards:
                        print ("Play was reversed! It's user's turn again!", "\n")

                    #If user plays draw two card computer draws two cards       
                    if played_card in draw_two_cards:
                        print ("User played a draw two card! Computer must draw two cards and is skipped! It's user's turn again!", "\n")
                        for i in range (0,2):
                            card_num = random.randint(0,len(deck)-1)
                            comp_hand.append(deck[card_num])
                            deck.remove(deck[card_num])

                    #If user plays wild draw four card computer draws four cards and user chooses color
                    if played_card in wild_draw_four:
                        print ("User played a wild draw four card! Computer must draw four cards and user must choose a color! It's user's turn again!")
                        for i in range (0,4):
                            card_num = random.randint(0,len(deck)-1)
                            comp_hand.append(deck[card_num])
                            deck.remove(deck[card_num])
                        print ("User played a wild pick color card! User must choose a color!")
                        color = input("Choose a color: ")
                        color = color.lower()
                        while not(color == "red") and not(color == "blue") and not(color == "yellow") and not(color == "green"):
                            print ("Invalid color entered. Please try again")
                            color = input("Choose a color: ")
                            color = color.lower()
                        played_card = color

                        print ("\n")

                    #Computer is skipped and user gets turn again
                    played_card, ignore_action = user_turn (deck, user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

                #If user plays wild pick color card they must choose the color
                if played_card in wild_pick_color:
                    print ("User played a wild pick color card! User must choose a color!")
                    color = input("Choose a color: ")
                    color = color.lower()
                    while not(color == "red") and not(color == "blue") and not(color == "yellow") and not(color == "green"):
                        print ("Invalid color entered. Please try again")
                        color = input("Choose a color: ")
                        color = color.lower()
                    played_card = color

                    print ("\n")


                    
            #Call computer turn function
            played_card, ignore_action = comp_turn (deck, comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)



            #Checking to see if computer played an action or wild card
            #If they did then perform the actions of those cards

            #Ignore action must be no
            if ignore_action == "no":
                #If comp plays a card that causes the opponent to miss turn they play again but only if ignored action == no
                while (played_card in skip_cards or played_card in reverse_cards or played_card in draw_two_cards or played_card in wild_draw_four) and ignore_action == "no" and len(comp_hand) > 0:

                    #If comp plays skip card, skip message is printed
                    if played_card in skip_cards:
                        print ("User was skipped! It's computer's turn again!", "\n")

                    #If comp plays reverse card reverse message is printed
                    if played_card in reverse_cards:
                        print ("Play was reversed! It's computer's turn again!", "\n")

                    #If comp plays draw two card user draws two cards       
                    if played_card in draw_two_cards:
                        print ("Computer played a draw two card! User must draw two cards and is skipped! It's computer's turn again!", "\n")
                        for i in range (0,2):
                            card_num = random.randint(0,len(deck)-1)
                            user_hand.append(deck[card_num])
                            print ("You drew", deck[card_num])
                            deck.remove(deck[card_num])

                    #If comp plays wild draw four card user draws four cards and comp chooses color
                    if played_card in wild_draw_four:
                        print ("Computer played a wild draw four card! User must draw four cards and computer must choose a color! It's user's turn again!")
                        for i in range (0,4):
                            card_num = random.randint(0,len(deck)-1)
                            user_hand.append(deck[card_num])
                            print ("You drew", deck[card_num])
                            deck.remove(deck[card_num])
                            
                        x = random.randint(0,3)
                            
                        if x == 0:
                            played_card = "red"
                        if x == 1:
                            played_card = "blue"
                        if x == 2:
                            played_card = "yellow"
                        if x == 3:
                            played_card = "green"
                            
                        print ("Computer chooses", played_card + "!")
                        print ("\n")
                               
                    #User is skipped and comp gets turn again
                    played_card, ignore_action = comp_turn (deck, comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)


                #If comp plays wild pick color card they must choose the color
                if played_card in wild_pick_color:
                    print ("Computer played a wild pick color card! Computer must choose a color!")

                    x = random.randint(0,3)
                               
                    if x == 0:
                        played_card = "red"
                    if x == 1:
                        played_card = "blue"
                    if x == 2:
                        played_card = "yellow"
                    if x == 3:
                        played_card = "green"
                               
                    print ("Computer chooses", played_card + "!")
                    print ("\n")


        #Display winner messages
        if len(user_hand) == 0:
            print ("\n")
            print ("USER WON!!!")
        elif len(comp_hand) == 0:
            print ("\n")
            print ("COMPUTER WON!!!")
            print ("\n")

        #Ask if user would like to play again
        play_again = input("Would you like to play again?(y or no): ")
        print ("\n")
        


#deal_cards function
#function takes the hand to add the dealt cards to and the deck as argument
#function deals card to the player
#Returns players dealt hand
def deal_cards (deck, hand):
    #For loop to repeat 7 times
    for x in range (0,7):
        #randomly chooses card index from 0 to length of deck
        card_num = random.randint(0, len(deck)-1)
        #adds that card to the player's hand
        hand.append(deck[card_num])
        #removes card from deck
        deck.remove(deck[card_num])
        
    return (hand)








#function begin_game
#function takes cards remaining in deck as argument
#Function randomly flips one of the cards in the deck to start the game and displays which card was flipped then takes out of deck
#Function return the flipped card
def begin_game (deck):
    #randomly chooses an index value from the length of the remaining deck
    chosen_num = random.randint(0,len(deck)-1)
    #print which card was flipped
    print ('The card', '"' + deck[chosen_num] + '"', 'was flipped.')
    print ("User starts.", "\n")
    #assign the card to the variable played_card
    played_card = deck[chosen_num]
    #delete card from the deck
    deck.remove(deck[chosen_num])
    
    return played_card








#def user_turn function
#function takes the deck, user's current hand, last played card, as well as card colors and types
#function simulates the user's turn
#returns the played card
def user_turn (deck, user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four):

    #print user's hand
    print ("User's current hand contains:", user_hand, "\n")

    #Check if player has UNO
    if len(user_hand) == 1:
        print ("User has UNO!!!!", "\n")

    #Call can_play function to check if user has any playable cards
    can_play = player_can_play(user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

    #Set ignore_action as no for default which tells main not to ignore the action of an action card if it is played (ex: skip or wild draw 4)
    ignore_action = "no"
    
    #If user has any cards that can be played ask for user to choose card
    if can_play == "yes":

        
        print ('Choose which card you want to play (please input in form "color number", ex: red 1). If not able to play a card you must draw from the deck.')
 
        #Create card_playable variable to determine if the user inputted card is actually playable and set to no
        card_can_be_played = "no"
        
        #While loop to keep asking for card until given card is playable 
        while card_can_be_played == "no":
            
            #User inputs which card they want to play
            user_play = input("Which card would you like to play? ")

            #Call card_can_be_played function to determine if card can be played
            card_can_be_played = is_card_playable (user_play, user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

            #If card can't be played ask for the user to choose another card
            if card_can_be_played == "no":
                print ("Inputted card is not playable. Please choose another card.")

        print ("\n")
        #Make sure card is in lowercase
        user_play = user_play.lower()
        
        #Display message that user played the card
        print ("You played", user_play + ".", "\n")
        
        #Remove played card from user's hand
        user_hand.remove(user_play)
            
        #Assign the card to the variable containing the last played card
        played_card = user_play


    else:
        #If user can't play any cards print message
        print ("User doesn't have any playable cards. User must draw one card from deck.", "\n")

        #Randomly give user card from deck and remove card form deck
        card_num = random.randint(0,len(deck)-1)
        user_play = deck[card_num]
        user_hand.append(user_play)
        deck.remove(user_play)



        #Display card that was drawn
        print('You drew', '"' + user_play + '"')

        print ("Checking to see if card can be played...", "\n")
        
        

        #Check if that card is playable
        card_can_be_played = is_card_playable (user_play, user_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

        #If card can be played
        if card_can_be_played == "yes":
            print ("You're in luck, the card you that you drew can be played!")
            
            #Display message that user played the card
            print ("You played", user_play + ".", "\n")
        
            #Remove played card from user's hand
            user_hand.remove(user_play)
                
            #Assign the card to the variable containing the last played card
            played_card = user_play


        else:
            #Drawn card can't be played so it stays in user's hand and the last played card remains the same
            print ("The card you drew can't be played.")
            print ("\n")
            #Change ignore_action to yes so that main will ignore the action of the card so that there is no infinite loop of skips if last card was a skip or action card
            ignore_action = "yes"
            


    return (played_card, ignore_action)








#def is_card_playable
#function takes the chosen card, the player's hand, last played card, and card colors and types as argument
#Function determines if that card is playable and in players hand
#Function returns either variable "card_can_be_played" which says either "no" or "yes"
def is_card_playable (card, player_hand, last_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four):

    #Makes sure input is in lowercase
    card = card.lower()


    #Check if card is in user's hand
    if card in player_hand:
        in_hand = "yes"

        #Set card_playable variable to no, if it is playable then the variable will be changed
        card_playable = "no"
                
        #Check if card is wildcard
        if card in wild_pick_color:
            card_playable = "yes"
        if card in wild_draw_four:
            card_playable = "yes"
                
                
        #Check if chosen card is playable by color
        if card in red_cards and last_card in red_cards:
            card_playable = "yes"
        if card in blue_cards and last_card in blue_cards:
            card_playable = "yes"
        if card in yellow_cards and last_card in yellow_cards:
            card_playable = "yes"
        if card in green_cards and last_card in green_cards:
            card_playable = "yes"

        #Check if card is playable by type or number
        if card in zero_cards and last_card in zero_cards:
            card_playable = "yes"
        if card in one_cards and last_card in one_cards:
            card_playable = "yes"
        if card in two_cards and last_card in two_cards:
            card_playable = "yes"
        if card in three_cards and last_card in three_cards:
            card_playable = "yes"
        if card in four_cards and last_card in four_cards:
            card_playable = "yes"
        if card in five_cards and last_card in five_cards:
            card_playable = "yes"
        if card in six_cards and last_card in six_cards:
            card_playable = "yes"
        if card in seven_cards and last_card in seven_cards:
            card_playable = "yes"
        if card in eight_cards and last_card in eight_cards:
            card_playable = "yes"
        if card in nine_cards and last_card in nine_cards:
                card_playable = "yes"
        if card in draw_two_cards and last_card in draw_two_cards:
                card_playable = "yes"
        if card in reverse_cards and last_card in reverse_cards:
                card_playable = "yes"
        if card in skip_cards and last_card in skip_cards:
                card_playable = "yes"

        #If card is in user's hand and playable card_can_be_played = yes
        if card_playable == "yes":
            card_can_be_played = "yes"
        else:
            #If card is in user's hand but can't be played
            card_can_be_played = "no"
                        

    else:
        #If card is not in user's hand
        card_can_be_played = "no"
    

    return card_can_be_played








#def player_can_play function
#function takes players hand, the last played card, and card types and colors as arguments
#function determines if any of the players cards can be played
#returns variable can_play which says "yes" or "no"
def player_can_play (player_hand, last_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four):

    #Set card_playable variable to no, if it is playable then the variable will be changed
    card_playable = "no"
    
    #Check if player can be play by itterating through their hand
    for card in player_hand:
        
        #Check if card is wildcard
            if card in wild_pick_color:
                card_playable = "yes"
            if card in wild_draw_four:
                card_playable = "yes"
                    
                    
            #Check if chosen card is playable by color
            if card in red_cards and last_card in red_cards:
                card_playable = "yes"
            if card in blue_cards and last_card in blue_cards:
                card_playable = "yes"
            if card in yellow_cards and last_card in yellow_cards:
                card_playable = "yes"
            if card in green_cards and last_card in green_cards:
                card_playable = "yes"

            #Check if card is playable by type or number
            if card in zero_cards and last_card in zero_cards:
                card_playable = "yes"
            if card in one_cards and last_card in one_cards:
                card_playable = "yes"
            if card in two_cards and last_card in two_cards:
                card_playable = "yes"
            if card in three_cards and last_card in three_cards:
                card_playable = "yes"
            if card in four_cards and last_card in four_cards:
                card_playable = "yes"
            if card in five_cards and last_card in five_cards:
                card_playable = "yes"
            if card in six_cards and last_card in six_cards:
                card_playable = "yes"
            if card in seven_cards and last_card in seven_cards:
                card_playable = "yes"
            if card in eight_cards and last_card in eight_cards:
                card_playable = "yes"
            if card in nine_cards and last_card in nine_cards:
                    card_playable = "yes"
            if card in draw_two_cards and last_card in draw_two_cards:
                    card_playable = "yes"
            if card in reverse_cards and last_card in reverse_cards:
                    card_playable = "yes"
            if card in skip_cards and last_card in skip_cards:
                    card_playable = "yes"

            #If any of their cards are playable then can_play = yes
            if card_playable == "yes":
                can_play = "yes"
            else:
                #If not can play is no
                can_play = "no"

        
    return (can_play)




#def comp_turn function
#function takes computer's hand, the last played card, and the deck and card colors and types as arguments
#function simulates computers turn
#function returns the computer's played card
def comp_turn (deck, comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four):

    #Check if player has UNO
    if len(comp_hand) == 1:
        print ("Computer has UNO!!!!", "\n")
        
    #Call can_play function to check if user has any playable cards
    can_play = player_can_play(comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

    #Set ignore action to no as default so that main doesn't ingore action of card played for the first time
    ignore_action = "no"
    
    #If computer has playable cards continue
    if can_play == "yes":

        
        #Initialize i as accumulator variable
        i = 0

        #Set card_can_be_played variable to no
        card_can_be_played = "no"
        
        #While loop to itterate through the computers hand looking for a card to play
        #Loop continues until either no cards left in hand or a card is found that can be played
        while i < len(comp_hand) and card_can_be_played == "no":
            #Assign card with given index to variable comp_play
            comp_play = comp_hand[i]
            #Call card_can_be_played function to determine if card can be played
            card_can_be_played = is_card_playable (comp_play, comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)
            #Add to accumulator variable
            i = i+1

            
        #If there is a card that can be played play it and remove it from the computer's hand
        if card_can_be_played == "yes":

            #Display message that cpmputer played the card
            print ("Computer played", comp_play + ".", "\n")
        
            #Remove played card from user's hand
            comp_hand.remove(comp_play)
            
            #Assign the card to the variable containing the last played card
            played_card = comp_play

    else:
        #If comp can't play any cards print message
        print ("Computer doesn't have any playable cards. Computer must draw one card from deck.", "\n")

        #Randomly give user card from deck and remove card form deck
        card_num = random.randint(0,len(deck)-1)
        comp_play = deck[card_num]
        comp_hand.append(comp_play)
        deck.remove(comp_play)


        #Display card that was drawn
        print ("Computer drew a card.")
        print ("Checking to see if card can be played...")
        
        

        #Check if that card is playable
        card_can_be_played = is_card_playable (comp_play, comp_hand, played_card, red_cards, blue_cards, yellow_cards, green_cards, zero_cards, one_cards, two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards, draw_two_cards, skip_cards, reverse_cards, wild_pick_color, wild_draw_four)

        if card_can_be_played == "yes":

            
            #Display message that user played the card
            print ("Computer can play the card that they drew!")
            print ("Computer played", comp_play + ".", "\n")
        
            #Remove played card from user's hand
            comp_hand.remove(comp_play)
                
            #Assign the card to the variable containing the last played card
            played_card = comp_play


        else:
            #Card is not playable so the computer must keep the card that they drew
            print ("Computer cannot play the card that they drew.", "\n")
            #Set ignore action to yes so that main ignores the action of a card coming through for the second time
            ignore_action = "yes"

            


        
            

            
    return (played_card, ignore_action)


main ()
        
    



