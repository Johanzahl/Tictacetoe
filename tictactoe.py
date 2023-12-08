bräde = [' ' for x in range(10)]

def sättInBokstav(bokstav, pos):
    bräde[pos] = bokstav

def platsÄrLedig(pos):
    return bräde[pos] == ' '

def skrivUtBräde(bräde):
    print('   |   |   ')
    print(' ' + bräde[1] + ' | ' + bräde[2] + ' | ' + bräde[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[4] + ' | ' + bräde[5] + ' | ' + bräde[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[7] + ' | ' + bräde[8] + ' | ' + bräde[9])
    print('   |   |   ')

def ärBrädetFullt(bräde):
    if bräde.count(' ') > 1:
        return False
    else:
        return True

def ärVinnare(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

def spelarDrag():
    kör = True
    while kör:
        drag = input("Vänligen välj en position för att placera X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if drag > 0 and drag < 10:
                if platsÄrLedig(drag):
                    kör = False
                    sättInBokstav('X', drag)
                else:
                    print('Tyvärr, denna plats är upptagen')
            else:
                print('Vänligen skriv ett nummer mellan 1 och 9')

        except:
            print('Vänligen skriv ett nummer')

def datornsDrag():
    möjligaDrag = [x for x, bokstav in enumerate(bräde) if bokstav == ' ' and x != 0]
    drag = 0

    for bokstav in ['O', 'X']:
        for i in möjligaDrag:
            brädeKopia = bräde[:]
            brädeKopia[i] = bokstav
            if ärVinnare(brädeKopia, bokstav):
                drag = i
                return drag

    hörnÖppna = []
    for i in möjligaDrag:
        if i in [1, 3, 7, 9]:
            hörnÖppna.append(i)

    if len(hörnÖppna) > 0:
        drag = slumpa(hörnÖppna)
        return drag

    if 5 in möjligaDrag:
        drag = 5
        return drag

    kanterÖppna = []
    for i in möjligaDrag:
        if i in [2, 4, 6, 8]:
            kanterÖppna.append(i)

    if len(kanterÖppna) > 0:
        drag = slumpa(kanterÖppna)
        return drag

def slumpa(lista):
    import random
    ln = len(lista)
    r = random.randrange(0, ln)
    return lista[r]

def huvudprogram():
    print("Välkommen till spelet!")
    skrivUtBräde(bräde)

    while not(ärBrädetFullt(bräde)):
        if not(ärVinnare(bräde, 'O')):
            spelarDrag()
            skrivUtBräde(bräde)
        else:
            print("Tyvärr, du förlorar!")
            break

        if not(ärVinnare(bräde, 'X')):
            drag = datornsDrag()
            if drag == 0:
                print(" ")
            else:
                sättInBokstav('O', drag)
                print('Datorn placerade en O på position', drag, ':')
                skrivUtBräde(bräde)
        else:
            print("Grattis, du vinner!")
            break

    if ärBrädetFullt(bräde):
        print("Oavgjort spel")

while True:
 x = input("Vill du spela? Tryck på y för ja eller n för nej (y/n)\n")
 if x.lower() == 'y':
        bräde = [' ' for x in range(10)]
        print('--------------------')
        huvudprogram()
 else:
        break
