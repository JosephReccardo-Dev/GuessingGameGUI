"""
Program: numberGuessGUI.py
Author: Joseph Reccardo 7/13/2023

A simple GUI version of the number guessing game written in standard python language. The game keeps track of attempts and displays the guess counter for each iteration of play.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame

# Other imports go here
import random 

# Class Header
class GuessingGame(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		#Call to Easy Frame constructor method
		EasyFrame.__init__(self, title = "Guessing Game", width = 260, height = 180)

		#Initialize the instance variables for the data
		self.magicNumber = random.randint(1, 100)
		self.count = 0

		#Create and add widgets to the window
		self.hintLabel = self.addLabel(text = "Guess a Number Between 1 and 100", row = 0, column = 0, sticky = "NSEW", columnspan = 2)
		self.addLabel(text = "Your guess: ", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)

		#Adding buttons
		self.nextButton = self.addButton(text = "Guess", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame)
	
	#Definition of the nextGuess() function
	def nextGuess(self):
		self.count += 1
		guess = self.guessField.getNumber()
		#Logic that determines the game's outcome
		if guess == self.magicNumber:
			self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempts!"
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry, too small!"
		else:
			self.hintLabel["text"] = "Sorry, too large!"

	#Definition of the newGame() function
	def newGame(self):
		"""Resets the data and GUI to their origional states"""
		self.magicNumber = random.randint(1,100)
		self.count = 0
		self.hintLabel["text"] = "Guess a number between 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"

# Global definition of the main() method
def main():
	GuessingGame().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()