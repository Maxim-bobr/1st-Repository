import random
compNum = random.randint(1, 100)
def programma():
    attempts = 0
    while 1 == 1:
        try:
            num = int(input("Привет! Попробуй угадать число, загаданное компьютером в диапазоне от 0 до 100) "))
            attempts += 1
            if num > compNum:
                print("Число компьютера меньше. Попробуй ещё раз ")
            elif num < compNum:
                print("Число компьютера больше. Попробуй ещё раз ")
            if num == compNum:
                print("Поздравляю, ты угадал за ", attempts, " попыток)")
                break
        except ValueError:
            print("Я тебя не понимаю( ")

programma()
