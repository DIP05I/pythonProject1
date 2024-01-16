import modulok
import math

# modulok gyakorlása
print(math.pi)
modulok.udvozles("Aladár")

inputresult = int(input("Írj be egy számot: "))
# inputresult = input("Írj be egy számot: ")

if not (isinstance(inputresult, int)):
    raise TypeError("Nem szám típusút adtál meg.")
else:
    if inputresult < 10:
        raise ValueError("10-nél kisebb számot adtál meg.")