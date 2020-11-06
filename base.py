import random
from time import sleep

play_again = True


def newcard():
    global used
    cardnum = 54
    while cardnum in used:
        cardnum = random.randint(1, 53)
    if cardnum not in used:
        used.append(cardnum)
    return cardnum


def hit_or_hold():
    add_a_card = str
    try:
        add_a_card = input('\nWould you like to hit or hold?:  ').lower()
        if add_a_card not in {'hit', 'hold'}:
            hit_hold_error = f'Oops! You said {add_a_card}.\nWe were looking for hit or hold (not case-sensitive)'
            raise Exception(hit_hold_error)
    except Exception as hit_hold_error:
        print(hit_hold_error)
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
    used = [54]
    replay = str
    hidden = True
    call = str

    def blackjack_check(hand):
        blackjack = False
        for n in range(0, 1):
            if hand[n] == 'A' and hand[n + 1] in [10, 'J', 'Q', 'K']:
                blackjack = True
            else:
                blackjack = False
        return blackjack


    for i in range(4):
        deck[i*13+0:i*13+12] = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    dealer_hand = [deck[newcard()], deck[newcard()]]
    player_hand = [deck[newcard()], deck[newcard()]]

    show_hands(dealer_hand, player_hand, hidden)

    while call != 'hold' and hand_sum(player_hand) <= 21:
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
            dealer_hand.append(deck[newcard()])
            show_hands(dealer_hand, player_hand, hidden)
        print(f'\nDealer\'s hand total is {hand_sum(dealer_hand)}')
        print(f'Your hand total is {hand_sum(player_hand)}')
        sleep(1)
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

    try:
        replay = input('\nplay again? y/n: ')
        if 'y' not in replay and 'n' not in replay:
            replay_error = f'Oops, you said {replay}, we were looking for any word with either y or n'
            raise Exception(replay_error)
        if 'y' in replay and 'n' in replay:
            replay_error = f'Oops, you included both a y and n in your response. Just use one'
            raise Exception(replay_error)
    except Exception as replay_error:
        print(replay_error)

    if 'y' in replay:
        print('Okay! shuffling the cards...\n')
    elif 'n' in replay:
        print('Okay! Thanks for playing\n')
        play_again = False
