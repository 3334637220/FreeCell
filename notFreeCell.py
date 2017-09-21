from deck import Deck

if __name__ == '__main__':
    # init the deck
    deck = Deck(1, 13, 4)
    deck.print()
    while 1:
        cmd = input('Enter m to move, q to quit:\t')
        if cmd == 'm':
            if deck.move():
                deck.print()
                if deck.victory():
                    print('Victory!')
                    exit(0)
        elif cmd == 'q':
            exit(0)
        else:
            print('<Error>: please input m or q!')
            continue
