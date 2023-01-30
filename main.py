import art
import random
cards_dict = {
    "ace": 11,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack":10,
    "queen":10,
    "king":10
}

def card_logo(key):
    """This function return the card logo."""
    if key == "ace":
        return art.ace
    elif key == "two":
        return art.two
    elif key == "three":
        return art.three
    elif key == "four":
        return art.four
    elif key == "five":
        return art.five
    elif key == "six":
        return art.six
    elif key == "seven":
        return art.seven
    elif key == "eight":
        return art.eight
    elif key == "nine":
        return art.nine
    elif key == "ten":
        return art.ten
    elif key == "jack":
        return art.jack
    elif key == "king":
        return art.king
    elif key == "queen":
        return art.queen
    else:
        return art.hidden

def show_dealer_card2():
    #show dealer card 2 now
    for key, value in cards_dict.items():
    # Check if the value matches the dealer card2 value
        if value == dealer_card2:
        # If the value matches, print the key
            print(f"Dealer's hidden card: {value}\n")
            print(card_logo(key))
            break
count = 0
def random_card():
    """This function randomly choose a card from card dictionary.Send the key of the dictionary to card_logo to print the logo. It returns card value."""
    global count
    #counting how many times this function is being called so that we can apply condition for the dealer_card2.
    count += 1
    #random_card_pair is a tuple.
    random_card_pair = random.choice(list(cards_dict.items()))
    #separate key and value from the tuple.
    key,value = random_card_pair
    #As second card of the dealer cannot be seen, therefore printing a hidden card logo.
    if count == 4:
        print(card_logo("hidden"))
    else:
        print(card_logo(key))
    return value


        
            
def hit(hand):
    """This function randomly choose another card then return the total sum of the card."""
    next_card = random_card() 
    hand1 = hand + next_card
    #check ace value if >21 the 1 or 11
    if hand1 > 21 and next_card == 11:
        next_card = 1
        hand1 = hand + next_card
    print(f"{hand} + {next_card} = {hand1}")
    return hand1

def check_winner(dealer_hand,user_hand):
    """This function checks who wins,lose or draw"""
    if dealer_hand < 22:
        if dealer_hand > user_hand:
            print("Oppss!! You lose and the dealer win!")
        elif dealer_hand == user_hand:
            print("Draw!")
        else: print("Congoo!! You win!")
    elif dealer_hand == user_hand:
        print("It's a draw!")
    else: print("Congoo!! You win!")

def dealer_turn(dealer_hand,user_hand):
    """This function checks if dealer_hand>21 if yes then user win or if deler_hand < 17 then there will be auto hit."""
    if dealer_hand < 17:
        final_hand = hit(dealer_hand)
        print(f"Dealer's final hand is: {final_hand}\n")
        dealer_turn(final_hand,user_hand)
    elif dealer_hand == 21:
        print("Dealer has BLACKJACK! Sorry, you lose!")
    else: check_winner(dealer_hand,user_hand)     

def user_turn(user_hand):
    """This function check if user_hand>21 if yes then game is over, if no then user can choose hit or stand"""

    if user_hand > 21:
        print("Oppss! You lose!")
    elif user_hand < 21:
        if input("Do you want to 'Hit' or 'Stand'?\n").lower() == "hit":
            final_hand = hit(user_hand)
            user_turn(final_hand)
        else: 
            print(f"Your final hand is: {user_hand}. Let's see the dealer's card.")
            show_dealer_card2()
            print(f"{dealer_card1} + {dealer_card2} = {dealer_hand}")
            dealer_turn(dealer_hand,user_hand)
    else: 
        print("BLACKJACK")
        show_dealer_card2()
        dealer_turn(dealer_hand,user_hand)
    
start = True
while start:
    print(art.logo)
    #State your betting amount. If you win, you get the amount otherwise you loose.
    set_bet_amount = True
    while set_bet_amount:
        bet = input("Enter betting amount: \n")
        if input("Type 'yes' if it's a deal or 'no' if you want to change your betting amount:\n").lower() == "yes":
            set_bet_amount = False
    print(f"You are playing for {bet} taka")
    start = input("Type 'deal' to start the game: \n").lower()
    
    if start == "deal":
        print("Your cards:\n")
        user_card1 = random_card()
        user_card2 = random_card()
        print("dealer cards:")
        dealer_card1 = random_card()
        dealer_card2 = random_card()
        user_hand = user_card1+user_card2
        dealer_hand = dealer_card1 + dealer_card2
        

        
        #start        
        #check ace value. if it's greater than 21 then ace = 1 else 11
        
        print(f"{user_card1} + {user_card2} = {user_hand}")
        user_turn(user_hand)
        if input("Type 'yes' if you want to play the game again or 'no' if you want to finish the game.\n").lower() == "yes":
            print("\033c")
            start = True
        else: 
            start = False
            print("\033c")
            print("Thank you for playing with me! I hope you earned some money!")
    
    
    
    