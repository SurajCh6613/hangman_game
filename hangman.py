import random
import hangman_stages
word_list = ['apple','beautiful','potato']
lives =6
# Choose Random word from word_list
choosen_word = random.choice(word_list)
print(choosen_word)
display =[]
# To place empty space(_) at the place of words
for i in range(len(choosen_word)):
    display += '_'
print(display)
# Get input word from user
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()   #p   _ p p _ _
    for position in range(len(choosen_word)):  # 0 1 2 3 4 for apple
        letter = choosen_word[position]
        if letter==guessed_letter:
            display[position] = guessed_letter

    print(display)
    if guessed_letter not in choosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Loose The Game!!")
    if '_' not in display:
        game_over = True
        print("You Win")
    print(hangman_stages.stages[lives])