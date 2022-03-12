
print ('''\n Developed by     _________ _______ _________ _        _______  _ 
|\     /||\     /|\__   __/(  ____ \\__   __/ ( \      (  ____ \( )
| )   ( || )   ( |   ) (   | (    \/   ) (   | (      | (    \/| |
| | _ | || (___) |   | |   | (_____    | |   | |      | (__    | |
| |( )| ||  ___  |   | |   (_____  )   | |   | |      |  __)   | |
| || || || (   ) |   | |         ) |   | |   | |      | (      (_)
| () () || )   ( |___) (___/\____) |   | |   | (____/\| (____/\ _ 
(_______)|/     \|\_______/\_______)   )_(   (_______/(_______/(_)
and SECRET!

''')

secim = input(" 01: Metinden şifreye çevirme\n 02: Şifreden metne çevirme\n\n Lütfen bir işlem seçiniz : ")
if secim == "01":
    
    cumle = input(" Cümleyi gir : ")
    liste = list(cumle)
    bitis = len(liste)
    i = 0

    while i < bitis:
        if liste[i] == "a" or liste[i] == "A":
            print("k", end=".")
        elif liste[i] == "b" or liste[i] == "B":
            print("h", end=".")
        elif liste[i] == "c" or liste[i] == "C" or liste[i] == "ç" or liste[i] == "Ç":
            print("t", end=".")
        elif liste[i] == "d" or liste[i] == "D":
            print("b", end=".")
        elif liste[i] == "e" or liste[i] == "E":
            print("d", end=".")
        elif liste[i] == "f" or liste[i] == "F":
            print("c", end=".")
        elif liste[i] == "g" or liste[i] == "G":
            print("s", end=".")
        elif liste[i] == "h" or liste[i] == "H":
            print("j", end=".")
        elif liste[i] == "i" or liste[i] == "İ" or liste[i] == "ı" or liste[i] == "I":
            print("a", end=".")
        elif liste[i] == "j" or liste[i] == "J":
            print("u", end=".")
        elif liste[i] == "k" or liste[i] == "K":
            print("p", end=".")
        elif liste[i] == "l" or liste[i] == "L":
            print("x", end=".")
        elif liste[i] == "m" or liste[i] == "M":
            print("z", end=".")
        elif liste[i] == "n" or liste[i] == "N":
            print("v", end=".")
        elif liste[i] == "o" or liste[i] == "O" or liste[i] == "ö" or liste[i] == "Ö":
            print("q", end=".")
        elif liste[i] == "p" or liste[i] == "P":
            print("e", end=".")
        elif liste[i] == "q" or liste[i] == "Q":
            print("r", end=".")
        elif liste[i] == "r" or liste[i] == "R":
            print("o", end=".")
        elif liste[i] == "s" or liste[i] == "S" or liste[i] == "ş" or liste[i] == "Ş":
            print("y", end=".")
        elif liste[i] == "t" or liste[i] == "T":
            print("n", end=".")
        elif liste[i] == "u" or liste[i] == "U" or liste[i] == "ü" or liste[i] == "Ü":
            print("w", end=".")
        elif liste[i] == "v" or liste[i] == "V":
            print("m", end=".")
        elif liste[i] == "w" or liste[i] == "W":
            print("l", end=".")
        elif liste[i] == "x" or liste[i] == "X":
            print("i", end=".")
        elif liste[i] == "y" or liste[i] == "Y":
            print("f", end=".")
        elif liste[i] == "z" or liste[i] == "Z":
            print("g", end=".")
        elif liste[i] == " " or liste[i] == "  ":
            print("/", end="")
        else:
            print("!")
        i += 1

elif secim == "02":

    sifre = input(" Şifreyi gir : ")
    liste = list(sifre)
    bitis = len(liste)
    i = 0
    while i < bitis:
        if liste[i] == "k":
            print ("a", end="")
        elif liste[i] == "h":
            print ("b", end="")
        elif liste[i] == "t":
            print ("c", end="")
        elif liste[i] == "b":
            print ("d", end="")
        elif liste[i] == "d":
            print ("e", end="")
        elif liste[i] == "c":
            print ("f", end="")
        elif liste[i] == "s":
            print ("g", end="")
        elif liste[i] == "j":
            print ("h", end="")
        elif liste[i] == "a":
            print ("i", end="")
        elif liste[i] == "u":
            print ("j", end="")
        elif liste[i] == "p":
            print ("k", end="")
        elif liste[i] == "x":
            print ("l", end="")
        elif liste[i] == "z":
            print ("m", end="")
        elif liste[i] == "v":
            print ("n", end="")
        elif liste[i] == "q":
            print ("o", end="")
        elif liste[i] == "e":
            print ("p", end="")
        elif liste[i] == "r":
            print ("q", end="")
        elif liste[i] == "o":
            print ("r", end="")
        elif liste[i] == "y":
            print ("s", end="")
        elif liste[i] == "n":
            print ("t", end="")
        elif liste[i] == "w":
            print ("u", end="")
        elif liste[i] == "m":
            print ("v", end="")
        elif liste[i] == "l":
            print ("w", end="")
        elif liste[i] == "i":
            print ("x", end="")
        elif liste[i] == "f":
            print ("y", end="")
        elif liste[i] == "g":
            print ("z", end="")
        elif liste[i] == "/":
            print (" ", end="")

        i += 1




else:
    print(" GEÇERSİZ İŞLEM!")