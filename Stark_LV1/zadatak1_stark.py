
def total_euro(x, y):
    total = x * y
    print("Cjelokupna zarada: ", total, "Eur/h." )

x = int(input("Unesi broj radnih sati: "))
y = int(input("Unesi zaradu po satu: "))
total = x * y

print("Broj radnih sati: ", x)
print("Eur/h: ", y)

total_euro(x, y)

