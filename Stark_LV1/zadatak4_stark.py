imeDatoteke = input("Uneiste ime datoteke: ")

file = open(imeDatoteke)

suma = None
brojac = None

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        broj = float(line.split(":")[1])
        suma += broj
        brojac += 1

prosjek = suma / brojac

print("Ime datoteke: " +imeDatoteke)
print("Average X-DSPAM-Confidence: ", prosjek)