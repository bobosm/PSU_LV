try:
    x = float(input("Unesite ocjenu[u rasponu od 0.0 do 1.0]: "))
    match x:
        case x if 0.9 <= x <= 1.0: 
            print("Ocjena je A.")
        case x if 0.8 <= x < 0.9:
            print("ocjena je B.")
        case x if 0.7 <= x < 0.8:
            print("Ocjena je C.")
        case x if 0.6 <= x < 0.7:
            print("Ocjena je D.")
        case x if x < 0.6 and x > 0.0:
            print("Ocjena je F. Pali ste!")
        case x if x < 0.0 or 1.0 < x:
            print("Upisali ste broj koji nije ocjena!")
except ValueError:
    print("Niste unijeli valjani znak!")