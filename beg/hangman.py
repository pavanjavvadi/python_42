import random

name = input("Enter your name: ")
print(f"Hi, {name} Welcome to Hangman.\nLet's start the game")
words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks'] 

def get_word(words):
    word = random.choice(words)
    return word

def play(word):
    words_completion = '-' * len(word)
    guessed_words = []
    guessed_letters = []
    guessed = False
    tries = 6
    print(words_completion)
    
    while not guessed and tries > 0:
        guess = input("Enter a alphabet or word: ")
        
        if guess.isalpha() and len(guess)==1:
            if guess in guessed_letters:
                print(f"You had already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} letter is not present in the word.")
                tries -= 1    
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word")
                guessed_letters.append(guess)    
                word_as_list  = list(words_completion)
                indices = [i for i,letter in enumerate(word) if letter==guess]  
                for index in indices:
                    word_as_list[index] = guess
                words_completion = ''.join(word_as_list)
                if '-' not in words_completion:
                    guessed = True
       
        elif guess.isalpha() and len(guess)==len(word):
            if guess in guessed_words:
                print(f"You had already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not a word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                words_completion = word        
            
        else:
            print("Not a valid guess")
            
        print(words_completion)

    if guessed:
        print("Congrats, you guessed the word!")
    else:
        print("Sorry, you are out of tries.The word which you missed : "+word)    

def main():
    word = get_word(words)
    play(word)
    while input("Play Again? (Y/N)").upper() == 'Y':
        word = get_word(words)
        play(word)
if __name__ == "__main__":
    main()