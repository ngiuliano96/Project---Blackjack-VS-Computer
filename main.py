############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The following list is the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the computer.

import random
from art import logo

def blackjack():
    # Greet player
    print(logo)
    print("Welcome to Blackjack, get ready to play!")

    # Define starting card deck (infinite)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Divider (for UI)
    divider = "-" * 72
    
    # Define functions
    # Function to generate a new card
    def deal_card():
        card = random.choice(cards)
        return card

    # Function to calculate scores
    def calc_score(hand_of_cards):
        score = 0
        for card in hand_of_cards:
            if card == 11 and score + 11 > 21:
                score += 1
            elif score + card == 21 and len(hand_of_cards) == 2:
                return 0
            else:
               score += card
        return score

    # Function to display score messages
    def display_score(hand_of_cards, score, status, is_player):
        if is_player:
            print(f"Your {'final hand:' if status == 'end' else 'cards:'} {hand_of_cards}, {'final' if status == 'end' else 'current'} score: {score}")
        else:
            print(f"Computer's {f'first card: {computer_hand[0]}' if status != 'end' else f'final hand: {computer_hand}, final score: {computer_score}'}")  
        
    # Generate starting hands and scores
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    player_score = calc_score(player_hand)
    computer_score = calc_score(computer_hand)
    
    # Display starting hands
    display_score(player_hand, player_score, 'cont', True)
    display_score(computer_hand, computer_score, 'cont', False)

    # Initialize card drawing loop
    drawing_cards = True
    while drawing_cards:
        print(divider)
        
        draw_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_again == "y" and player_score <= 21 and player_score != 0 and computer_score != 0:
            # Draw card and add to player hand
            player_hand.append(deal_card())
            player_score = calc_score(player_hand)
            
            # Display scores             
            display_score(player_hand, player_score, 'cont', True)
            display_score(computer_hand, computer_score, 'cont', False)
             
            print(divider)
            
        else:
            # Draw cards for computer until score > 17
            while computer_score != 0 and computer_score < 17:
                computer_hand.append(deal_card())
                computer_score = calc_score(computer_hand)
                
            display_score(player_hand, player_score, 'end', True)
            display_score(computer_hand, computer_score, 'end', False)

            print(divider)
            
            # Determine if the player wins
            if player_score == computer_score:
                print("Draw.")
            elif computer_score == 0:
                print("Dealer got a Blackjack! You lose.")
            elif player_score == 0:
                print("You got a Blackjack! You win.")
            elif player_score > 21:
                print("You went over 21! You lose.")
            elif computer_score > 21:
                print("Computer went over 21! You win.")
            elif player_score > computer_score:
                print("You win!")
            else:
                print("You lose.")

            print(divider)
            
            drawing_cards = False
    
    # Check if the player wants to play again
    play_again = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()

    print(divider)

    if play_again == "y":
        blackjack()
    else:
        print("OK then, see you later!")
        

blackjack()
