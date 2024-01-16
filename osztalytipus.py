szo = "hello"
print(type(szo))
#objektum referencuája
print(id(szo))

szo2 = szo
print(id(szo2))

while True:
    try:
        inputszam = int(input("Adj meg egy számot: "))
        break
    except ValuieError:
        print("Nem szám.")
