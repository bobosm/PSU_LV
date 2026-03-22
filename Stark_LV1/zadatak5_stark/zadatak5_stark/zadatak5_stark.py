try:
    fhand = open(r"C:\Users\Luka\Desktop\LV1\song.txt")
    brojac = dict()

    for redak in fhand:
        redak = redak.lower()
        rijeci = redak.split()

        for rijec in rijeci:
            brojac[rijec] = brojac.get(rijec, 0) + 1

    fhand.close()

    jedinstveneRijeci = []
    for kljuc in brojac:
        if brojac[kljuc] == 1:
            jedinstveneRijeci.append(kljuc)
    
    print(f"Ukupno riječi koje se pojavljuju samo jednom: {len(jedinstveneRijeci)}")
    print("To su rijeci: ", jedinstveneRijeci)

except FileNotFoundError:
    print("Datoteka nije pronađena!")