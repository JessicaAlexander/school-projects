from tkinter import *
import random

class Application(Frame) :
        def __init__(self, master) :
            super(Application, self).__init__(master)
            self.wins = 0
            self.losses = 0
            self.tries = 0
            self.number = 0
            self.selectRange = False
            self.grid()
            self.create_widgets()
        
        def create_widgets(self):
            self.StartLabel = Label(self, text = "Welcome To My GUI Guessing Game! \nPlease selecte one of the Ranges below. \nThen you may start guessing! \nYou only have 10 tries.\n\n")
            self.StartLabel.grid(row = 0, column = 0, columnspan = 3)
            self.StartLabel.configure(background ="cyan")

            Label(self, text = "Ranges").grid(row = 2, column = 0, sticky = W)

            self.choice = StringVar()
            self.choice.set(None)

            self.rbtn1 = Radiobutton(self, text = "1 - 100", variable = self.choice, value = "1", command = self.UpdateChoice)
            self.rbtn1.grid(row = 3, column = 0, sticky = W)

            self.rbtn2 = Radiobutton(self, text = "1 - 1,000", variable = self.choice, value = "2", command = self.UpdateChoice)
            self.rbtn2.grid(row = 4, column = 0, sticky = W)

            self.rbtn3 = Radiobutton(self, text = "1 - 10,000", variable = self.choice, value = "3", command = self.UpdateChoice)
            self.rbtn3.grid(row = 5, column = 0, sticky = W)

            self.startBtn = Button(self, text = "Start", command = self.Start)
            self.startBtn.grid(row = 4, column = 1, sticky = W)
            self.startBtn.configure(state = DISABLED)
            self.startBtn.configure(background ="blue")
            self.startBtn.configure(foreground ="white")

            Label(self, text = "Enter Guess Here!").grid(row = 5, column = 1, sticky = W)

            self.GuessTxt = Entry(self)
            self.GuessTxt.grid(row = 6, column = 1, sticky = W)

            self.SubmitBtn = Button(self, text = "Submit", command = self.CalcGuess)
            self.SubmitBtn.grid(row = 6, column = 2, sticky = E)
            self.SubmitBtn.configure(state = DISABLED)
            self.SubmitBtn.configure(background ="green")
            self.SubmitBtn.configure(foreground ="white")

            self.TriesLbl = Label(self, text = "Tries:     ")
            self.TriesLbl.grid(row = 7, column = 1, sticky = E)

            self.AnswerLbl = Label(self, text = "Ready to Play!", height = 4)
            self.AnswerLbl.grid(row = 9, column = 0, columnspan = 4)

            Label(self, text = "Wins").grid(row = 15, column = 0, sticky = W)
            self.WinsLbl = Label(self, text = "0")
            self.WinsLbl.grid(row = 15, column = 1, sticky = W)
        
            Label(self, text = "Losses").grid(row = 16, column = 0, sticky = W)
            self.LossesLbl = Label(self, text = "0")
            self.LossesLbl.grid(row = 16, column = 1, sticky = W)
        
            self.PlayBtn = Button(self, text = "Play Again!", command = self.Play)
            self.PlayBtn.grid(row = 15, column = 2, sticky = E)
            self.PlayBtn.configure(state = DISABLED)
            self.PlayBtn.configure(background ="red")
            self.PlayBtn.configure(foreground ="white")
        
            self.ExitBtn = Button(self, text = "Exit!", command = self.Exit)
            self.PlayBtn.grid(row = 16, column = 2, sticky = E)
            self.PlayBtn.configure(state = DISABLED)
            self.PlayBtn.configure(background ="blue")
            self.PlayBtn.configure(foreground ="white")

        def UpdateChoice(self):
            if self.choice.get() == "1":
                self.number =random.randint(1, 100)
            elif self.choice.get() == "2":
                self.number =random.randint(1, 1000)
            else:
                self.number =random.randint(1, 10000)
            self.startBtn.configure(state = NORMAL)
        
        def Start(self):
            self.rbtn1.configure(state = DISABLED)
            self.rbtn2.configure(state = DISABLED)
            self.rbtn3.configure(state = DISABLED)
            self.startBtn.configure(state = DISABLED)
            self.GuessTxt.focus()
            self.SubmitBtn.configure(state = NORMAL)
        
        def CalcGuess(self):
            if self.GuessTxt.get() == "":
                self.AnswerLbl.configure(text = "You must enter a  number before \nclicking Submit!")
            elif int(self.GuessTxt.get()) == self.number:
                self.tries += 1
                self.AnswerLbl.configure(text = "Your guess was correct! You win!!")
                self.wins += 1
                self.WinsLbl.configure(text = self.wins)
                self.PlayBtn.configure(state = NORMAL)
                self.SubmitBtn.configure(state = DISABLED)
            elif int(self.GuessTxt.get ()) > self.number:
                self.tries += 1
                self.AnswerLbl.configure(text = "Your guess was to high!")
                self.GuessTxt.select_range(0, END)
            else:
                self.tries += 1
                self.AnswerLbl.configure(text = "Your guess was to low!")
                self.GuessTxt.select_range(0, END)
                
            self.TriesLbl.configure(text = "Tries:  " + str(self.tries))
            
            if self.tries >= 10:
                self.AnswerLbl.configure(text = "I'm sorry you lose! The correct answer was " + str(self.number))
                self.losses += 1
                self.LossesLbl.configure(text = self.losses)
                self.PlayBtn.configure(state = NORMAL)
                self.SubmitBtn.configure(state = DISABLED)
            
        def Play(self):
            self.rbtn1.configure(state =NORMAL)
            self.rbtn2.configure(state =NORMAL)
            self.rbtn3.configure(state =NORMAL)
            self.choice.set(NONE)
            self.startBtn.configure(state = DISABLED)
            self.SubmitBtn.configure(state = DISABLED)
            self.PlayBtn.configure(state = DISABLED)
            self.GuessTxt.delete(0, END)
            self.AnswerLbl.configure(text = "")
            self.tries = 0
            self.TriesLbl.configure(text = "Tries:  " + str(self.tries)) 

        def Exit(self):
            root.destroy()
                
root = Tk()
root.title("GUI Guessing Game!")
root.geometry("395x400")
app = Application(root)
root.mainloop()

