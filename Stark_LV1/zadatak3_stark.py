brojevi = []

while True:
    x = input("Unesite broj, kada zelite zaustaviti unosenje napisite Done: ")
    if  x.lower() == "done":
        print("Prekinuli ste unos brojeva.")
        break

    try:
        broj = float(x)
        brojevi.append(broj)
    except ValueError:
        print("Unijeli ste ne valjani znak!")

if len(brojevi) > 0:
    brojevi.sort()

    print("Broj brojeva koje je korisnik unio: ", len(brojevi))
    print("Srednja vrijednoste: ", sum(brojevi) / len(brojevi))
    print("Minimalna vrijednost: ", min(brojevi))
    print("Maksimalna vrijednost: ", max(brojevi))
    print("Sortirana lista: ", sorted(brojevi))


    