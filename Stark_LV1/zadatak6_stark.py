hamSumaRijeci = 0
hamBrojPoruka = 0

spamSumaRijeci = 0
spamBrojPoruka = 0
spamSUsklicnikom = 0

try:
    file = open(r"C:\Users\Luka\Desktop\LV1\SMSSpamCollection.txt", encoding = "utf-8")

    for line in file:
        parts = line.split()
        if len(parts) < 2:
            continue

        label = parts[0]
        tekstPoruke = parts[1:]
        brojacRijeci = len(tekstPoruke)

        if label == "ham":
            hamSumaRijeci += brojacRijeci
            hamBrojPoruka += 1
        elif label == "spam":
            spamSumaRijeci += brojacRijeci
            spamBrojPoruka += 1

            zadnjaRijec = parts[-1]
            if zadnjaRijec.endswith("!"):
                spamSUsklicnikom += 1

    file.close()

    if hamBrojPoruka > 0:
        print(f"Prosjecan broj rijeci u ham porukama: {hamSumaRijeci / hamBrojPoruka:.2f}")
    if spamBrojPoruka > 0:
        print(f"Prosjecan broj rijeci u spam porukama: {spamSumaRijeci / spamBrojPoruka:.2f}")
        print(f"Spam poruke koje završavaju sa '!': {spamSUsklicnikom}")

except FileNotFoundError:
    print("Datoteka nije pronađena!")



