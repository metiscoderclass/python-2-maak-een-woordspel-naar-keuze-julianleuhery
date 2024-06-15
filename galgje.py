# print galgje ascii
# creer wordje dat geraden moet worden
# vraag voor letter
# speler mag 7 keer een fout letter raden
# als letter goed geraden is zeg dan wat
# als letter fout geraden is zeg dan ook wat
# als meer dan een letter geef fout melding
# als geen letter geef fout melding
# als ? mag de speler het hele woord raden
# wanneer woord geraden is zeg hoera hoera
# wanneer woord niet geraden is zeg wat het woord was

import random
from os import system, name

global galg

galg = [
    """
  +---+
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


# Functie om het scherm leeg te maken
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def welkom():
    clear()
    boodschap = """

   #####
#     #   ##   #       ####       # ######
#        #  #  #      #    #      # #
#  #### #    # #      #           # #####
#     # ###### #      #  ###      # #
#     # #    # #      #    # #    # #
 #####  #    # ######  ####   ####  ######


  hallo ga galgje spelen NU

  type enter om te beginnen
"""
    print(boodschap)
    input()
    clear()


# deze functie maakt een lijst van de woorden uit ons bestand
# en kiest een willekeurig woord uit de lijst:
# eerst shuffelen we de lijst zodat de woorden in willekeurige volgorde staan
# dan kiezen we het eerste woord uit de lijst
# strip de newline van het woord en zet het woord in hoofdletters
def select_word():
    global word
    with open("wordlist.txt") as wordlist:
        words = wordlist.readlines()
        random.shuffle(words)
        word = words[0].strip().upper()


# deze functie schrijft een streepje voor elke letter in het woord
# als de letter al geraden is dan schrijven we de letter
def streepjes():
    streepjes = ""
    for letter in word:
        if letter in letters:
            streepjes += letter
        else:
            streepjes += "_"
    return streepjes


def spel_zelf():
    global letters

    playing = True
    bericht = ""
    letters = ""
    ronde = 1
    fouten = 0

    while playing:
        # begin bovenaan het scherm met de clear functie en print de ronde, galg, streepjes, bericht en geraden letters
        clear()
        print("ronde: " + str(ronde) + "\n\n")

        # hier heeft mama geholpen: de waarde van fouten is de index van de galg lijst. De index begint bij 0.
        # Dus bij nul fouten printen we de eerste galg bij twee fouten de derde galg enzovoort
        print(galg[fouten] + "\n\n")
        print(streepjes() + "\n\n")
        print(bericht + "\n\n")
        print("geraden letters: " + letters + "\n\n")

        # voordat we verder gaan checken we of het woord geraden is of dat de max errors is bereikt
        # als het woord geraden is printen we een hoera bericht en het woord en breken we de loop
        if streepjes() == word:
            clear()
            print(galg[fouten] + "\n\n")
            print("hoera hoera je hebt het woord geraden")
            print("het woord was " + word)
            break

        # als de max errors is bereikt printen we een helaas bericht en het woord en breken we de loop
        if fouten == 7:
            clear()
            print(galg[fouten] + "\n\n")
            print("helaas je hebt het woord niet geraden")
            print("het woord was " + word)
            break

        letter = input("kies één letter of kies ? als je denkt het woord te weten ")
        if letter.lower() == "stop":
            print("Ok. We stoppen het spel nu")
            break

        # we hebben input van de speler, nu gaan we checken of de input valide is
        # is de input meer dan één letter dan geven we een foutmelding en beginnen we deze ronde opnieuw
        if len(letter) > 1:
            bericht = "dat zijn er meer dan één! kies maar één letter"
            continue

        # als de speler een ? invoert dan mag de speler het woord raden
        if letter == "?":
            geraden_woord = input("wat is het woord? ").upper()
            if geraden_woord == word:
                clear()
                print(galg[fouten] + "\n\n")
                print("hoera hoera je hebt het woord geraden")
                print("het woord was " + word)
                break
            else:
                # als het woord niet geraden is dan printen we een helaas bericht
                #  en het woord en beeindigen we het spel
                clear()
                print(galg[7] + "\n\n")
                print("helaas je hebt het woord niet geraden")
                print("het woord was " + word)
                break

        # als de speler geen letter invoert dan geven we een foutmelding
        # en beginnen we deze ronde opnieuw
        if not letter.isalpha():
            bericht = "dat is geen letter. kies een letter"
            continue

        # als de speler een letter invoert die al geraden is dan geven we een foutmelding
        # en beginnen we deze ronde opnieuw
        if letter.upper() in letters:
            bericht = "deze letter heb je al gebruikt dumbo"
            continue

        # als de speler een letter invoert die in het woord zit dan geven we een goed bericht
        # en voegen we de letter toe aan de geraden letters
        # nieuwe ronde
        if letter.upper() in word:
            ronde += 1
            bericht = "goed antwoord. heel knap van je. ga zo door. je bent een topper"
            letters += letter.upper()

        # als de speler een letter invoert die niet in het woord zit dan geven we een fout bericht
        # en voegen we de letter toe aan de geraden letters
        # nieuwe ronde
        if letter.upper() not in word:
            ronde += 1
            fouten += 1
            letters += letter.upper()
            bericht = "fout! haha stoopi dum dum"

    # het spel is over. nog een keer?
    if input("wil je nog een keer spelen? j/n ").upper() == "J":
        galgje()
    else:
        clear()
        print("kthxbai!")


def galgje():
    select_word()
    spel_zelf()


welkom()
galgje()
