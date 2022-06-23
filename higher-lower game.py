import random
import time

from pygame import mixer

machine_guess = random.randint(1,100)
lives = 0

game_mode = input("For hard mode, press h, for easy mode press e ").lower()
if game_mode == "h":
    lives = 5
else:
    lives = 9

game_on = True
while game_on:
    user_guess = int(input("Choose a number between 1 and 100 "))
    if user_guess >= 101:
        print("Only numbers between 1 and 100 allowed")
    else:
        if user_guess == machine_guess:
            mixer.init()
            mixer.music.load("tada-fanfare-a-6313.mp3")
            mixer.music.play()
            print("Congrats, you win the game! ")
            while mixer.music.get_busy():
                time.sleep(0.0001)
            game_on = False


        elif user_guess < machine_guess:
            print("Target number is higher")
            mixer.init()
            mixer.music.load("negative_beeps-6008.mp3")
            mixer.music.play()
            lives -= 1
            print(f"{lives} live(s) left")
        else:
            print("Target number is lower")
            mixer.init()
            mixer.music.load("negative_beeps-6008.mp3")
            mixer.music.play()
            lives -= 1
            print(f"{lives} live(s) left")

    if lives == 0:

        print(f"The machine guess is {machine_guess}")
        print("You lose")
        mixer.init()
        mixer.music.load("no-luck-too-bad-disappointing-sound-effect-112943.mp3")
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(0.0001)
        game_on = False



