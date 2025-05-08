from math import sqrt
def programma():
    print("Привет! Тут ты можешь проверить число на квадрат. Если захочешь остановить программу, просто напиши стоп)")
    while True:
        try:
            num = input("Введите положительное число для проверки на квадрат: ")
            if num == "Стоп" or num == "стоп":
                print("Пока!")
                break
            num2 = int(num)
            koren = sqrt(num2)
            if koren % 1:
                n = int(input("Введите точность округления: "))
                print("Число не является квадратом. Приблизительный результат: ", round(koren, n))
            else:
                print("Число является квадратом. Результат: ", koren)
        except ValueError:
            print("Введите лучше число")
programma()
