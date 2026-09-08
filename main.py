feld = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
switch_player = 1

def feld_anzeigen():
    print(feld[0])
    print(feld[1])
    print(feld[2])

def marker_setzen(x, y):
    global switch_player

    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Die Zahl muss zwischen 1 und 3 liegen")
    elif feld[y - 1][x - 1] == "-":
        if switch_player == 1:
            feld[y - 1][x - 1] = "X"
            switch_player = 2
        else:
            feld[y - 1][x - 1] = "O"
            switch_player = 1
    else:
        print("Das Feld ist bereits belegt")

def sieg_check(feld, spieler):
    for reihe in feld:
        if reihe == [spieler, spieler, spieler]:
            return True
    for col in range(3):
        if feld[0][col] == spieler and feld[1][col] == spieler and feld[2][col] == spieler:
            return True

    if feld[0][0] == spieler and feld[1][1] == spieler and feld[2][2] == spieler:
        return True
    if feld[2][0] == spieler and feld[1][1] == spieler and feld[0][2] == spieler:
        return True
    else:
        return False

feld_anzeigen()

while True:
    marker_setzen(x = int(input("Welche Spalte willst du auswählen (1-3)")), y = int(input("Welche Ziele willst du auswählen (1-3")))
    x_gewinnt = sieg_check(feld, "X")
    o_gewinnt = sieg_check(feld, "O")
    feld_anzeigen()

    if x_gewinnt:
        print("X hat gewonnen")
        break
    elif o_gewinnt:
        print("O hat gewonnen")
        break

