import time
import cowsay

while True:
    try:
        n = int(input("Введите число секунд: "))
        while n >= 1:
            n -= 1
            print(n)
            time.sleep(1)
            if n == 1:
                cowsay.cow("Бадабум")
                break
        break
    except ValueError:
        print("Лучше введите число ")
