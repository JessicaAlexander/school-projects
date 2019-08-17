import cards, games     

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """

    def num_cards(self) :
        return len(self.cards)

    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if len(self.cards) >= (per_hand * len(hands)):
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Reshuffling deck.")
                    self.cards = []
                    self.populate()
                    self.shuffle()
                    top_card = self.cards[0]
                    self.give(top_card, hand)  
    
class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        
        t = 0
        for card in self.cards:
              t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """

    def __init__ (self, name, bankroll=1000) :
        super(BJ_Player, self). __init__ (name)
        self.bankroll = bankroll
        self.bet = 0
        
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def ante(self) :
        self.bankroll = self.bankroll - 100

    def is_bankrupt(self):
        return self.bankroll < 1

    def place_bet(self) :
        print (self.name + ", you currentlyhave a bankroll of " + str(self.bankroll))
        self.bet = games.ask_number("How much would you like to bet? ", low = 1, high = self.bankroll +1)
        
    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
           self.bankroll -= self.bet
           print(self.name + ", you lose " + str(self.bet)," and you currently have a bankroll of " + str(self.bankroll))
           if self.bankroll < 1:
               print(self.name, "leaves the game!")

    def win(self):
           self.bankroll += self.bet
           print(self.name + ", you win " + str(self.bet)," and you currently have a bankroll of " + str(self.bankroll))

    def push(self):
        print(self.name, "pushes.")
        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def has_player(self) :
        return len(self.players) > 0

    @property
    def get_still_playing(self):
        remaining = []
        for player in self.players:
            if not player.is_busted():
                remaining.append(player)
        return remaining
    still_playing = (get_still_playing)

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        if self.deck.num_cards() <  7 * len(self.players) :
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()        

        for player in self.players:
            print(player.place_bet())
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()

        for player in self.players:
            print(player)
            print(self.dealer)        

        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()        

        if not self.still_playing:
            print(self.dealer)           

        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)            

            if self.dealer.is_busted():                

                for player in self.still_playing:
                    player.win()                    
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()                       
                    elif player.total < self.dealer.total:
                        player.lose()                        
                    else:
                        player.push()                        
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")
    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()        
    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")

main()
input("\n\nPress the enter key to exit.")



