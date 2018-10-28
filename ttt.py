# -*- coding: utf-8 -*-
"""
Created on Fri March  9 16:27:49 2018

@author: Ankit Singh
"""

from tkinter import *
import time
import random

class ticTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.mainTitleText = StringVar()
        self.mainTitleText.set('Welcome!')
        self.mainTitle = Label(self.window, text = self.mainTitleText.get())
        self.mainTitle.grid(row = 0, column = 1)

        # Some Variables
        self.newStartGameText = StringVar()
        self.whoseTurnText = StringVar()
        self.scoreText = 0
        self.xIcon = PhotoImage(file = 'x.gif') #width = 145, height = 155
        self.oIcon = PhotoImage(file = 'o.gif')
        self.default = PhotoImage(file = 'default.gif')

        #Buttons For Tic Tac Toe, Disabled Initially
        self.grid1 = Button(self.window, state = DISABLED, command = self.grid1Pressed)
        self.grid1.grid(row=1, column = 0)
        self.grid1.config(image = self.default, width = '145', height = '155')
        #self.grid1.bind('<Button-1>', self.grid1Pressed)
        
        self.grid2 = Button(self.window, state = DISABLED, command = self.grid2Pressed)
        self.grid2.grid(row=1, column = 1)
        self.grid2.config(image = self.default, width = '145', height = '155')
        #self.grid2.bind('<Button-1>', self.grid2Pressed)
        
        self.grid3 = Button(self.window, state = DISABLED, command = self.grid3Pressed)
        self.grid3.grid(row=1, column = 2) 
        self.grid3.config(image = self.default, width = '145', height = '155')
        #self.grid3.bind('<Button-1>', self.grid3Pressed)
        
        self.grid4 = Button(self.window, state = DISABLED, command = self.grid4Pressed)
        self.grid4.grid(row=2, column = 0)
        self.grid4.config(image = self.default, width = '145', height = '155')        
        #self.grid4.bind('<Button-1>', self.grid4Pressed)

        self.grid5 = Button(self.window, state = DISABLED, command = self.grid5Pressed)
        self.grid5.grid(row=2, column = 1)
        self.grid5.config(image = self.default, width = '145', height = '155')        
        #self.grid5.bind('<Button-1>', self.grid5Pressed)

        self.grid6 = Button(self.window, state = DISABLED, command = self.grid6Pressed)
        self.grid6.grid(row=2, column = 2)
        self.grid6.config(image = self.default, width = '145', height = '155')       
        #self.grid6.bind('<Button-1>', self.grid6Pressed)

        self.grid7 = Button(self.window, state = DISABLED, command = self.grid7Pressed)
        self.grid7.grid(row=3, column = 0)
        self.grid7.config(image = self.default, width = '145', height = '155')        
        #self.grid7.bind('<Button-1>', self.grid7Pressed)

        self.grid8 = Button(self.window, state = DISABLED, command = self.grid8Pressed)
        self.grid8.grid(row=3, column = 1)
        self.grid8.config(image = self.default, width = '145', height = '155')       
        #self.grid8.bind('<Button-1>', self.grid8Pressed)

        self.grid9 = Button(self.window, state = DISABLED, command = self.grid9Pressed)        
        self.grid9.grid(row=3, column = 2)
        self.grid9.config(image = self.default, width = '145', height = '155')
        #self.grid9.bind('<Button-1>', self.grid9Pressed)

        self.gridButtons = [self.grid1, self.grid2, self.grid3, self.grid4, self.grid5, self.grid6, self.grid7, self.grid8, self.grid9]

        #New Game Button
        self.newStartGameText.set('Start Game')
        self.newStartGame = Button(self.window, text = self.newStartGameText.get())
        self.newStartGame.grid(row = 4, column = 1)
        self.newStartGame.bind('<Button-1>', self.startGame)
        
        #Whose Turn Is It Label
        self.whoseTurnText.set('TBD')
        self.whoseTurn = Label(self.window, text = self.whoseTurnText.get())
        self.whoseTurn.grid(row = 4, column = 0)
        
        #Score Label
        self.score = Label(self.window, text = 'Score: {}'.format(self.scoreText))
        self.score.grid(row = 4, column = 2)

        #Game in Progress Variable
        self.gameInProgress = False

        #Who's first?
        self.first = IntVar()
        self.first.set(9) #arbitrary number for testing
            
        
        self.window.mainloop()

    def startGame(self, event):
        firstPlayer = self.firstPlayer()
        self.FIRST = firstPlayer

        if self.gameInProgress:
            self.mainTitleText.set('Starting New Game')
            self.mainTitle.config(text = self.mainTitleText.get())
            for grid in self.gridButtons:
                grid.config(text = '')

        else:
            self.mainTitleText.set('Starting Game')
            self.mainTitle.config(text = self.mainTitleText.get())            
            self.gameInProgress = True
            for grid in self.gridButtons:
                grid.config(state = NORMAL, text = '')

                
        self.first.set(firstPlayer)
        print('The first player is: {}'.format(self.first.get()))
        self.resetButtonState()
        if self.FIRST == 0:
            self.AIFirstMove()
        return firstPlayer

    def firstPlayer(self):
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            return 0 #0 means the computer will go first
        else:
            return 1 #1 means the player will go first

    def userWinConfig(self):
        if self.first.get() == 1:
            if 'x' in self.grid1.config('text'):
                if 'x' in self.grid2.config('text'):
                    if 'x' in self.grid3.config('text'):
                        return True
                if 'x' in self.grid4.config('text'):
                    if 'x' in self.grid7.config('text'):
                        return True
                if 'x' in self.grid5.config('text'):
                    if 'x' in self.grid9.config('text'):
                        return True
            if 'x' in self.grid3.config('text'):
                if 'x' in self.grid6.config('text'):
                    if 'x' in self.grid9.config('text'):
                        return True
                if 'x' in self.grid5.config('text'):
                    if 'x' in self.grid7.config('text'):
                        return True
            if 'x' in self.grid7.config('text'):
                if 'x' in self.grid8.config('text'):
                    if 'x' in self.grid9.config('text'):
                        return True
            if 'x' in self.grid2.config('text'):
                if 'x' in self.grid5.config('text'):
                    if 'x' in self.grid8.config('text'):
                        return True
            if 'x' in self.grid4.config('text'):
                if 'x' in self.grid5.config('text'):
                    if 'x' in self.grid6.config('text'):
                        return True

        elif self.first.get() == 0:
            if 'o' in self.grid1.config('text'):
                if 'o' in self.grid2.config('text'):
                    if 'o' in self.grid3.config('text'):
                        return True
                if 'o' in self.grid4.config('text'):
                    if 'o' in self.grid7.config('text'):
                        return True
                if 'o' in self.grid5.config('text'):
                    if 'o' in self.grid9.config('text'):
                        return True
            if 'o' in self.grid3.config('text'):
                if 'o' in self.grid6.config('text'):
                    if 'o' in self.grid9.config('text'):
                        return True
                if 'o' in self.grid5.config('text'):
                    if 'o' in self.grid7.config('text'):
                        return True
            if 'o' in self.grid7.config('text'):
                if 'o' in self.grid8.config('text'):
                    if 'o' in self.grid9.config('text'):
                        return True
            if 'o' in self.grid2.config('text'):
                if 'o' in self.grid5.config('text'):
                    if 'o' in self.grid8.config('text'):
                        return True
            if 'o' in self.grid4.config('text'):
                if 'o' in self.grid5.config('text'):
                    if 'o' in self.grid6.config('text'):
                        return True
        return False


    def userWin(self):
        for grid in self.gridButtons:
            grid.config(text = '', state = DISABLED)
            grid.update()
        self.scoreText += 1
        self.score.config(text = 'Score: {}'.format(self.scoreText))
        

    def grid1Pressed(self):
        if self.first.get() == 1:
            self.grid1.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid1.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
            print(self.grid1.config('state'))
        else:
            self.window.after(1000, self.AI)
        
    def grid2Pressed(self):
        if self.first.get() == 1:
            self.grid2.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid2.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid3Pressed(self):
        if self.first.get() == 1:
            self.grid3.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid3.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid4Pressed(self):
        if self.first.get() == 1:
            self.grid4.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid4.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid5Pressed(self):
        if self.first.get() == 1:
            self.grid5.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid5.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid6Pressed(self):
        if self.first.get() == 1:
            self.grid6.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid6.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid7Pressed(self):
        if self.first.get() == 1:
            self.grid7.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid7.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid8Pressed(self):
        if self.first.get() == 1:
            self.grid8.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid8.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')

        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
        else:
            self.window.after(1000, self.AI)
        
    def grid9Pressed(self):
        if self.first.get() == 1:
            self.grid9.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
        elif self.first.get() == 0: 
            self.grid9.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
            
        checkIfWin = self.userWinConfig()
        if checkIfWin:
            print('You won!')
            self.userWin()
            print(self.grid9.config('text'))
        else:
            self.window.after(1000, self.AI)       
            

    def resetButtonState(self):
        for button in self.gridButtons:
            button.config(state = NORMAL, image = self.default, text = '')

    def AI(self):
        if self.FIRST == 1:
            randomMove = random.randint(1,4)

            #OFFENSIVE MOVES
            if 'o' in self.grid1.config('text'):

                #1-2-3
                if 'o' in self.grid2.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        if 'x' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True
                if 'o' in self.grid3.config('text'):
                    if 'o' not in self.grid2.config('text'):
                        if 'x' not in self.grid2.config('text'):
                            self.grid2PressedAI()
                            return True
                #1-4-7
                if 'o' in self.grid4.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        if 'x' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True
                if 'o' in self.grid7.config('text'):
                    if 'o' not in self.grid4.config('text'):
                        if 'x' not in self.grid4.config('text'):
                            self.grid4PressedAI()
                            return True
                #1-5-9
                if 'o' in self.grid5.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        if 'x' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True
                if 'o' in self.grid9.config('text'):
                    if 'o' not in self.grid5.config('text'):
                        if 'x' not in self.grid5.config('text'):
                            self.grid5PressedAI()
                            return True

            if 'o' in self.grid3.config('text'):

                #3-2-1
                if 'o' in self.grid2.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        if 'x' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True

                #3-6-9

                if 'o' in self.grid6.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        if 'x' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True
                if 'o' in self.grid9.config('text'):
                    if 'o' not in self.grid6.config('text'):
                        if 'x' not in self.grid6.config('text'):
                            self.grid6PressedAI()
                            return True

                #3-5-7

                if 'o' in self.grid5.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        if 'x' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True
                if 'o' in self.grid7.config('text'):
                    if 'o' not in self.grid5.config('text'):
                        if 'x' not in self.grid5.config('text'):
                            self.grid5PressedAI()
                            return True
                        
            if 'o' in self.grid7.config('text'):
                #7-4-1
                if 'o' in self.grid4.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        if 'x' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True

                #7-8-9
                if 'o' in self.grid8.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        if 'x' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True

                if 'o' in self.grid9.config('text'):
                    if 'o' not in self.grid8.config('text'):
                        if 'x' not in self.grid8.config('text'):
                            self.grid8PressedAI()
                            return True

                #7-5-3
                if 'o' in self.grid5.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        if 'x' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True
                        
            if 'o' in self.grid9.config('text'):

                #9-6-3
                if 'o' in self.grid6.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        if 'x' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True

                #9-8-7
                if 'o' in self.grid8.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        if 'x' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True

                #9-5-1
                if 'o' in self.grid5.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        if 'x' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True
                
                
                
                


            #DEFENSIVE MOVES
            if 'x' in self.grid1.config('text'):
                if 'x' in self.grid2.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'x' in self.grid4.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                    
            if 'x' in self.grid3.config('text'):
                if 'x' in self.grid2.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'x' in self.grid6.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
            if 'x' in self.grid7.config('text'):
                if 'x' in self.grid4.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'x' in self.grid8.config('text'):                        #THIS IS WHERE THE COMPUTER LOST IN ONE CASE. WHY MOTHERFUCKER WHY
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            if 'x' in self.grid9.config('text'):
                if 'x' in self.grid6.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'x' in self.grid8.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True


            if 'x' in self.grid5.config('text'):
                if 'x' in self.grid1.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
                if 'x' in self.grid3.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                if 'x' in self.grid7.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'x' in self.grid9.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'x' in self.grid2.config('text'):
                    if 'o' not in self.grid8.config('text'):
                        self.grid8PressedAI()
                        return True
                if 'x' in self.grid8.config('text'):
                    if 'o' not in self.grid2.config('text'):
                        self.grid2PressedAI()
                        return True
                if 'x' in self.grid4.config('text'):
                    if 'o' not in self.grid6.config('text'):
                        self.grid6PressedAI()
                        return True
                if 'x' in self.grid6.config('text'):
                    if 'o' not in self.grid4.config('text'):
                        self.grid4PressedAI()
                        return True

            if 'x' in self.grid5.config('text'):
                if 'o' not in self.grid1.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        if 'o' not in self.grid7.config('text'):
                            if 'o' not in self.grid9.config('text'):
                                cornerMove = random.randint(1,4)
                                if cornerMove == 1:
                                    self.grid1PressedAI()
                                    return True
                                elif cornerMove == 2:
                                    self.grid3PressedAI()
                                    return True
                                elif cornerMove == 3:
                                    self.grid7PressedAI()
                                    return True
                                elif cornerMove == 4:
                                    self.grid9PressedAI()
                                    return True


            #RANDOM MOVE
                                
            if randomMove == 1:
                if 'x' not in self.grid1.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'x' not in self.grid3.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'x' not in self.grid7.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'x' not in self.grid9.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 2:
                if 'x' not in self.grid3.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'x' not in self.grid1.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'x' not in self.grid7.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'x' not in self.grid9.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 3:
                if 'x' not in self.grid7.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'x' not in self.grid3.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'x' not in self.grid1.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'x' not in self.grid9.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 4:
                if 'x' not in self.grid9.config('text'):
                    if 'o' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
                elif 'x' not in self.grid3.config('text'):
                    if 'o' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'x' not in self.grid7.config('text'):
                    if 'o' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'x' not in self.grid1.config('text'):
                    if 'o' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True

            #DEFAULT MOVES IF NO GOOD ONES ARE AVAILABLE
            if 'x' not in self.grid1.config('text'):
                if 'o' not in self.grid1.config('text'):
                    self.grid1PressedAI()
                    return True

            if 'x' not in self.grid2.config('text'):
                if 'o' not in self.grid2.config('text'):
                    self.grid2PressedAI()
                    return True

            if 'x' not in self.grid3.config('text'):
                if 'o' not in self.grid3.config('text'):
                    self.grid3PressedAI()
                    return True            

            if 'x' not in self.grid4.config('text'):
                if 'o' not in self.grid4.config('text'):
                    self.grid4PressedAI()
                    return True

            if 'x' not in self.grid5.config('text'):
                if 'o' not in self.grid5.config('text'):
                    self.grid5PressedAI()
                    return True

            if 'x' not in self.grid6.config('text'):
                if 'o' not in self.grid6.config('text'):
                    self.grid6PressedAI()
                    return True

            if 'x' not in self.grid7.config('text'):
                if 'o' not in self.grid7.config('text'):
                    self.grid7PressedAI()
                    return True

            if 'x' not in self.grid8.config('text'):
                if 'o' not in self.grid8.config('text'):
                    self.grid8PressedAI()
                    return True

            if 'x' not in self.grid9.config('text'):
                if 'o' not in self.grid9.config('text'):
                    self.grid9PressedAI()
                    return True
            
                                

        elif self.FIRST == 0:
            randomMove = random.randint(1,4)

            #OFFENSIVE MOVES
            if 'x' in self.grid1.config('text'):

                #1-2-3
                if 'x' in self.grid2.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        if 'o' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True
                if 'x' in self.grid3.config('text'):
                    if 'x' not in self.grid2.config('text'):
                        if 'o' not in self.grid2.config('text'):
                            self.grid2PressedAI()
                            return True
                #1-4-7
                if 'x' in self.grid4.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        if 'o' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True
                if 'x' in self.grid7.config('text'):
                    if 'x' not in self.grid4.config('text'):
                        if 'o' not in self.grid4.config('text'):
                            self.grid4PressedAI()
                            return True
                #1-5-9
                if 'x' in self.grid5.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        if 'o' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True
                if 'x' in self.grid9.config('text'):
                    if 'x' not in self.grid5.config('text'):
                        if 'o' not in self.grid5.config('text'):
                            self.grid5PressedAI()
                            return True

            if 'x' in self.grid3.config('text'):

                #3-2-1
                if 'x' in self.grid2.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        if 'o' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True

                #3-6-9

                if 'x' in self.grid6.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        if 'o' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True
                if 'x' in self.grid9.config('text'):
                    if 'x' not in self.grid6.config('text'):
                        if 'o' not in self.grid6.config('text'):
                            self.grid6PressedAI()
                            return True

                #3-5-7

                if 'x' in self.grid5.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        if 'o' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True
                if 'x' in self.grid7.config('text'):
                    if 'x' not in self.grid5.config('text'):
                        if 'o' not in self.grid5.config('text'):
                            self.grid5PressedAI()
                            return True
                        
            if 'x' in self.grid7.config('text'):
                #7-4-1
                if 'x' in self.grid4.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        if 'o' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True

                #7-8-9
                if 'x' in self.grid8.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        if 'o' not in self.grid9.config('text'):
                            self.grid9PressedAI()
                            return True

                if 'x' in self.grid9.config('text'):
                    if 'x' not in self.grid8.config('text'):
                        if 'o' not in self.grid8.config('text'):
                            self.grid8PressedAI()
                            return True

                #7-5-3
                if 'x' in self.grid5.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        if 'o' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True
                        
            if 'x' in self.grid9.config('text'):

                #9-6-3
                if 'x' in self.grid6.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        if 'o' not in self.grid3.config('text'):
                            self.grid3PressedAI()
                            return True

                #9-8-7
                if 'x' in self.grid8.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        if 'o' not in self.grid7.config('text'):
                            self.grid7PressedAI()
                            return True

                #9-5-1
                if 'x' in self.grid5.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        if 'o' not in self.grid1.config('text'):
                            self.grid1PressedAI()
                            return True
                
                
                
                


            #DEFENSIVE MOVES
            if 'o' in self.grid1.config('text'):
                if 'o' in self.grid2.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'o' in self.grid4.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                    
            if 'o' in self.grid3.config('text'):
                if 'o' in self.grid2.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'o' in self.grid6.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
            if 'o' in self.grid7.config('text'):
                if 'o' in self.grid4.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'o' in self.grid8.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            if 'o' in self.grid9.config('text'):
                if 'o' in self.grid6.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'o' in self.grid8.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True


            if 'o' in self.grid5.config('text'):
                if 'o' in self.grid1.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
                if 'o' in self.grid3.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                if 'o' in self.grid7.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                if 'o' in self.grid9.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                if 'o' in self.grid2.config('text'):
                    if 'x' not in self.grid8.config('text'):
                        self.grid8PressedAI()
                        return True
                if 'o' in self.grid8.config('text'):
                    if 'x' not in self.grid2.config('text'):
                        self.grid2PressedAI()
                        return True
                if 'o' in self.grid4.config('text'):
                    if 'x' not in self.grid6.config('text'):
                        self.grid6PressedAI()
                        return True
                if 'o' in self.grid6.config('text'):
                    if 'x' not in self.grid4.config('text'):
                        self.grid4PressedAI()
                        return True

            if 'o' in self.grid5.config('text'):
                if 'x' not in self.grid1.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        if 'o' not in self.grid7.config('text'):
                            if 'x' not in self.grid9.config('text'):
                                cornerMove = random.randint(1,4)
                                if cornerMove == 1:
                                    self.grid1PressedAI()
                                    return True
                                elif cornerMove == 2:
                                    self.grid3PressedAI()
                                    return True
                                elif cornerMove == 3:
                                    self.grid7PressedAI()
                                    return True
                                elif cornerMove == 4:
                                    self.grid9PressedAI()
                                    return True


            #RANDOM MOVE
                                
            if randomMove == 1:
                if 'o' not in self.grid1.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'o' not in self.grid3.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'o' not in self.grid7.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'o' not in self.grid9.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 2:
                if 'o' not in self.grid3.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'o' not in self.grid1.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'o' not in self.grid7.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'o' not in self.grid9.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 3:
                if 'o' not in self.grid7.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'o' not in self.grid3.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'o' not in self.grid1.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True
                elif 'o' not in self.grid9.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True

            elif randomMove == 4:
                if 'o' not in self.grid9.config('text'):
                    if 'x' not in self.grid9.config('text'):
                        self.grid9PressedAI()
                        return True
                elif 'o' not in self.grid3.config('text'):
                    if 'x' not in self.grid3.config('text'):
                        self.grid3PressedAI()
                        return True
                elif 'o' not in self.grid7.config('text'):
                    if 'x' not in self.grid7.config('text'):
                        self.grid7PressedAI()
                        return True
                elif 'o' not in self.grid1.config('text'):
                    if 'x' not in self.grid1.config('text'):
                        self.grid1PressedAI()
                        return True

            #DEFAULT MOVES IF NO GOOD ONES ARE AVAILABLE
            if 'x' not in self.grid1.config('text'):
                if 'o' not in self.grid1.config('text'):
                    self.grid1PressedAI()
                    return True

            if 'x' not in self.grid2.config('text'):
                if 'o' not in self.grid2.config('text'):
                    self.grid2PressedAI()
                    return True

            if 'x' not in self.grid3.config('text'):
                if 'o' not in self.grid3.config('text'):
                    self.grid3PressedAI()
                    return True            

            if 'x' not in self.grid4.config('text'):
                if 'o' not in self.grid4.config('text'):
                    self.grid4PressedAI()
                    return True

            if 'x' not in self.grid5.config('text'):
                if 'o' not in self.grid5.config('text'):
                    self.grid5PressedAI()
                    return True

            if 'x' not in self.grid6.config('text'):
                if 'o' not in self.grid6.config('text'):
                    self.grid6PressedAI()
                    return True

            if 'x' not in self.grid7.config('text'):
                if 'o' not in self.grid7.config('text'):
                    self.grid7PressedAI()
                    return True

            if 'x' not in self.grid8.config('text'):
                if 'o' not in self.grid8.config('text'):
                    self.grid8PressedAI()
                    return True

            if 'x' not in self.grid9.config('text'):
                if 'o' not in self.grid9.config('text'):
                    self.grid9PressedAI()
                    return True
       

    def AIFirstMove(self):
        #If AI is the first player, this happens
        checkIfBlankBoard = []
        for grid in self.gridButtons:
            if 'x' not in grid.config('text'):
                if 'o' not in grid.config('text'):
                    checkIfBlankBoard.append(True)
                else:
                    checkIfBlankBoard.append(False)
            else:
                checkIfBlankBoard.append(False)
        if all(checkIfBlankBoard) == True:
            firstMove = random.randint(1,5)
            if firstMove == 1:
                self.grid1PressedAI()
            elif firstMove == 2:
                self.grid3PressedAI()
            elif firstMove == 3:
                self.grid7PressedAI()
            elif firstMove == 4:
                self.grid9PressedAI()
            elif firstMove == 5:
                self.grid5PressedAI()

    

    def grid1PressedAI(self):
        if self.FIRST == 1:
            self.grid1.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid1.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
            self.grid1.update()
        
    def grid2PressedAI(self):
        if self.FIRST == 1:
            self.grid2.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid2.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')

        
    def grid3PressedAI(self):
        if self.FIRST == 1:
            self.grid3.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid3.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
            self.grid3.update()

        
    def grid4PressedAI(self):
        if self.FIRST == 1:
            self.grid4.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid4.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')

        
    def grid5PressedAI(self):
        if self.FIRST == 1:
            self.grid5.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid5.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')

        
    def grid6PressedAI(self):
        if self.FIRST == 1:
            self.grid6.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid6.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')

        
    def grid7PressedAI(self):
        if self.FIRST == 1:
            self.grid7.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid7.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
            self.grid7.update()

        
    def grid8PressedAI(self):
        if self.FIRST == 1:
            self.grid8.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid8.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')

        
    def grid9PressedAI(self):
        if self.FIRST == 1:
            self.grid9.config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')
        elif self.FIRST == 0: 
            self.grid9.config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
            self.grid9.update()



def check(x):
    startTime = time.time()
    for k in range(x):
        pass
    endTime = time.time()
    timeTaken = endTime - startTime
    return 'Found in {} seconds.'.format(timeTaken)


'''
    def AI(self):
        validMove = False
        counter = 0
        while validMove == False:
            move = random.randint(0,8)
            if self.first.get() == 0:
                if 'x' not in self.gridButtons[move].config('text'):
                    if 'o' not in self.gridButtons[move].config('text'):
                        print(move)
                        validMove = True
                        self.gridButtons[move].config(state = DISABLED, image = self.xIcon, width = '145', height = '155', text = 'x')
            elif self.first.get() == 1:
                if 'x' not in self.gridButtons[move].config('text'):
                    if 'o' not in self.gridButtons[move].config('text'):
                        print(move)
                        validMove = True
                        self.gridButtons[move].config(state = DISABLED, image = self.oIcon, width = '145', height = '155', text = 'o')         

'''
   
    
        
ticTacToe()