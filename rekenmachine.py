from os import system, name

# welkom bericht
# vraag cijfers en bewerking
# bereken antwoord
# print antwoord
# vraag of je een nieuw cijfer wil berekenen
getal1 = 0
getal2 = 0
bewerking = ""
antwoord = 0


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def print_welkom():
    boodschap = """
  hallo persoon die niet weet dat google een built in calculator heeft
"""
    print(boodschap)


def vraag_input():
    global getal1, getal2, bewerking

    getal1 = int(input("Geef het eerste getal "))
    getal2 = int(input("Geef het tweede getal "))
    bewerking = input("Kies een bewerking uit + - * / : ")


def bereken_antwoord():
    global antwoord

    if bewerking == "-":
        antwoord = getal1 - getal2
    elif bewerking == "+":
        antwoord = getal1 + getal2
    elif bewerking == "*":
        antwoord = getal1 * getal2
    elif bewerking == "/":
        antwoord = getal1 / getal2
    elif bewerking == ":":
        antwoord = getal1 / getal2


def print_antwoord():
    print("Je hebt gevraagd om te berekenen: ")
    print(getal1, bewerking, getal2)
    print("Antwoord:", antwoord)


def rekenmachine():
    print_welkom()

    doorgaan = True

    while doorgaan:
        vraag_input()
        bereken_antwoord()
        print_antwoord()

        if input("Wil je nog een berekening? J/N ").upper() == "N":
            print("kthnxbai!")
            break

        print("Oke, laten we nog een berekening maken")
        # clear the screen
        clear()


rekenmachine()
