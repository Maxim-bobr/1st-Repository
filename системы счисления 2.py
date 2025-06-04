while True:
    try:
        a = 0
        while a == 0:
            schisl = input('Введите систему счисления для перевода (2-10): ')
            if 2 <= int(schisl) <= 10:
                chislo1 = input('Введите число в указанной системе счисления: ')
                if int(chislo1) < int(str((int(schisl)-1))*len(chislo1)):
                    schisl2 = input('Введите систему счисления, в которую хотите перевести (2-10): ')
                    if 2 <= int(schisl2) <= 10:
                        a = 1
                    else:
                        print('Введите указанную систему счисления')
                else:
                    print('Введите корректное число (в числе есть цифра, которая отсутствует в алфавите этой системы счисления)')
            else:
                print('Введите указанную систему счисления')

        n = -1
        stepen = 0
        desyatich = 0

        for i in range(len(chislo1)):
            desyatich += int(chislo1[n]) * (int(schisl) ** stepen)
            n -= 1
            stepen += 1
        chastnoe = 0
        itog = ''
        while desyatich > 0:
            itog = str(desyatich % int(schisl2)) + itog
            desyatich = desyatich // int(schisl2)
        print('Число в указанной системе счисления:', itog)
    except ValueError:
        print('Введите лучше число')
