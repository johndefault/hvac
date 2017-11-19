class Svet:
    def __init__(self,meno):
        self.meno=meno
        self.teplotaVzduchu=20
        self.co2=350
        print("Novy svet",self.meno,"teplota:",self.teplotaVzduchu,"C a co2 je",self.co2,"ppm")

class Priestor:
    def __init__(self,meno,kde):
        self.meno=meno
        self.teplotaVzduchu = kde.teplotaVzduchu
        self.co2 = kde.co2
        self.stav()

    def stav(self):
        print("V priestore",self.meno,"je",self.teplotaVzduchu, "C a", self.co2,"ppm")

class Clovek:
    def __init__(self):
        print("Novy clovek!")


svet=Svet("svet")
dom=Priestor("dom",svet)
obyvacka=Priestor("obyvacka",dom)
ja=Clovek()
obyvacka.stav()
