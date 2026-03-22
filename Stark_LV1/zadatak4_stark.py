imeDatoteke = input("Uneiste ime datoteke: ")

try:
    file = open(imeDatoteke)

    suma = 0.0
    brojac = 0

    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            broj = float(line.split(":")[1])
            suma += broj
            brojac += 1

    if brojac > 0:
        prosjek = suma / brojac
        print("Ime datoteke: " +imeDatoteke)
        print("Average X-DSPAM-Confidence: ", prosjek)
    else:
        print("Nema pronađemih linija!")
    
except FileNotFound:
    print("Datoteka nije pronađena!")
