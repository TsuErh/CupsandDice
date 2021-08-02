#!/usr/bin/env python
# coding: utf-8

# # Cups and Dice

# ### Tsu Erh Lin
# ##### Feb 08 2021

# ## Part 1

# In[1]:


import random


# In[2]:


class SixSidedDice:
    'A class that represents a six sides dice'
    
    def __init__(self):
        'Initialize the number of the dice as 1'
        self.r = 1                        # Set the initial number as 1
        
    def roll(self):
        'Return the number of the facevalue'
        self.r = random.randrange(1, 7)   # Give a random number from 1 to 7
        return self.r                     # Return the facevalue
    
    def getFaceValue(self):
        'Return the result after rolling a dice'
        return self.r
    
    def __repr__(self):
        'Return canonical string representation SixSidedDice'
        return "SixSidedDice({})".format(self.r)


# In[3]:


class TenSidedDice(SixSidedDice):
    'A class represent a ten sides dice'
        
    def roll(self):
        'Override the number after rolling the dice'
        self.r = random.randrange(1, 11)   # Give a random number from 1 to 10
        return self.r                      # Return the facevalue
    def __repr__(self):
        'Return canonical string representation TenSidedDice()'
        return "TenSidedDice({})".format(self.r)


# In[4]:


class TwentySidedDice(SixSidedDice):
    'A class represent a twenty sides dice'
        
    def roll(self):
        'Override the number after rolling the dice'
        self.r = random.randrange(1, 21)   # Give a random number from 1 to 20
        return self.r                      # Return the facevalue
    
    def __repr__(self):
        'Return canonical string representation TwentySidedDice()'
        return "TwentySidedDice({})".format(self.r)


# In[5]:


class Cup:
    'A class represent several dices in a cup'
    
    def __init__(self, sixsided = 1, tensided = 1, twentysided = 1):   # Set the initial value, the cup contain each type of die
        'Initialized the cup with each type of dice'
        self.sixdie = sixsided      # Assign the input number of six sided dies to self.sixdie
        self.tendie = tensided      # Assign the input number of ten sided dies to self.tendie
        self.twedie = twentysided   # Assign the input number of twenty sided dies to self.twentysided
        
    def roll(self):
        'Roll the dices in the cup'
        self.sum = 0                               # Assign zero at first to the sum
        self.ttl = []                              # Give an empty list for each face value and type of dies in the cup
    
        r = 0                                      # Give r as 0
        while r < self.sixdie:                     # When r is smaller than the input six die number the loop should keep running
            self.six = SixSidedDice()              # Assign the six sided die to self.six
            self.sixrolls = self.six.roll()        # Assign the face value after rolled the die to self.sixrolls
            self.sum += self.sixrolls              # Add the face value to the sum each time after roll
            self.ttl.append(self.six)              # Append self.six to the ttl list
            r += 1                                 # r plus 1 in each loop
            
        r = 0                                      # Give r as 0
        while r < self.tendie:                     # When r is smaller than the input ten die number the loop should keep running
            self.ten = TenSidedDice()              # Assign the ten sided die to self.ten
            self.tenrolls = self.ten.roll()        # Assign the face value after rolled the die to self.tenrolls
            self.sum += self.tenrolls              # Add the face value to the sum each time after roll
            self.ttl.append(self.ten)              # Append self.ten to the ttl list
            r += 1                                 # r plus in each loop
            
        r = 0                                      # Give r as 0
        while r < self.twedie:                     # When r is smaller than the input twenty die number the loop should keep running
            self.twe = TwentySidedDice()           # Assign the twenty sided die to self.twenty
            self.twerolls = self.twe.roll()        # Assign the face value after rolled the die to self.twerolls
            self.sum += self.twerolls              # Add the face value to the sum each time after roll
            self.ttl.append(self.twe)              # Append self.twe to the ttl list
            r += 1                                 # r plus in each loop
                
    def getSum(self):
        'Return the sum'
        return self.sum
    
    def __repr__(self):
        'Return canonical string representation Cup()'
        return "Card({})".format(self.ttl)


