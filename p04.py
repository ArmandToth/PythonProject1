def negyszog(a, b):
    ker = 2 * a + 2 * b
    ter = a * b
    alakzat = "téglalap"
    if a == b:
        alakzat = "négyzet"

    return ker, ter, alakzat

def szamolas(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg, legnagyobb


sorozat = (1,2,"három",4,5)
for elem in sorozat:
    print(elem)

for i in range(10):
    print(i)

for _ in range(10):
    print("Nem leszek rossz!")


print("Összegzés:",szamolas(1, 2, 3))
print("Összegzés:",szamolas(1, 2, 3, 4))
# a = 2
# b = 4
print("Kerület:", negyszog(4, 4)[0])
print("Terület:", negyszog(4, 4)[1])
print("Alakzat:", negyszog(4, 4)[2])
