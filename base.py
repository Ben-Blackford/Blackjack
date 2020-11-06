import random
from time import sleep

play_again = True


def blackjack_check(hand):
    blackjack = False
    for n in range(0, 1):
        if hand[n] == 'A' and hand[n + 1] in [10, 'J', 'Q', 'K']:
            blackjack = True
        else:
            blackjack = False
    return blackjack


def newcard():
    global used
    cardnum = 52
    while cardnum in used:
        cardnum = random.randint(0, 51)
    if cardnum not in used:
        used.append(cardnum)
    return cardnum


def hit_or_hold():
    while True:
        try:
            add_a_card = input('\nWould you like to hit or hold?:  ').lower()
            if add_a_card not in {'hit', 'hold'}:
                sleep(0.5)
                hit_hold_error = f'\nOops! You said {add_a_card}.\nWe were looking for hit or hold (not case-sensitive)'
                raise Exception(hit_hold_error)
        except Exception as hit_hold_error:
            print(hit_hold_error)
            sleep(2)
        else:
            break
    return add_a_card


def show_hands(d_hand, p_hand, hide):
    dealer_display = d_hand[:]
    player_display = p_hand[:]
    if hide:
        dealer_display[0] = '?'
    sleep(0.5)
    print(f'\nDealer Hand: {dealer_display}')
    sleep(0.5)
    print(f'Player Hand: {player_display}')
    sleep(0.5)


def hand_sum(hand):
    hand_total = 0
    ace_count = 0
    for n in range(0, len(hand)):
        if hand[n] == 'A':
            ace_count = ace_count + 1
            hand_total = hand_total + 11
        elif isinstance(hand[n], str):
            hand_total = hand_total + 10
        else:
            hand_total = hand_total + hand[n]
        if hand_total > 21 and ace_count > 0:
            hand_total = hand_total - 10
            ace_count = ace_count - 1
    return hand_total


while play_again:
    deck = []
    used = [52]
    replay = str
    hidden = True
    call = str

    for i in range(4):
        deck[i*13+0:i*13+12] = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    dealer_hand = [deck[newcard()], deck[newcard()]]
    player_hand = [deck[newcard()], deck[newcard()]]
    show_hands(dealer_hand, player_hand, hidden)

    while call != 'hold' and hand_sum(player_hand) <= 21:
        sleep(1)
        call = hit_or_hold()
        if call == 'hit':
            player_hand.append(deck[newcard()])
            show_hands(dealer_hand, player_hand, hidden)
    hidden = False

    sleep(1)
    if hand_sum(player_hand) > 21:
        print('\nTough Luck! You Busted')
    else:
        print('\ndealer\'s turn')
        show_hands(dealer_hand, player_hand, hidden)
        while hand_sum(dealer_hand) < 17:
            sleep(2)
            print('\nDealer Hits')
            sleep(0.5)
            dealer_hand.append(deck[newcard()])
            show_hands(dealer_hand, player_hand, hidden)
        sleep(1)
        print(f'\nDealer\'s hand total is {hand_sum(dealer_hand)}')
        print(f'Your hand total is {hand_sum(player_hand)}\n')
        sleep(2)
        if hand_sum(dealer_hand) > 21:
            print('Congratulations! Dealer Busts, You Win!')
        elif blackjack_check(player_hand) and not blackjack_check(dealer_hand):
            print('Congratulation! Blackjack, You Win!')
        elif blackjack_check(dealer_hand) and not blackjack_check(player_hand):
            print('Tough Luck, Dealer Wins with Blackjack')
        elif hand_sum(player_hand) > hand_sum(dealer_hand):
            print('Congratulations! You Win')
        elif hand_sum(player_hand) < hand_sum(dealer_hand):
            print('Tough Luck, Dealer Wins')
        else:
            print('Wow! A Tie!')

    while True:
        try:
            sleep(0.5)
            replay = input('\nplay again? y/n: ')
            sleep(0.5)
            if 'y' not in replay and 'n' not in replay:
                replay_error = f'\nOops, you said {replay}, we were looking for any word with either y or n'
                raise Exception(replay_error)
            elif 'y' in replay and 'n' in replay:
                replay_error = f'\nOops, you included both a y and n in your response. Please just use one'
                raise Exception(replay_error)
        except Exception as replay_error:
            print(replay_error)
        else:
            break

    sleep(0.5)
    if 'y' in replay:
        print('\nOkay! shuffling the cards...\n')
    elif 'n' in replay:
        print('\nOkay! Thanks for playing\n')
        play_again = False
    sleep(0.5)

print('Contact Me!\nblackfordbenjamin@gmail.com\nblackfordengineering.ca')
