
def proverka_writeln():
    #if "'" not in a:
        #print("Error 52")
        #exit()
    if "(" not in a:
        print("Error 52")
        exit()
    if ")" not in a:
        print("Error 52")
        exit()

def Peremennie():
    global PEREMEN
    if ":=" in a:
        x = a[0:a.find(":=")-0]
        x.strip()
        znach = a[a.find(':') + 2:]
        try:
            cnisl = int(znach)
            #if "*" in a:
                #umnoz = cnisl * a[a.find("*"):]
                #print(umnoz)
        except ValueError:
            if "'" not in znach:
                print("Error 52")
                exit()
            znach.strip()
            znach = znach[1:-1]
            znach.strip()
        peremenn[x] = znach.strip()
        for k in peremenn.keys():
            PEREMEN.append(k)
            print(PEREMEN)
            print(peremenn)
        PEREMEN = list(set(PEREMEN))
print("begin")
OK = []
poryadoc = []
n = 0
a = ""
peremenn = {}
i = 1
o = 1
g = 1
PEREMEN = []
while a != "end.":
    n += 1
    a = input(str(n) + ") ")
    a.strip()
    pon = a[:7]
    if pon.lower() == "writeln":
        proverka_writeln()
        #keys = peremenn.keys()
        Peremennie()
        #for k in peremenn.keys():
            #PEREMEN.append(k)
            #print(PEREMEN)
        word1 = a[a.find("(")+1:a.find(")")-0]
        print(word1)
        print(len(PEREMEN))
        if len(PEREMEN) >= 1:
            #print(PEREMEN[i])
            if "*" in word1:
                mnoz = word1[0:word1.find("*")]
                mnoz2 = word1[word1.find("*")+1:]
                print(mnoz)
                print(mnoz2)
                mnoz = peremenn[PEREMEN[g]]
                mnoz2 = peremenn[PEREMEN[o]]
                word1 = int(mnoz) * int(mnoz2)
                print(word1)
            elif "-" in word1:
                umensh = word1[0:word1.find("-")]
                vichit = word1[word1.find("-")+1:]
                print(umensh)
                print(vichit)
                for umensh in PEREMEN[g]:
                    umensh = peremenn[PEREMEN[g]]
                    g += 1
                for vichit in PEREMEN[o]:
                    vichit = peremenn[PEREMEN[o]]
                    o += 1
                print(umensh)
                print(vichit)

                word1 = int(umensh) - int(vichit)
                print(word1)
            elif "/" in word1:
                delim = word1[0:word1.find("/")]
                delitel = word1[word1.find("/")+1:]
                #for PEREMEN[i] in delim:
                delim = peremenn[PEREMEN[i]]
                    #i += 1
                print(delim)
                #for PEREMEN[o] in delitel:
                delitel = peremenn[PEREMEN[o]]
                    #o += 1
                print(delitel)
                word1 = int(delim) / int(delitel)
                print(word1)
            elif "+" in word1:
                slag1 = word1[0:word1.find("+")]
                slag2 = word1[word1.find("+")+1:]
                #for PEREMEN[i] in slag1:
                slag1 = peremenn[PEREMEN[i]]
                    #i += 1
                print(slag1)
                #for PEREMEN[o] in slag2:
                slag2 = peremenn[PEREMEN[o]]
                    #o += 1
                print(slag2)
                word1 = int(slag1) + int(slag2)
                print(word1)
            else:
                for PEREMEN[i] in word1:
                    word1 = peremenn[PEREMEN[i]]
                    i += 1
                    print(word1)

        OK.append(word1)
        poryadoc.append(1)

    if ":=" in a:
        Peremennie()



m = 0
lena = len(poryadoc)
print(poryadoc)
print(lena)
print(OK)
if a == "end." or a == "Готово":
    print()
    print("-----------------")
    while lena > 0:
        for i in poryadoc:
            if i == 1:
                print(OK[m])
                m += 1
                lena -= 1
                i += 1