# ## Part 2

# In[6]:


def CupDieGame():
    'Main Function, return the result of cups and dies game'
    
    name = Greet()    # First use Greet function to greet and get the username
    balance = 100     # Assign 100 to user's balance
    while Play():     # While the Play() return True, means user want to play the game, the loop will go on
        goal = Goal()   # Show the user the goal of each game and return goal
        bet = Bet(balance)                                          # Assign bet from the value returned from Bet()
        sixnum, tennum, twennum = DieNum()                          # Return sixnum, tennum, twennum from DieNum()
        roll_sum = CupGame(sixnum, tennum, twennum)                 # Give the value of sixnum, tennum, and twennum to CupGame() and return sum of the facevalue
        balance = MatchGoal(bet, balance, roll_sum, goal)           # Assign new balance after a game
        print("{}, your balance now is {}!".format(name, balance))  # Report the result to user


# In[7]:


def Greet():
    'Greet and return user name.'
    
    print('Hello! Welcome to Cups and Dies Game!\n')   # Greet the user
    name = input('Please enter your name: ')           # Ask the user for their name
    return name                                        # Return name


# In[8]:


def Play():
    'Return True or False the user is going to join the game'
    
    play = input('Do you want to play the game?(y/n) ')   # Ask the user if they want to play the game
    if play == "y":                                       # If the answer is "y", Play function will return True
        return True
    elif play == "n":                                     # If the answer is "n", Play function will return False
        return False
    return "Valid Answer! Should be y or n!"              # If the answer is neither "y" or "n", print a warning


# In[9]:


def Goal():
    'Return the goal number of the game'
    
    goal = random.randrange(1, 101)      # Set the goal by using random number from 1 to 100
    print("The Goal Number: {}".format(goal))
    return goal


# In[10]:


def Bet(balance):
    'Return how much the user is going to bet for a game'
    
    bet = eval(input('How much would you like to bet? '))   # Ask the user how much they are going to bet
    while (bet < 1 or bet > balance):                       # If the bet is not reasonable, print a notification
        print("The bet should larger than 1 and less than your balance: {}!".format(balance))
        bet = eval(input('How much would you like to bet? '))   # Ask the user to re-enter the bet
    return bet                                                  # If the bet is reasonable, then return bet


# In[11]:


def DieNum():
    'Return the number of each die the user is going to put into the cup'
    
    sixnum = eval(input("How many of SIX sided die do you want to roll? "))       # Ask for the number of six sided die
    tennum = eval(input("How many of TEN sided die do you want to roll? "))       # Ask for the number of ten sided die
    twennum = eval(input("How many of TWENTY sided die do you want to roll? "))   # Ask for the number of twenty sided die
    return sixnum, tennum, twennum


# In[12]:


def CupGame(sixnum, tennum, twennum):
    'Return the sum of the facevalue in the cup'
    
    # Use the class cup for the game
    cup = Cup(sixnum, tennum, twennum)   # Use the sixnum, tennum, twennum requested from user in DieNum()
    roll_sum = cup.roll()                # Roll the dice and return the sum of the facevalue in the cup
    return roll_sum


# In[13]:


def MatchGoal(bet, balance, roll_sum, goal):
    'Return the updated value in each game'
    
    balance -= bet                                          # Deduct the bet value from the balance
    if goal == roll_sum:                                    # Condition1: if the roll equals to the goal
        balance += (bet * 10)                               # The user will get 10 times of the bet back
    elif (roll_sum == goal + 3 or roll_sum == goal - 3):    # Condition2: if the roll is within 3 of the goal
        balance += (bet * 5)                                # The user will get 5 times of the bet back
    elif (roll_sum == goal + 10 or roll_sum == goal - 10):  # Condition3: if the roll is within 10 of the goal
        balance += (bet * 2)                                # The user will get 2 times of the bet back
    return balance


# In[14]:


CupDieGame()


# In[ ]:




