def perevodVdecytich():
    while True:
        try:
            yesNo = input("Введите систему счисления(от 2 до 10): ")
            if yesNo == "Стоп" or yesNo == "стоп":
                print("Пока!")
                break
            schisl = int(yesNo)
            if 2 <= schisl <= 10:
                chislo = input("Введите число в указанной системе счисления: ")
                n = -1
                stepen = 0
                desytich = 0

                for i in range(len(chislo)):
                    desytich += int(chislo[n]) * (schisl ** stepen)
                    n -= 1
                    stepen += 1
                print("Получилось число ", desytich)
            else:
                print("Введите число в указанном диапазоне")
        except ValueError:
            print("Введите лучше число")
def perevodVdruguy():
    print("Привет! Здесь ты можешь перевести число из одной системы счисления в другую. Чтобы выйти, напиши стоп)")
    perevodVdecytich()

print("Привет! В этой программе ты можешь перевести число в десятичную или в другие системы.")
while True:
    oneORtwo = input("Напиши 1 для перевода в десятичную, 2 - для перевода в другую. ")
    if oneORtwo == "1":
        print("Здесь ты можешь перевести из указанной системы счисления в десятичную. Чтобы выйти, напиши стоп) ")
        perevodVdecytich()
        break
    if oneORtwo == "2":
        perevodVdruguy()
    else:
        pon = None
