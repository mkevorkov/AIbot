from audio import speach
from random import randint, choice
import time

levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    words = levels.get(level, [])

    score = 0
    num_attempts = 3

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Произнесите слово {random_word}")
        recog_word = speach().lower()
        print(recog_word)

        if recog_word == random_word:
            print('ДААА')
            score += 1
        else:
            print(f"Нет! Правильное слово: {random_word}")
        time.sleep(2)
    print(f'Игра завершена! Ваш счёт: {score}/{len(words)}')

sel_level = input("easy/medium/hard ")
play_game(sel_level)