class Teglalap():
    alakzat = "téglalap"
    def __init__(self, alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag
        print(f"A {self.alakzat}  alapja = {self.alap}")
        print(f"A {self.alakzat}  magassag = {self.magassag}")

    def kerulet(self):
        return 2 * self.alap + 2 * self.magassag

    def terulet(self):
        return self.alap * self.magassag
tegla = Teglalap(20,15)
print("A kerülete = ", tegla.kerulet())
print("A területe = ", tegla.terulet())