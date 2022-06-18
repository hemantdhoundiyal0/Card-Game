import random
from operator import itemgetter


class Deck:
    suits=['S','H','D','C']
    
    #initializing the deck of cards
    def __init__(self):
        self.deck=[]
        for suit in self.suits:
            for num in range(1,14):
                self.deck.append((suit,num))


class Players(Deck):
    def __init__(self,num_players):
        super().__init__()
        self.num_players=num_players
        self.players_name=[]
        self.player_score_dict={}
        for i in range(1,self.num_players+1):
            self.players_name.append("player"+str(i))
            self.player_score_dict["player"+str(i)]=0


class Game(Players):
    def pickTwoCards(self):
        self.cards=random.sample(self.deck,2)
        self.deck=list(set(self.deck)-set(self.cards))
        
    def rounds(self):
        i=1
        while len(self.deck)>=2*(self.num_players):
            print("Round",i)
            self.allPlayerCardPicks()
            self.roundWinner()
            i+=1
            
        else:
            pass

    def allPlayerCardPicks(self):
        self.greaterCardEachPlayer=[]
        for player in self.players_name:
            self.pickTwoCards()
            print(f'Two cards picked by {player} : ',self.cards)
            for item in self.greaterCard(self.cards):
                self.greaterCardEachPlayer.append(item)
        print('Cards shown by each player : ',self.greaterCardEachPlayer)
        self.round_greatest_card=self.greaterCard(self.greaterCardEachPlayer)
        if len(self.round_greatest_card)==1:
            self.round_greatest_card=self.round_greatest_card[0]
        print("Round's greatest card : ",self.round_greatest_card)
        return self.round_greatest_card

    def greaterCard(self,card_list):
        self.card_list=card_list
        max_num=(max(self.card_list,key=itemgetter(1))[1]) # check greatest number
        self.fillter_cards =   [item for item in self.card_list if max_num == item[1]]
        if len(self.fillter_cards) > 1:
            max_letter=max(self.fillter_cards,key=itemgetter(0))[0] # if numbers same check greatest letter
            self.fillter_cards=[item for item in self.fillter_cards if max_letter == item[0]]
        return self.fillter_cards

    def roundWinner(self):
        index = (self.greaterCardEachPlayer).index(self.round_greatest_card)
        self.player_score_dict[self.players_name[index]]=self.player_score_dict[self.players_name[index]]+1
        print(self.player_score_dict)
    
    def winner(self):
        self.rounds()
        self.roundWinner()
        print('Number of cards remaining : ',len(self.deck))
        print("Final winner is : ",max(self.player_score_dict,key=self.player_score_dict.get))
        print('Game Over !!!') 


obj=Game(4)
obj.winner()









