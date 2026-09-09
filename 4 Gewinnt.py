feld = []
switch_player = 1

def feld_erstellen(höhe, breite):
    for i in range(höhe):
        feld.insert(i, [])
        for j in range(breite):
            feld[i].insert(j, "-")

def feld_anzeigen():
    for i in range(len(feld)):
        print(feld[i])

def marker_setzen(x, höhe):
    global switch_player
    marker_höhe = 0

    if x < 1 or x > 7:
        print("Die Zahl muss zwischen 1 und 7 liegen")
    for i in range(höhe):
        if feld[i][x-1] == "-" and i <= 4:
            marker_höhe += 1
        elif feld[i][x-1] in ("X", "O") or marker_höhe >= 5:
            if feld[i][x-1] in "-":
                if switch_player == 1:
                    feld[marker_höhe][x - 1] = "X"
                    switch_player = 2
                    marker_position = [marker_höhe, x -1]
                    return marker_position
                else:
                    feld[marker_höhe][x - 1] = "O"
                    switch_player = 1
                    marker_position = [marker_höhe, x - 1]
                    return marker_position
            elif switch_player == 1:
                feld[marker_höhe - 1][x - 1] = "X"
                switch_player = 2
                marker_position = [marker_höhe - 1, x - 1]
                return marker_position
            else:
                feld[marker_höhe - 1][x - 1] = "O"
                switch_player = 1
                marker_position = [marker_höhe - 1, x - 1]
                return marker_position
        else:
            print("Die Reihe ist bereits belegt")

def sieg_check(spieler, marker_position, höhe, breite):
    unentschieden_counter = 0
    for i in range(8):
        if i in (0,1,7):
            x_rotation = 1
        elif i in (2, 6):
            x_rotation = 0
        elif i in (3,4,5):
            x_rotation = -1
        else:
            x_rotation = 0
        if i in (1,2,3):
            y_rotation = 1
        elif i in (0,4):
            y_rotation = 0
        elif i in (5,6,7):
            y_rotation = -1
        else:
            y_rotation = 0

        p0_y, p0_x = marker_position[0], marker_position[1]
        p1_y, p1_x = p0_y + x_rotation, p0_x + y_rotation
        p2_y, p2_x = p0_y + x_rotation * 2, p0_x + y_rotation * 2
        p3_y, p3_x = p0_y + x_rotation * 3, p0_x + y_rotation * 3

        if (0 <= p0_y < höhe and 0 <= p0_x < breite and
                0 <= p1_y < höhe and 0 <= p1_x < breite and
                0 <= p2_y < höhe and 0 <= p2_x < breite and
                0 <= p3_y < höhe and 0 <= p3_x < breite):

            if feld[p0_y][p0_x] == spieler and feld[p1_y][p1_x] == spieler and feld[p2_y][p2_x] == spieler and feld[p3_y][p3_x] == spieler:
                return True

    for j in range(höhe):
        for k in range(breite):
            if feld[j][k] in ("X", "O"):
                unentschieden_counter += 1

    if unentschieden_counter == höhe * breite:
        print("Unentschieden")
        return True

feld_erstellen(6, 7)
feld_anzeigen()

while True:
    marker = marker_setzen(x = int(input("Welche Spalte willst du auswählen (1-7)")), höhe = 6)
    feld_anzeigen()
    x_gewinnt = sieg_check("X", marker, 6, 7)
    o_gewinnt = sieg_check("O", marker, 6, 7)

    if x_gewinnt:
        print("X hat gewonnen")
        break
    elif o_gewinnt:
        print("O hat gewonnen")
        break

    unentschieden_check = sieg_check("O", marker, 6, 7)

    if unentschieden_check:
        break