#!/usr/bin/env python

import glob
import os
import pygame
import Tkinter, tkFileDialog


root = Tkinter.Tk()
dirname = tkFileDialog.askdirectory(parent=root,initialdir="~",title='Please select a directory')
root.destroy()

print (dirname)


pygame.init()


vocabulary_words = glob.glob( dirname + "/*.wav")
score = 0
count = 0

for vocabulary_word in vocabulary_words:
	count += 1
	spell_word = os.path.splitext(os.path.basename(vocabulary_word))[0]
	pygame.mixer.Sound(vocabulary_word).play()
	users_input_word = raw_input('Enter the correct spelling: ')
	if users_input_word == spell_word:
		print ('Correct')
		score += 1
	else:
		print ('Incorrect')
		print (spell_word)
print ('Your score is ' + str(score))

grade = float(score)/float(count) * 100

print ('Your grade is ' + str(grade))


