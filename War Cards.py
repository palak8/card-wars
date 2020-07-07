#!/usr/bin/env python
# coding: utf-8

# In[26]:


import random


# In[27]:


suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,
        'King':13,'Ace':14}


# In[28]:


class Cards:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit


# In[29]:


class Deck:
  
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                create_card=Cards(suit,rank)
                
                self.all_cards.append(create_card)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
       
    def remove_one(self):
        
        return self.all_cards.pop()


# In[30]:


class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards = []
        
    def remove_one(self):
        
        return self.all_cards.pop()
    
    def add_card(self,new_card):
        
        if type(new_card)==type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)
            
    def __str__(self):
        
        return f'Player {self.name} has {len(self.all_cards) } cards. '


# In[31]:


player1=Player("One")
player2=Player("Two")

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_card(new_deck.remove_one())
    player2.add_card(new_deck.remove_one())
    


# In[32]:


start=True

round_num=0

while start:
    
    round_num += 1
    print(f"Round {round_num}")
    
    if len((player1.all_cards))==0:
        print("Player Two Wins!!")
        start=False
        break
    if len((player2.all_cards))==0:
        print("Player One Wins!!")
        start=False
        break
    
    ones_cards= []
    ones_cards.append(player1.all_cards.pop())
    
    
    
    twos_cards= []
    twos_cards.append(player2.all_cards.pop())
    
    print('P1 (' + str(len(player1.all_cards)) + ') ' + ones_cards[-1].rank +
          ' <-> ' + 
          twos_cards[-1].rank + '('+ str(len(player2.all_cards)) + ') P2')
    war=True
    
    while war:
        
        if (ones_cards[-1].value) > (twos_cards[-1].value) :
            
            player1.add_card(ones_cards)
            player1.add_card(twos_cards)
            
            war=False
        
        elif (ones_cards[-1].value) < (twos_cards[-1].value) :
            
            player2.add_card(ones_cards)
            player2.add_card(twos_cards)
            
            war=False
        
        else:
            
            print("!!WAR!!")
            
            if len(player1.all_cards) < 3:
                print("Player 1 is unable to declare war.")
                print("Player 2 wins.")
                start=False
                break
                
            elif len(player2.all_cards) < 3:
                print("Player 2 is unable to declare war.")
                print("Player 1 wins.")
                start=False
                break
                
            else:
                
                for x in range(3):
                    ones_cards.append(player1.remove_one())
                    twos_cards.append(player2.remove_one())
                    print('P1 (' + str(len(player1.all_cards)) + ') ' + ones_cards[-1].rank +' <-> ' +  twos_cards[-1].rank + '('+ str(len(player2.all_cards)) + ') P2')
                               

