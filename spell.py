import pygame

pygame.init()
pygame.mixer.Sound('/home/owner/Music/spell/voracious.wav').play()
vocabulary_word = 'voracious'
score = 0
spell_word = raw_input('Enter the correct spelling: ')
if spell_word == vocabulary_word: 
	print('correct')
	score += 1
else:
	print('incorrect')
	print(vocabulary_word)
print(score)

 
# Thoughts on project
# Create a list of words by 
# reading all wave file in folder
# and use spelling of file name 
# as key for the spelling words
# and audio recording of words
# for students to spell

# Second thought, show dialog when 
# script opens for folder cantaining
# audio files.



